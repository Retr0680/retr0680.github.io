---
layout: post
title: "Fix integrity and root detection"
date: 2025-06-04
permalink: /play_integrity/
---
Step by step guide on how to fix play integrity and root detection.
<!--more-->

# FIXING INTEGRITY

### Installing required modules:
* [ReZygisk](https://github.com/PerformanC/ReZygisk/releases)
* [Play Integrity Fix Fork](https://github.com/KOWX712/PlayIntegrityFix/releases)
* [Tricky Store](https://github.com/beakthoven/TrickyStoreOSS/releases)
* [Tricky Store Add-On](https://github.com/KOWX712/Tricky-Addon-Update-Target-List/releases)

### Configuring PlayIntegrityFix:
* Open Modules tab in KernelSU/Magisk manager.
* On the PIF module, tap Fetch pif.json to retrieve the config file.

Check integrity now, if you already have atleast 2 green ticks aka device integrity, you can skip the below "Configuring TrickyStore" steps.

### Configuring TrickyStore:

If your integrity is not fixed using above mentioned PIF Module follow this.

* Open Modules tab in KernelSU/Magisk manager.
* Find Tricky Store in the modules list.
* Tap on Open/Action button.
* Click on menu

```
1. Select All > Save
2. Deselect Unecessary > Save
3. Set Valid Keybox
4. Set Security Patch > get security patch date.
```

* Done ✅

If you are using any custom ROMs, make sure to disable any integrity fix spoof that comes with the ROM (if any).

Your integrity should be fixed now. You can check integrity using [this app](https://play.google.com/store/apps/details?id=gr.nikolasspyr.integritycheck).

---