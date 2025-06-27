---
layout: post
title: "Stix Free Utility"
date: 2025-06-27
permalink: /stixfreeutility/
---


 Stix is a YouTuber and optimizer (over 1yr+). All information regarding the free utility comes as of June 3rd, 2025; information is bound to change as he updates his tools.





[Youtube Video Summary](https://www.youtube.com/watch?v=LRijhBlQDG4)




 I'll start with benchmarks first because the code review will get fairly lengthly; the link to the utility will be at the bottom, make sure to read my warning next to the link if you choose to visit.



### How does it affect PC performance?



 It's important to remember that any sorts of gains or losses will vary from one machine to another, as we all have different components; but on my system (3080ti, 5950x, 32gb ddr4) here are how the utility fared against "before and after" on a clean install of 23h2 Win11 Pro



Starting with driver latency captured with the Windows Performance Toolkit; data is measured in microseconds


**nvlddmkm.sys** or the nvidia gpu driver saw a major decrease to the max value of latency while the average latency was taken down close to 50%


**ntoskrnl.sys** or the system kernel didn't deviate much from the max value of latency, but the average latency was reduced close to 84%


**dxgkrnl.sys** or the direct X kernel also didn't have a huge variation of max values before and after, but the average latency was reduced close to 44%



***Click for Latency Benchmark***
![system latency](/images/stixfree/stixfreelat.png)


Onto FPS; for Fortnite we saw roughly a 120 average boost with solid gains to the 1 and 0.2 percentiles. 



***Click for Fortnite Benchmark***
![fortnite fps](/images/stixfree/stixfreefort.png)


In Valorant, we didn't see a major boost to the average frames, but the percentiles did see some massive improvements



***Click for Valorant Benchmark***
![valorant fps](/images/stixfree/stixfreeval.png)


### The Code and What it Does


Here is the utility in its entirety as of version 2.7


![stix free utility](/images/stixfree/stixfreeutil.png)


#### Option 0: Download Resources


is required for the utility to work for its maximum potential; the code for 0 is



***Click to See Batch Code***

```

curl -g -k -L -# -o "%temp%\Stix Free.zip" "https://www.dropbox.com/scl/fi/qdgw7wcn7oesd3rbfu883/Stix-Free.zip?rlkey=6ed88ulyityakfpyv7f0que9d&st=6eeunx33&dl=1" >nul 2>&1
powershell -NoProfile Expand-Archive '%temp%\Stix Free.zip' -DestinationPath 'C:\' >nul 2>&1
  
```


... and the result of running this is the downloading of this file(provided in screenshot below) which allows the other options 1-11 to properly function later on.



***Click for Resulting File***
![screenshot of apps](/images/stixfree/optionzero.png)




#### Option 1: Windows Settings



##### Changes Made


* **Boot Config:** Tweaks timers and disables dynamic ticking.
* **Thread & Heap:** Disables Thread DPC and Fault Tolerant Heap.
* **CSRSS:** Boosts IO and CPU priority for csrss.exe.
* **Multimedia:** Tunes thread scheduling and responsiveness.
* **Game Mode:** Enables automatic game optimizations.
* **Latency:** Removes IoLatencyCaps from services.
* **Power:** Disables power throttling, hibernation, sleep study, and storage sense.
* **GPU:** Enables Hardware-Accelerated GPU Scheduling (HAGS).
* **Privacy:** Disables telemetry, tracking, location, and transparency.
* **VBS:** Disables Virtualization-Based Security.
* **MMCSS:** Fully disables the multimedia scheduler service.
* **Priority Tuning:** Sets Win32PrioritySeparation to 42.
* **DMA:** Disables DMA remapping for all services.
* **Windows Update:** Uses Wub.exe to disable updates.




***Click to See Batch Code***

```

echo - Optimizing Boot Config
bcdedit /deletevalue useplatformclock >nul 2>&1
bcdedit /set disabledynamictick yes >nul 2>&1
bcdedit /set useplatformtick yes >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling ThreadDPC
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ThreadDpcEnable" /t REG_DWORD /d "0" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Fault Tolerant Heap
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\FTH" /v Enabled /t REG_DWORD /d 0 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Setting CSRSS IO and CPU Priority
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions" /v "CpuPriorityClass" /t REG_DWORD /d "3" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions" /v "IoPriority" /t REG_DWORD /d "3" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Setting System Responsiveness
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d "0" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling IoLatencyCap
FOR /F "eol=E" %%a in ('REG QUERY "HKLM\SYSTEM\CurrentControlSet\Services" /S /F "IoLatencyCap"^| FINDSTR /V "IoLatencyCap"') DO (
	REG ADD "%%a" /F /V "IoLatencyCap" /T REG_DWORD /d 0 >nul 2>&1... FOR /F "tokens=*" %%z IN ("%%a") DO (
		SET STR=%%z
		SET STR=!STR:HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\=!
		SET STR=!STR:\Parameters=!
	)
)
timeout 2 >nul 2>&1
echo - Enabling Game Mode
reg add "HKCU\SOFTWARE\Microsoft\GameBar" /v "AllowAutoGameMode" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\GameBar" /v "AutoGameModeEnabled" /t REG_DWORD /d "1" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling StorPort Idle
for /f "tokens=*" %%s in ('reg query "HKLM\System\CurrentControlSet\Enum" /S /F "StorPort" ^| findstr /e "StorPort"') do reg add "%%s" /v "EnableIdlePowerManagement" /t REG_DWORD /d "0" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Enabling HAGS
reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d 2 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Windows Tracking
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\Maps" /v "AutoUpdateEnabled" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKCU\Software\Policies\Microsoft\Windows\WindowsCopilot" /v TurnOffWindowsCopilot /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKCU\Software\Policies\Microsoft\Windows\Explorer" /v "DisableNotificationCenter" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" /v "DisableWindowsLocationProvider" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" /v "DisableLocationScripting" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" /v "DisableLocation" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Input\TIPC" /v "Enabled" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Biometrics" /v "Enabled" /t REG_DWORD /d 0 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Optimizing System Profile
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SchedulerPeriod" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NoLazyMode" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "MaxThreadsTotal" /t REG_DWORD /d 128 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "MaxThreadsPerProcess" /t REG_DWORD /d 10 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "LazyModeTimeout" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "IdleDetectionCycles" /t REG_DWORD /d 0 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling VBS
reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 0 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Power Throttling & Hibernation
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /v "PowerThrottlingOff" /t REG_DWORD /d 1 /f >nul 2>&1
powercfg -h off
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v "HiberBootEnabled" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power" /v "HibernateEnabled" /t REG_DWORD /d 0 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Storage Sense
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy" /v "01" /t REG_DWORD /d 0 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Sleep Study
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "SleepstudyAccountingEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v "SleepStudyDisabled" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v "SleepStudyDeviceAccountingLevel" /t REG_DWORD /d "0" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Energy Logging
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "DisableTaggedEnergyLogging" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxApplication" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxTagPerApplication" /t REG_DWORD /d "0" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling MMCSS
reg add "HKLM\SYSTEM\CurrentControlSet\Services\MMCSS" /v "Start" /t REG_DWORD /d "4" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Setting Win32 Priority Seperation Value
reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 42 /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling DMA Remapping
for %%a in (DmaRemappingCompatible) do for /f "delims=" %%b in ('reg query "HKLM\SYSTEM\CurrentControlSet\Services" /s /f "%%a" ^| findstr "HKEY"') do Reg.exe add "%%b" /v "%%a" /t REG_DWORD /d "0" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Windows Updates
"C:\Stix Free\Wub.exe"
  
```


#### Option 2: Power Gating



##### Changes Made


* **DisableDynamicPstate:** Disables dynamic P-state scaling for GPU or display adapters (registry path under class {4d36e968...}).
* **Force D0 State:** Iterates through all Plug and Play devices and sets their default power state to D0 (fully on), ensuring devices don't downclock or sleep unnecessarily.




***Click to See Batch Code***

```

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0001" /v "DisableDynamicPstate" /t REG_DWORD /d "1" /f >nul 2>&1
timeout 2 >nul 2>&1
echo - Forcing D0 State
for /f "tokens=1,2 delims==" %%a in ('wmic path Win32_PnPEntity get DeviceID /value') do (
    if not "%%a"=="" (
        set dev=%%a
        set dev=!dev:~0,-1!
        reg add "HKLM\SYSTEM\CurrentControlSet\Enum\!dev!\Device Parameters\Power" /v DefaultPowerState /t REG_DWORD /d 0 /f >nul 2>&1
    )
)
  
```


#### Option 3: Telemetry Removal



##### Changes Made


* **Ran O&O ShutUp10:** Executes with predefined config if present.
* **Disabled Preinstalled Apps:** Stops Microsoft from reinstalling or silently enabling built-in apps.
* **Disabled Tracking & Telemetry:** Blocks diagnostics, advertising ID, activity history, Cortana, CDP, and experiment features.
* **Hardened Search Settings:** Disables Bing integration, Cortana features, and web search results.
* **Disabled Scheduled Tasks:** Turns off various diagnostics and efficiency analysis background tasks.
* **Disabled Autologgers:** Prevents logging of system events like ReadyBoot, Defender logs, and RDP graphics traces.




***Click to See Batch Code***

```

set OOSUPath="C:\Stix Free\OOSU10.exe"
set ConfigPath="C:\Stix Free\Stix-OOSU.cfg"

if exist %OOSUPath% (
    if exist %ConfigPath% (
        %OOSUPath% %ConfigPath%
    )
)
echo - Stop Reinstalling Preinstalled Apps 
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "PreInstalledAppsEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SilentInstalledAppsEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "OemPreInstalledAppsEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "ContentDeliveryAllowed" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SubscribedContentEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "PreInstalledAppsEverEnabled" /t REG_DWORD /d "0" /f>nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Windows Tracking
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CDP" /v "CdpSessionUserAuthzPolicy" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CDP" /v "NearShareChannelUserAuthzPolicy" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance" /v "MaintenanceDisabled" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\PolicyManager\current\device\System" /v "AllowExperimentation" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\PolicyManager\default\System\AllowExperimentation" /v "value" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Feeds" /v "EnableFeeds" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft" /v "AllowNewsAndInterests" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\Control Panel\International\User Profile" /v "HttpAcceptLanguageOptOut" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v "BingSearchEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v "CortanaCapabilities" /t REG_SZ /d "" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v "IsAssignedAccess" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v "IsWindowsHelloActive" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "AllowSearchToUseLocation" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchPrivacy" /t REG_DWORD /d 3 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchSafeSearch" /t REG_DWORD /d 3 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchUseWeb" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchUseWebOverMeteredConnections" /t >nul 2>&1
reg add "HKLM\Software\Microsoft\PolicyManager\default\Experience\AllowCortana" /v "value" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\SearchCompanion" /v "DisableContentFileUpdates" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "AllowCloudSearch" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "AllowCortanaAboveLock" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "AllowSearchToUseLocation" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchPrivacy" /t REG_DWORD /d "3" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchUseWeb" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "ConnectedSearchUseWebOverMeteredConnections" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "DisableWebSearch" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "DoNotUseWebResults" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "AITEnable" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "AllowTelemetry" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "DisableInventory" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "DisableUAR" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "DisableEngine" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "DisablePCA" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Privacy" /v "TailoredExperiencesWithDiagnosticDataEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack" /v "ShowedToastAtLevel" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKEY_CURRENT_USER\Software\Microsoft\Input\TIPC" /v "Enabled" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKEY_CURRENT_USER\Control Panel\International\User Profile" /v "HttpAcceptLanguageOptOut" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Attachments" /v "SaveZoneInformation" /t REG_DWORD /d "1" /f >nul 2>&1
reg add "HKLM\System\CurrentControlSet\Control\Diagnostics\Performance" /v "DisablediagnosticTracing" /t REG_DWORD /d "1" /f >nul 2>&1 >nul 2>&1
reg add "HKLM\Software\Policies\Microsoft\Windows\WDI\{9c5a40da-b965-4fc3-8781-88dd50a6299d}" /v "ScenarioExecutionEnabled" /t REG_DWORD /d "0" /f >nul 2>&1
schtasks /change /tn "\Microsoft\Windows\Application Experience\StartupAppTask" /Disable >nul 2>&1
schtasks /end /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" >nul 2>&1
schtasks /change /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /Disable >nul 2>&1
schtasks /end /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" >nul 2>&1
schtasks /change /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" /Disable >nul 2>&1
schtasks /end /tn "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem" >nul 2>&1
schtasks /change /tn "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem" /Disable >nul 2>&1
timeout 2 >nul 2>&1
echo - Disabling Autologgers
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\ReadyBoot" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\SpoolerLogger" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\UBPM" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\WiFiSession" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\Circular Kernel Context Logger" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\Diagtrack-Listener" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\LwtNetLog" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\Microsoft-Windows-Rdp-Graphics-RdpIdd-Trace" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\NetCore" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\NtfsLog" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\CloudExperienceHostOobe" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\DefenderAuditLogger" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\RadioMgr" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\RdrLog" /v Start /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\DiagLog" /v Start /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\WdiContextLog" /v Start /t REG_DWORD /d 1 /f >nul 2>&1
  
```


#### Option 4: CPU



##### Changes Made


* **Adjusted CPU Power Settings:** Set `InitialUnparkCount`, disabled event-based processor power states, and C-States.
* **Imported Custom Power Plan:** Applied the “Stix Free Powerplan”.
* **Opened Power Options:** Launches Control Panel’s power settings UI.




***Click to See Batch Code***

```

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v InitialUnparkCount/t REG_DWORD /d 100 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v EventProcessorEnabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "CStates" /t REG_DWORD /d 0 /f >nul 2>&1
powercfg -import "C:\Stix Free\Stix Free Powerplan" >nul 2>&1
start control powercfg.cpl
  
```


#### Option 5: Memory Optimizations



##### Changes Made


* **Memory Optimization Tweaks:** Disabled page file clearing at shutdown, enabled LargeSystemCache, and set NonPagedPool limits.
* **Enabled Physical Address Extension (PAE):** Improves memory addressing support.
* **Performance Enhancements:** Enabled video energy policy and set timer resolutions for better responsiveness.
* **Disabled Memory Compression:** Turned off Windows memory compression via PowerShell.




##### Changes Made


* **Memory Optimization Tweaks:** Disabled page file clearing at shutdown, enabled LargeSystemCache, and set NonPagedPool limits.
* **Enabled Physical Address Extension (PAE):** Improves memory addressing support.
* **Performance Enhancements:** Enabled video energy policy and set timer resolutions for better responsiveness.
* **Disabled Memory Compression:** Turned off Windows memory compression via PowerShell.




***Click to See Batch Code***

```

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "ClearPageFileAtShutdown" /t REG_DWORD /d 0x00000000 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "LargeSystemCache" /t REG_DWORD /d 0x00000001 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "NonPagedPoolQuota" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "NonPagedPoolSize" /t REG_DWORD /d 0x00000000 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PhysicalAddressExtension" /t REG_DWORD /d 0x00000001 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "EnergyDriverPolicyVideo" /t REG_DWORD /d 0x00000001 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "TimerBResolution" /t REG_DWORD /d 0x00000001 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "TimerMinResolution" /t REG_DWORD /d 0x00000001 /f >nul 2>&1
powershell "Disable-MMAgent -MemoryCompression" >nul 2>&1
  
```


#### Option 6: Nvidia GPU



##### Changes Made


* **Telemetry Disabled:** Disabled NVIDIA telemetry and background crash report tasks.
* **Preemption Tweaks:** Disabled various forms of GPU thread/context preemption for lower latency and improved consistency.
* **Power Saving Disabled:** Disabled DisplayPowerSaving features through both registry and NVTweak.
* **Profile Optimization:** Applied a custom NVIDIA Profile Inspector configuration for additional performance tuning.




***Click to See Batch Code***

```

reg add "HKLM\SOFTWARE\NVIDIA Corporation\NvControlPanel2\Client" /v "OptInOrOutPreference" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\Startup" /v "SendTelemetryData" /t REG_DWORD /d "0" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\Startup" /v "SendTelemetryData" /t REG_DWORD /d "0" /f >nul 2>&1
schtasks /change /disable /tn "NvTmRep_CrashReport2_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}" >nul 2>&1
schtasks /change /disable /tn "NvTmRep_CrashReport3_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}" >nul 2>&1
schtasks /change /disable /tn "NvTmRep_CrashReport4_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}" >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "DisablePreemption" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "DisableCudaContextPreemption" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "EnableCEPreemption" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "DisablePreemptionOnS3S4" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "ComputePreemption" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "EnableMidGfxPreemption" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "EnableMidGfxPreemptionVGPU" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "EnableMidBufferPreemptionForHighTdrTimeout" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "EnableMidBufferPreemption" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "EnableAsyncMidBufferPreemption" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm" /v "DisableCudaContextPreemption" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\nvlddmkm\Global\NVTweak" /v "DisplayPowerSaving" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\NVIDIA Corporation\Global\NVTweak" /v "DisplayPowerSaving" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\GraphicsDrivers\Scheduler" /v "EnablePreemption" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0001" /v "RMPowerFeature" /t REG_DWORD /d "4" /f >nul 2>&1
"C:\Stix Free\nvidiaProfileInspector.exe" -import "C:\Stix Free\Stix Free NIP.nip"
  
```


#### Option 7: AMD GPU



##### Changes Made


* **Power Gating Disabled:** Disabled UVD, VCE, DRMDMA, and general power gating for more consistent GPU performance.
* **ULPS Disabled:** Prevents ultra-low power state when multiple GPUs are present, avoiding wake delays.
* **Overlay & Skins Disabled:** Turned off Radeon overlays and skins to reduce UI overhead and background processes.
* **Snapshot & Subscription Settings:** Disabled snapshot and subscription features that can use extra system resources.
* **Other Tweaks:** Adjusted color depth, DMA copy, stutter mode, and block write behaviors for performance tuning.




***Click to See Batch Code***

```

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisableUVDPowerGatingDynamic" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "AllowSnapshot" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisableDrmdmaPowerGating" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "EnableUlps" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "AllowRSOverlay" /t REG_SZ /d "false" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "AutoColorDepthReduction_NA" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "AllowSubscription" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisableUVDPowerGatingDynamic" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisableVCEPowerGating" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisableDMACopy" /t REG_DWORD /d 1 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "AllowSkins" /t REG_SZ /d "false" /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "PP_GPUPowerDownEnabled" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisableBlockWrite" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "StutterMode" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v "DisablePowerGating" /t REG_DWORD /d 1 /f >nul 2>&1
  
```


#### Option 8: Timer Res



##### Changes Made


* **Timer Resolution Registry:** Enabled `GlobalTimerResolutionRequests` to allow custom system-wide timer adjustments.
* **SetTimerResolution Utility:** Downloaded and placed in startup folder for persistent 0.5ms timer resolution.
* **Auto-Launch Setup:** Created a shortcut with required arguments to run silently at boot.




***Click to See Batch Code***

```

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "GlobalTimerResolutionRequests" /t REG_DWORD /d 1 /f >nul 2>&1
set exeUrl=https://www.dropbox.com/scl/fi/uv869o0oo544t1gbgle55/SetTimerResolution.exe?rlkey=edatyvmqbgyh35l45rtiz8m10&st=o72mxwrm&dl=1
set exeFilePath=C:\SetTimerResolution.exe
set startupFolder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set shortcutPath=%startupFolder%\SetTimerResolution - Shortcut.lnk

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%exeUrl%', '%exeFilePath%')"

cscript //nologo "%startupFolder%\CreateShortcut.vbs"
del "%startupFolder%\CreateShortcut.vbs"
  
```


#### Option 9: Network



##### Changes Made


* Added QoS policies for Fortnite, Valorant, CSGO, and Apex Legends to prioritize their network traffic (DSCP value 46).
* Disabled unnecessary network adapter bindings (MS Client, Server, LLDP, IPv6) via PowerShell for network optimization.
* Disabled LMHOSTS and adjusted NDIS DefaultPnPCapabilities for improved network performance and reduced overhead.




***Click to See Batch Code***

```

::QoS For Fortnite
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Version" /t REG_SZ /d "1.0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Application Name" /t REG_SZ /d "FortniteClient-Win64-Shipping.exe" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Protocol" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Local Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Local IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Local IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Remote Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Remote IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Remote IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "DSCP Value" /t REG_DWORD /d 46 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\FortnitePolicy" /v "Throttle Rate" /t REG_DWORD /d -1 /f >nul 2>&1

::QoS For Valorant
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Version" /t REG_SZ /d "1.0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Application Name" /t REG_SZ /d "VALORANT.exe" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Protocol" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Local Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Local IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Local IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Remote Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Remote IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Remote IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "DSCP Value" /t REG_DWORD /d 46 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ValorantPolicy" /v "Throttle Rate" /t REG_DWORD /d -1 /f >nul 2>&1

::QoS For CSGO
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Version" /t REG_SZ /d "1.0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Application Name" /t REG_SZ /d "csgo.exe" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Protocol" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Local Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Local IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Local IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Remote Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Remote IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Remote IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "DSCP Value" /t REG_DWORD /d 46 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\CSGOPolicy" /v "Throttle Rate" /t REG_DWORD /d -1 /f >nul 2>&1

::QoS For Apex
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Version" /t REG_SZ /d "1.0" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Application Name" /t REG_SZ /d "r5apex.exe" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Protocol" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Local Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Local IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Local IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Remote Port" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Remote IP" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Remote IP Prefix Length" /t REG_SZ /d "*" /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "DSCP Value" /t REG_DWORD /d 46 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS\ApexPolicy" /v "Throttle Rate" /t REG_DWORD /d -1 /f >nul 2>&1
PowerShell -Command "Get-NetAdapter | ForEach-Object { Set-NetAdapterBinding -Name $_.Name -ComponentID ms_msclient -Enabled $false }" >nul 2>&1
PowerShell -Command "Get-NetAdapter | ForEach-Object { Set-NetAdapterBinding -Name $_.Name -ComponentID ms_server -Enabled $false }" >nul 2>&1
PowerShell -Command "Get-NetAdapter | ForEach-Object { Set-NetAdapterBinding -Name $_.Name -ComponentID ms_lldp -Enabled $false }" >nul 2>&1
PowerShell -Command "Get-NetAdapter | ForEach-Object { Set-NetAdapterBinding -Name $_.Name -ComponentID ms_tcpip6 -Enabled $false }" >nul 2>&1
reg add "HKLM\System\CurrentControlSet\Services\Tcpip\Parameters" /v EnableLmhosts /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\System\CurrentControlSet\Services\NDIS\Parameters" /v DefaultPnPCapabilities /t REG_DWORD /d 24 /f >nul 2>&1
  
```


#### Option 10: Disk/Storage



##### Changes Made


* Disabled NTFS encryption to improve performance.
* Enabled 8.3 filename creation only on the system volume.
* Set system cache usage to high for better memory performance.
* Disabled Last Access timestamp updates to reduce disk writes.
* Enabled automatic reset of Resource Manager state on C: drive.
* Set Resource Manager consistency on C: drive.
* Configured Resource Manager log to shrink to 10MB on C: drive.




***Click to See Batch Code***

```

fsutil behavior set disableEncryption 1 >nul 2>&1
fsutil 8dot3name set 1 >nul 2>&1
fsutil behavior set memoryusage 2 >nul 2>&1
fsutil behavior set disablelastaccess 1 >nul 2>&1
fsutil resource setautoreset true C:\ >nul 2>&1
fsutil resource setconsistent C:\ >nul 2>&1
fsutil resource setlog shrink 10 C:\ >nul 2>&1
  
```


#### Option 11: Debloat



##### Changes Made


* Deleted contents of user Temp, Windows Temp, Windows Prefetch, and Windows Error Reporting folders.
* Cleared Windows logs.
* Removed various Windows optional packages and apps (QuickAssist, Disney, Bing apps, Microsoft Paint, OneDrive, Skype, Spotify, Teams, and more).
* Uninstalled OneDrive from multiple locations.
* Disabled services: RemoteRegistry, RemoteAccess, WinRM, RmSvc, PrintNotify, and Spooler.
* Disabled scheduled printing tasks (EduPrintProv, PrinterCleanupTask).
* Ran Autoruns utility from "C:\Stix Free\autoruns.exe".




***Click to See Batch Code***

```

set "tempFolder=%LOCALAPPDATA%\Temp"
if exist "%tempFolder%" (
    del /q /s "%tempFolder%\*.*"
    echo Contents of Temp folder have been deleted.
) else (
    echo Temp folder not found.
)

echo Cleaning C:\Windows\Temp folder...
del /q /s "C:\Windows\Temp\*.*"
echo Contents of C:\Windows\Temp folder have been deleted.

echo Cleaning C:\Windows\Prefetch folder...
del /q /s "C:\Windows\Prefetch\*.*"
echo Contents of C:\Windows\Prefetch folder have been deleted.

echo Cleaning Windows Error Reporting files...
del /q /s "%LOCALAPPDATA%\Microsoft\Windows\WER\ReportQueue\*"
echo Windows Error Reporting files have been deleted.

echo Cleaning Windows temporary files...
del /q /s "%windir%\Temp\*"
echo Windows temporary files have been deleted.
)
echo Windows logs have been cleared.
Powershell.exe -command "Get-WindowsPackage -Online | Where PackageName -like *Hello-Face* | Remove-WindowsPackage -Online -NoRestart
Powershell.exe -command "Get-WindowsPackage -Online | Where PackageName -like *QuickAssist* | Remove-WindowsPackage -Online -NoRestart
Powershell.exe -command "Get-AppxPackage -allusers Disney.37853FC22B2CE | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.BingNews | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.BingWeather | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.GetHelp | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.Getstarted | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.MSPaint | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.Microsoft3DViewer | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.MicrosoftOfficeHub | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.MicrosoftSolitaireCollection | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.MicrosoftStickyNotes | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.Office.OneNote | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.OneDriveSync | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.People | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.PowerAutomateDesktop | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.SkypeApp | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.Todos | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.Wallet | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.WindowsAlarms | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.WindowsCamera | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.WindowsFeedbackHub | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.WindowsMaps | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.WindowsSoundRecorder | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.YourPhone | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.ZuneMusic | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.ZuneVideo | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers MicrosoftCorporationII.QuickAssist | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers MicrosoftTeams | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers MicrosoftWindows.Client.WebExperience | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers SpotifyAB.SpotifyMusic | Remove-AppxPackage
Powershell.exe -command "Get-AppxPackage -allusers Microsoft.WindowsCommunicationsApps | Remove-AppxPackage

C:\Windows\SysWOW64\OneDriveSetup.exe -uninstall
C:\Users\Administrator\AppData\Local\Microsoft\OneDrive\22.012.0117.0003\OneDriveSetup.exe /uninstall
C:\Users\Administrator\AppData\Local\Microsoft\OneDrive\23.194.0917.0001\OneDriveSetup.exe /uninstall
sc config RemoteRegistry start= disabled >nul 2>&1
sc config RemoteAccess start= disabled >nul 2>&1
sc config WinRM start= disabled >nul 2>&1
sc config RmSvc start= disabled >nul 2>&1
sc config PrintNotify start= disabled >nul 2>&1
sc config Spooler start= disabled >nul 2>&1
schtasks /Change /TN "Microsoft\Windows\Printing\EduPrintProv" /Disable >nul 2>&1
schtasks /Change /TN "Microsoft\Windows\Printing\PrinterCleanupTask" /Disable >nul 2>&1
"C:\Stix Free\autoruns.exe"
  
```


### Where can you try the utility?



 At the time of this article's creation, I have full faith in the legitimacy and product safety of Stix and his free utility from malicious code. But as with anyone, I must urge you to do your own research to ensure the current state of safety for your own system. To try this software for yourself, you can find it within his 
 [Discord Server](https://discord.gg/UXjTVqJHB3) found under the channel #free-tweaks.



##### End of Article, feel free to reach out to me if you notice any errors or typos and I will gladly adjust. Retr0