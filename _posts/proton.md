---
layout: post
title: "Useful Proton commands"
date: 2026-08-11
permalink: /proton_commands/
categories: [linux]
teaser: "List of useful commands for proton which work flawlessly with my games on Linux."
---

Personal commands notes for running games via Proton on Linux. All entries tested on my system — your mileage may vary.

<!--more-->

## Spoof DS4
```PROTON_SONY_DUALSENSE_AS_DUALSHOCK4=1 %command%```

## XInput Convert
```PROTON_SONY_HIDRAW_XINPUT=1 %command%```

## Steam Input Fallback
```
PROTON_SONY_HIDRAW_XINPUT=1 \
PROTON_STEAMINPUT_XINPUT_FALLBACK=1 \
%command%
```