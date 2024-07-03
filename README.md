# SleepObserver
Internet of Things
By: Marcel Molnár, mm224yx

## Description
The purpose of this project is to “monitor” your sleep, with the use of a sound sensor and a tilt/vibration sensor we are able to collect data on if and how many times you make noise and also move during your sleep.
The project took roughly 20h of work to get to where it is now but it can still be improved.

## Objective
### Why did I choose this project?
During a conversation with one of my siblings I had mentioned to them that they snored while sleeping and they were very adamant of them not snoring or making any noise while they sleep. So from the inspiration of some phone apps I decided that this would be a fun way to prove to them that they do indeed make noise while sleeping.

### What purpose does it serve? / What insight will it give?
Well it allows for the user to see whether they move and make noise during certain times, which can indeed be used for monitoring sleep and then together with some analysis you could potentially measure sleep quality and or even use it to track pet behavior while away from home. Simply good for gathering data in regards to movement and sound but I focused on the sleep aspect.

## Materials
| Part | Description |
| ---- | ----------- |
| Raspberry pico W | The micro controller itself, used to store and run the code. |
| CZN-15E | A sound sensor with an adjustable sensitivity. Outputs a 0 or 1 depending on if it picks up any sounds. |
| SW-520D | A tilt sensor. Outputs a 0 or 1 depending on if the 2 metal balls inside the cylinder are touching the base of the cylinder or not. |
| Breadboard | A board with several connection points allowing for simple wiring. |
| Connection cable x 8 | A thin wire with exposed ends which allows you to stick them into the breadboard to establish connection between two points. |
| USB to Micro USB | A cable which allows you to connect the micro controller to your PC to be able to send over code or whatever other files you may need. |

All these parts came in a bundle of a lot of other items I purchased from this [link](https://www.elecrow.com/raspberry-pi-pico-advanced-kit-with-pico-board-32-modules-and-32-detailed-projects-lessons.html) which cost me 38 USD which is roughly 403 SEK.

## Setup
### IDE:
- Thonny

### Workflow
All the work was done via Thonny directly, the code was written and tested with the Pico W connected to the PC and then saved directly to the device itself.

### Steps:
1. Install Thonny IDE
2. Flash the Pico W
    1. Connect the Pico W to your PC using the USB to Micro USB cable.
    2. Open the Thonny IDE and select the Pico W using the button on the bottom left of the program.
3. Download pyRTOS library from [link](https://github.com/Rybec/pyRTOS).
4. Upload the downloaded file to the Pico W using Thonny.

## Assembly
The assembly of the project is very simple as it requires no resistors or any complicated extra connections, each sensor has 3 pins; a OUT pin that sends data, a GND pin that is connected to a GND pin on the Pico W and lastly a VCC pin which is connected to the 3.3V pin on the Pico W.

![Circuit diagram](https://cdn.discordapp.com/attachments/567450731372740641/1257994237799305287/image.png?ex=66866dee&is=66851c6e&hm=1105323c56d521ef7b57fc5ecb75c648b433039419e588ae21960fdaaf3b3c59&)

The module with the gold looking cylinder on top is the SW-520D but the one I used does not have a sensitivity adjuster (little blue square with screw).

## Platform
Everything is simply run on the Pico W that sends the data to a public free MQTT broker called HiveMQ, I then connect to that via MQTTX which is a free software that I use to somewhat neatly display my data.

## Code
The code is realtively simple, but to make it a little more advanced I used pyRTOS which allows for the 2 sensors to send data practically at the same time. [The code itself](SleepObserver.py).

## Transmitting Data
The data is sent only when sound and/or movement is detected, and with the use of RTOS I was able to make it so that both data of the sound and movement sensor can be sent at the same time and also they measure virtually at the same time.
I used Wifi to then send my data via MQTT.

## Presenting Data
The data is presented in numerical value with a timestamp every time the data is sent. The data is also categorized so that you can view all data, just sound data or just movement data, this is done using different topics when publishing the data. The data is saved on MQTTX, and the amount of instances detected get reset every time the device itself is reset.

![Image showing the collective data (Morse_Data)](https://cdn.discordapp.com/attachments/567450731372740641/1257996160912723968/image.png?ex=66866fb9&is=66851e39&hm=69af907df2e61e30144a7f17eb45e6ed951c69628ed4506d56d805fa5ad70632&)

*Image showing the collective data (Morse_Data)*


![Image showing only sound data (Morse_Sound)](https://cdn.discordapp.com/attachments/567450731372740641/1257996289132597258/image.png?ex=66866fd7&is=66851e57&hm=dd63061b58e07e09f91d08c4f996a8b21e2df7f53aa76e3b31713fb267878550&)

*Image showing only sound data (Morse_Sound)*


![Image showing only movement data (Morse_Move)](https://cdn.discordapp.com/attachments/567450731372740641/1257996289551896637/image.png?ex=66866fd7&is=66851e57&hm=0b096562e927710ab5763dd99bbaba5a2d14483f16e6a7b7f337158748e9c47f&)

*Image showing only movement data (Morse_Move)*



## Summary
To start off; I made a huge mistake when reading the deadline. I thought I had until the 30th of JULY not JUNE. So my time management was terrible and I could not complete everything I wanted to complete, especially the graphing of the data.

If I were to do this again I would most definitely make it so that the data can be graphed through time to have a somewhat visual representation of the movements and sounds made during the time period specified. If I had access to a 3D printer then I would have also liked to make some sort of shell for it to keep everything protected while in use. I would have connected the battery pack that came in the bundle had I had a soldering pen. Lastly maybe even add a light sensor to see potential correlation between light level and “awakeness”.

All in all I believe the project turned out to be a very good prototype and very much prepared for upgrades and other additions, I believe the code to be simple enough to make quick and easy additions or even changes and the hardware versatile enough to also make additions or even alterations.

![Image of final product](https://cdn.discordapp.com/attachments/567450731372740641/1256956012171366481/PXL_20240630_125404775.jpg?ex=6685f2c2&is=6684a142&hm=fe9ee7054a2bbf3abe21f4044d71b54338a4314d0a7ba47b9408828e24effabf&)

*Image of final product*

