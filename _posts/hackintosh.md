

So, in this guide, I am going to show how you can make a full offline installer for macOS, on your Windows PC. This can come in handy for the people wanting to install macOS on a device where internet connection is still a problem.

(Disclaimer: I am not a developer of any of the tools used in this guide, this is just how I got a successful full installer USB. I thought it could come in handy for the people wanting to get this too, so I wanted to share it.)

So first of all, go here and make sure you have the prerequisites ([gibMacOS](https://github.com/corpnewt/gibMacOS), [MakeInstallmacOS](https://github.com/doesprintfwork/MakeInstallmacOS), [Python](https://www.python.org/downloads/), [TransMac](https://www.acutesystems.com/scrtm.htm), [Paragon Hard Disk Manager](https://www.paragon-software.com/free/pm-express/#), [Boot Disk Utility](http://cvad-mac.narod.ru/index/bootdiskutility_exe/0-5) and [7-zip](https://www.7-zip.org/). You don't need the Clover Cloud Editor, because we will be converting the installer to OpenCore😊. And I highly recommend a 16GB USB 3.0 as a minimum. Higher is better of course.

The guide can be a little confusing, I had a hard time finding my way through the guiding files, as they are all apart from each other. They do link to each other tho.

    So you start the guide [here](https://github.com/doesprintfwork/All-in-one-Vanilla-AMD-Hackintosh-Guide/blob/master/download/network-part-1.md). So run gibMacOS and enter the number of the macOS version you want. You don't need to toggle Recovery Only, as we want the full installer. Once it's downloaded, you can enter the [next step](https://github.com/doesprintfwork/All-in-one-Vanilla-AMD-Hackintosh-Guide/blob/master/offline-installer-guide/offline-part-3/windows.md).

    So now you want to put the PackAppWin.py (from MakeInstallmacOS) into the downloaded macOS Installer files folder (i.e.: gibMacOS/macOS Downloads/publicrelease/xxx-xxxxx blah blah blah) Open it, and enter P. Now a new folder called SharedSupport will be created. Once that is finished, you can go to the next step.

    Now you will be making the actual installer. Plugin your USB, and open the BDU tool (Boot Disk Utility) you have installed. The guide tells you to "Go to Options > Configuration and press Check Now." You don't have to do that, as we are not going to use Clover in the end. So click on your USB in the list and press Format. The app will start to format your disk into 2 partition: 1. CLOVER (the EFI partition. BDU will auto-install Clover to it) 2. HFS+ (for your Installer Resources). Don't worry, we will get rid of Clover later... Once this is done, don't exit the program just yet.

    In BDU, click Tools > Extract HFS (HFS+) from DMG-file. Now choose the BaseSystem.dmg file that is in the downloaded folder. (Don't choose the one in the SharedSupport folder) Choose Desktop as the destination folder, as this is easy to find. It will now start to extract the 4.hfs file from BaseSystem.dmg. For me, this happened pretty quickly. Once it is finished, the command prompt window will automatically close. Press the "plus" button next to the USB and choose Part 2. Press Restore and choose the extracted 4.hfs file. BDU will start to restore the files to your USB. This also went pretty quick for me.

    Open Paragon Disk Manager and click on the second partition of your USB. You may see grabbers on the partition. If so, drag the right edge all the way to the right and press Apply on the pop-up window. Otherwise, choose Move or Resize on the left. Set Space after partition to 0 and press OK, after that press Apply. This makes sure you have enough space on your partition for the full installer. You don't have to exit the tool just yet, we will need it to remove the Clover partition later.

    Now run TransMac as Administrator. Click on your USB and go to macOS Base System (or OS X Base System)/Install macOS xxx.app/Contents Drag and drop the prepared SharedSupport folder here. This may take some time. After that, you don't need to proceed to the next part of the guide, as the guide will just show you how to configure Clover. And we don't want that... 😅

    Okay, so now you have a USB, with Clover and macOS partitions on it. But we want to get rid of Clover and use OpenCore instead. So back to the Paragon Disk Manager, click on the first partition of the USB (most likely named CLOVER, or EFI) and select Remove Partition on the left, click Apply. Now you want to make a new partition out of the "Unallocated Space", so select the empty space and select Create Volume. Show the advanced options, and make sure you set the File System to Fat32, and name the partition "EFI". Now that's done, the EFI partition should show up in Explorer.

    Now you can copy your already made EFI folder from OpenCore to the EFI partition. Or you could start building the EFI folder from scratch using the [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/).

That's it! If everything went well, you now have a full macOS installer, that doesn't require internet to install it!

Good luck hackintoshing!
