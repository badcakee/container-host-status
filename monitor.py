import requests
import psutil
import shutil
import platform
import os
import time
from collections import deque

# === CONFIG ===
WEBHOOK_URL = "https://discord.com/api/webhooks/XXX/YYY?wait=true"  # <== your webhook with ?wait=true
UPDATE_INTERVAL = 0.5       # seconds
HISTORY_POINTS = 3600     # keep 1h of history

# === HISTORY BUFFERS ===
cpu_hist = deque(maxlen=HISTORY_POINTS)
ram_hist = deque(maxlen=HISTORY_POINTS)
disk_hist = deque(maxlen=HISTORY_POINTS)
swap_hist = deque(maxlen=HISTORY_POINTS)

# === UTILS ===
def bytes_to_gb(value):
    return round(value / (1024**3), 2)

def get_cpu_model():
    try:
        if os.name == "posix":  # Linux
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":", 1)[1].strip()
        return platform.uname().processor or platform.processor() or "Unknown CPU"
    except:
        return "Unknown CPU"

def get_system_specs():
    cpu_name = get_cpu_model()
    try:
        freq = psutil.cpu_freq()
        cpu_ghz = round(freq.max / 1000, 2) if freq and freq.max else "N/A"
    except:
        cpu_ghz = "N/A"

    ram_total = bytes_to_gb(psutil.virtual_memory().total)
    disk_total = bytes_to_gb(shutil.disk_usage("/").total)
    swap_total = bytes_to_gb(psutil.swap_memory().total)

    cores = psutil.cpu_count(logical=False) or 0
    threads = psutil.cpu_count(logical=True) or 0

    return cpu_name, cpu_ghz, ram_total, disk_total, swap_total, cores, threads

def get_metrics():
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    disk = shutil.disk_usage("/")
    disk_used = round(disk.used / disk.total * 100, 1)
    return cpu, ram, swap, disk_used

def calc_stats(history):
    if not history:
        return 0, 0, 0, 0
    avg = round(sum(history)/len(history), 1)
    hi = round(max(history), 1)
    lo = round(min(history), 1)
    latest = round(history[-1], 1)
    return latest, avg, hi, lo

# === MAIN ===
def main():
    specs = get_system_specs()
    cpu_name, cpu_ghz, ram_total, disk_total, swap_total, cores, threads = specs

    # --- Send the first proper embed ---
    embed = {
        "title": "📊 Host Monitor",
        "color": 0x00ff00,
        "fields": [
            {
                "name": "⚙️ Specs",
                "value": f"**CPU:** {cpu_name} @ {cpu_ghz} GHz\n"
                         f"**Cores/Threads:** {cores}/{threads}\n"
                         f"**RAM:** {ram_total} GB\n"
                         f"**Disk:** {disk_total} GB\n"
                         f"**Swap:** {swap_total} GB",
                "inline": False
            },
            {"name": "🖥️ CPU", "value": "Loading...", "inline": True},
            {"name": "💾 RAM", "value": "Loading...", "inline": True},
            {"name": "🔄 Swap", "value": "Loading...", "inline": True},
            {"name": "📀 Disk", "value": "Loading...", "inline": True},
        ],
        "footer": {"text": "Updating every half a second • Tracking last 1 hour"}
    }

    resp = requests.post(WEBHOOK_URL, json={"embeds": [embed]})
    if resp.status_code >= 300:
        print("❌ Failed to send initial webhook:", resp.status_code, resp.text)
        return

    try:
        message_id = resp.json()["id"]
    except Exception:
        print("❌ Webhook did not return JSON. Make sure URL ends with ?wait=true")
        return

    base_url = WEBHOOK_URL.split("?")[0]

    # --- Update loop ---
    while True:
        cpu, ram, swap, disk = get_metrics()
        cpu_hist.append(cpu)
        ram_hist.append(ram)
        swap_hist.append(swap)
        disk_hist.append(disk)

        cpu_now, cpu_avg, cpu_hi, cpu_lo = calc_stats(cpu_hist)
        ram_now, ram_avg, ram_hi, ram_lo = calc_stats(ram_hist)
        swap_now, swap_avg, swap_hi, swap_lo = calc_stats(swap_hist)
        disk_now, disk_avg, disk_hi, disk_lo = calc_stats(disk_hist)

        embed["color"] = 0x00ff00 if cpu_now < 70 else 0xffa500 if cpu_now < 90 else 0xff0000
        embed["fields"][1]["value"] = f"Now: {cpu_now}%\nAvg(1h): {cpu_avg}%\nHigh: {cpu_hi}%\nLow: {cpu_lo}%"
        embed["fields"][2]["value"] = f"Now: {ram_now}%\nAvg(1h): {ram_avg}%\nHigh: {ram_hi}%\nLow: {ram_lo}%"
        embed["fields"][3]["value"] = f"Now: {swap_now}%\nAvg(1h): {swap_avg}%\nHigh: {swap_hi}%\nLow: {swap_lo}%"
        embed["fields"][4]["value"] = f"Now: {disk_now}%\nAvg(1h): {disk_avg}%\nHigh: {disk_hi}%\nLow: {disk_lo}%"

        url = f"{base_url}/messages/{message_id}"
        r = requests.patch(url, json={"embeds": [embed]})
        if r.status_code >= 300:
            print("❌ Failed to edit webhook message:", r.status_code, r.text)

        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
