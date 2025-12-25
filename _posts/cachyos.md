---
layout: post
title: "How to set secure boot for your cachyos installation"
date: 2025-06-04
permalink: /cachy/
---


    Enter BIOS and ensure secure boot is off (set to Custom OS on my ASUS board).

    Delete system keys in BIOS (enter Secure Boot setup mode). Save BIOS settings and exit.

    Boot into CachyOS.

    sudo pacman -S sbctl

    sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=cachyos --modules="tpm" --disable-shim-lock

    sudo sbctl create-keys

    sudo sbctl enroll-keys --microsoft

    sudo sbctl-batch-sign

    Reboot and re-enable secure boot in BIOS (for my ASUS board change OS to "Windows UEFI mode")

    All should be working now. Can confirm from Linux cli with sudo sbctl status and should see Secure-Boot as Enabled.
