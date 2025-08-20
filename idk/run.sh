python3 monitor.py &
clear
echo -e "\e[1;33mcontainer@pterodactyl~\e[0m Server marked as running...
\e[1;33mcontainer@pterodactyl~\e[0m java -version
openjdk version \"21.0.7\" 2025-04-15 LTS
OpenJDK Runtime Environment Temurin-21.0.7+6 (build 21.0.7+6-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.7+6 (build 21.0.7+6-LTS, mixed mode, sharing)
\e[1;33mcontainer@pterodactyl~\e[0m java -Xms128M -XX:MaxRAMPercentage=95.0 -Dterminal.jline=false -Dterminal.ansi=true -jar server.jar
Starting org.bukkit.craftbukkit.Main
[00:27:49 INFO]: [bootstrap] Running Java 21 (OpenJDK 64-Bit Server VM 21.0.7+6-LTS; Eclipse Adoptium Temurin-21.0.7+6) on Linux 6.12.34-0-lts (amd64)
[00:27:49 INFO]: [bootstrap] Loading Paper 1.21.8-36-main@47f983f (2025-08-17T12:02:12Z) for Minecraft 1.21.8
[00:27:49 INFO]: [PluginInitializerManager] Initializing plugins...
[00:27:50 INFO]: [PluginInitializerManager] Initialized 0 plugins
[00:28:02 INFO]: Environment: Environment[sessionHost=https://sessionserver.mojang.com, servicesHost=https://api.minecraftservices.com, name=PROD]
[00:28:06 INFO]: Loaded 1407 recipes
[00:28:06 INFO]: Loaded 1520 advancements
[00:28:06 INFO]: [ca.spottedleaf.dataconverter.minecraft.datatypes.MCTypeRegistry] Initialising converters for DataConverter...
[00:28:08 INFO]: [ca.spottedleaf.dataconverter.minecraft.datatypes.MCTypeRegistry] Finished initialising converters for DataConverter in 1,199.8ms
[00:28:08 INFO]: Starting minecraft server version 1.21.8
[00:28:08 INFO]: Loading properties
[00:28:08 INFO]: This server is running Paper version 1.21.8-36-main@47f983f (2025-08-17T12:02:12Z) (Implementing API version 1.21.8-R0.1-SNAPSHOT)
[00:28:09 INFO]: [spark] This server bundles the spark profiler. For more information please visit https://docs.papermc.io/paper/profiling
[00:28:09 INFO]: Server Ping Player Sample Count: 12
[00:28:09 INFO]: Using 4 threads for Netty based IO
[00:28:11 INFO]: [MoonriseCommon] Paper is using 1 worker threads, 1 I/O threads
[00:28:11 INFO]: [ChunkTaskScheduler] Chunk system is using population gen parallelism: true
[00:28:12 INFO]: Default game type: SURVIVAL
[00:28:12 INFO]: Generating keypair
[00:28:12 INFO]: Starting Minecraft server on 0.0.0.0:27203
[00:28:12 INFO]: Using epoll channel type
[00:28:12 INFO]: Paper: Using libdeflate (Linux x86_64) compression from Velocity.
[00:28:12 INFO]: Paper: Using OpenSSL 3.x.x (Linux x86_64) cipher from Velocity.
[00:28:12 INFO]: Server permissions file permissions.yml is empty, ignoring it
[00:28:12 INFO]: Preparing level \"world\"
[00:28:13 INFO]: Preparing start region for dimension minecraft:overworld
[00:28:13 INFO]: Preparing spawn area: 0%
[00:28:14 INFO]: Preparing spawn area: 2%
[00:28:14 INFO]: Preparing spawn area: 8%
[00:28:14 INFO]: Time elapsed: 1177 ms
[00:28:14 INFO]: Preparing start region for dimension minecraft:the_nether
[00:28:14 INFO]: Preparing spawn area: 0%
[00:28:15 INFO]: Preparing spawn area: 10%
[00:28:15 INFO]: Preparing spawn area: 10%
[00:28:15 INFO]: Time elapsed: 1225 ms
[00:28:15 INFO]: Preparing start region for dimension minecraft:the_end
[00:28:15 INFO]: Preparing spawn area: 0%
[00:28:16 INFO]: Time elapsed: 318 ms
[00:28:16 INFO]: [spark] Starting background profiler...
[00:28:17 INFO]: Done preparing level \"world\" (4.338s)
[00:28:17 INFO]: Running delayed init tasks
[00:28:17 INFO]: Done (30.074s)! For help, type \"help\""
