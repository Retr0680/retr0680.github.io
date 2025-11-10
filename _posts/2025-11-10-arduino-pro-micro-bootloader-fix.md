---
layout: post
title: "How to Burn Bootloader on your Arduino Pro Micro"
date: 2025-11-10
permalink: /pro_micro/
---
Step by step guide on how to flash bootloader on your arduino pro micro.
<!--more-->

# Pin Diagram

The wiring diagram is very simple, just follow the table below.

![wiring](/images/pro_micro/pin.png)

# Time to Burn!!

Now that you're done with the wiring it is time to flash the bootloader.
But before we begin you first have to prepare your arduino uno as programmer, for that open your `arduino ide` click on `File < Examples < ArduinoISP`, Once the ISP code is opened go ahead and upload the sketch on your board.

![ArduinoISP](/images/pro_micro/1.png)

![ArduinoISP](/images/pro_micro/isp.png)

Once you're done with uploading the sketch go ahead and select your board and flash the bootloader.

![ToolsBoardArduinoLeonardo](/images/pro_micro/2.png)

![ToolsProgrammerArduinoAsISP](/images/pro_micro/3.png)

![BurnBootloader](/images/pro_micro/4.png)

Now that you've flashed your board now disconnect the board and power it up. if the board led turns on, congratulations on fixing your bricked Arduino Pro Micro.

##### End of Article, feel free to reach out to me if you notice any errors or typos and I will gladly adjust. Retr0