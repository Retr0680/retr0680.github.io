---
layout: post
title: "How to use NTFS Drive on Linux"
date: 2026-08-28
permalink: /lowntfs/
categories: [linux]
teaser: "Steps on how to use your NTFS drive on Linux."
---

NOT OFFICIAL - USING NTFS IS NOT RECOMMENDED

<!--more-->

# Configuring and Automounting the NTFS Partition

## Create a Mount Point

Create a mount point for the NTFS game disk:
```
$ sudo mkdir /media/gamedisk
```

Find the User ID, Group ID, attached disk partition, and the UUID using the following commands:

**User ID**
```
$ id -u
```
**Group ID**
```
$ id -g
```
By default, both should be `1000`
**Attached Disk Partition**
```
$ sudo fdisk -l
```
It should be labeled similar to `/dev/sda2`
The trailing letter and number (a2) will depend on how many disks are attached.
**UUID**
```
$ sudo blkid
```
Find the line where the first column matches the label of the `fdisk` command.
For example, `/dev/sda2` would match this line:
```
/dev/sda2: UUID="38CE9483CE943AD8" TYPE="ntfs"
```
Copy the UUID.

## Editing fstab
You've made it this far. Just wanted to remind you again that using NTFS is not recommended.
Edit the fstab file to mount the partition:
```
$ sudo nano /etc/fstab
```
At the bottom of the file, add the following line (changing UUID, uid, and gid where needed):
```
UUID=38CE9483CE943AD8 /media/gamedisk ntfs uid=1000,gid=1000,rw,user,exec,umask=000 0 0
```


On Ubuntu, as long as `ntfs-3g` is installed using `ntfs` as the filesystem type will work
Reboot the computer for the changes to take effect:
```
$ sudo reboot
```
**If the partition is mounted as read-only after reboot**
If Windows is installed on the NTFS partition, the Windows Fast Startup feature can cause the mount command to fail. To prevent that, consider to disable it. Example tutorial: [PassFab: Disable Fast Startup](https://www.passfab.com/windows-10/disable-fast-boot-windows-10.html#way3)

## Preventing NTFS Read Errors
**THERE HAS BEEN A REPORT THAT THIS MAY CAUSE DATA LOSS**
Due to the nature of NTFS, creating [files/folders with names that are invalid on Windows](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file#naming-conventions) will cause disk errors (leading to games that don't launch). The most common issue is a `:` (colon) character in filenames that Proton creates on the NTFS disk.
Fixing this is pretty simple: create the `/compatdata` folder on the mounted NTFS disk as a symlink that points to a folder on a Linux partition.
Creating the symlink:
```
$ mkdir -p ~/.steam/steam/steamapps/compatdata
$ ln -s ~/.steam/steam/steamapps/compatdata /media/gamedisk/Steam/steamapps/
```
If the `/compatdata` folder already exists on the mounted disk BEFORE the symlink, DELETE IT!

## Turning off case-sensitivity in file names
Sometimes case-sensitivity can be an issue and lead to files not being found, because their names differ in case from what is expected. In such cases, mounting the NTFS partition with `lowntfs-3g` may solve the problem (source: https://serverfault.com/questions/901855/ntfs-3g-ignore-case). To do that, edit the entry in `/etc/fstab` as follows:
```
UUID=38CE9483CE943AD8 /media/gamedisk lowntfs-3g uid=1000,gid=1000,rw,user,exec,umask=000 0 0
```
And then reboot.