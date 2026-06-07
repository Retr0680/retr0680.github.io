---
layout: post
title: "How to Burn Bootloader on your Arduino Pro Micro"
date: 2026-06-08
permalink: /pro_micro/
categories: [diy]
teaser: "How to burn a bootloader onto a bricked Arduino Pro Micro using an Arduino Uno as an ISP programmer."
---
Step by step guide on how to flash bootloader on your arduino pro micro.
<!--more-->

# Pin Diagram

ARDUINO UNO – ARDUINO PRO MICRO CONNECTIONS
Connect the Arduino Uno 5V pin to Arduino Pro Micro VCC pin (red wire)
Connect the Arduino Uno GND pin to Arduino Pro Micro GND pin (black wire)
Connect the Arduino Uno Pin 13 to Arduino Pro Micro Pin 15 (blue wire)
Connect the Arduino Uno Pin 12 to Arduino Pro Micro Pin 14 (green wire)
Connect the Arduino Uno Pin 11 to Arduino Pro Micro Pin 16 (yellow wire)
Connect the Arduino Uno Pin 10 to Arduino Pro Micro Pin RST (white wire)Image below shows how I connected the two boards based from the connections above:

![wiring](/images/pro_micro/1.png)
![wiring1](/images/pro_micro/2.png)
![wiring2](/images/pro_micro/3.png)

# LOADING THE ArduinoISP SKETCH TO ARDUINO UNO

Open the Arduino IDE. Then go to File > Examples > ArduinoISP > ArduinoISP. Please see screenshot below:

![ide](/images/pro_micro/4.png)

Now, plug the Arduino Uno to the computer, select the port where the Arduino Uno is connected to, and upload the sketch. Screenshot below shows that the selected board is Arduino/Genuino Uno and the port (yours could be different):

![idk](/images/pro_micro/5.png)

Now, upload the sketch.

BOOTLOADER BURNING
Now that the Arduino Uno is programmed to be an ISP (ISP stand for Is-System Programmer), we are now ready to burn the bootloader to the Arduino Pro Micro.From Tools > Board, choose Arduino Leonardo:

![idk1](/images/pro_micro/6.png)

Then we select Arduino As ISP from Tools > Programmer:

![alt text](/images/pro_micro/image.png)

The last step is to burn the bootloader, by going to Tools and clicking Burn Bootloader. Wait for a minute, until the process is done:

![alt text](/images/pro_micro/image-1.png)

While the process is burning the bootloader is taking place, you should see the Arduino Led, the TX Led  and the RX Led blinking. Once the process is done, a message similar to the screenshot below is shown:

![alt text](/images/pro_micro/image-2.png)

Now that the process of burning the bootloader is done, try connecting the Arduino Pro Micro to the computer and upload the Blink sketch (by the way, there isn’t any built-in LED on my Arduino Pro Micro, but I used Pin 17 to blink the RX Led).

This article serves as my documentation in case I forget what I’ve done to “revive” my Arduino Pro Micro. I haven’t tried this method in my other boards, as all of them are still detectable.

##### End of Article, feel free to reach out to me if you notice any errors or typos and I will gladly adjust. Retr0