# DT-Minecraft Digital Twin

A "fun" ongoing project with potentially useful applications: using DT's virtual sensors to observe the real world and update objects in a virtual world accordingly.

## Prerequisites

- a Minecraft server. My server runs on a Raspberry Pi 4, and I used [this very helpful guide](https://lemire.me/blog/2016/04/02/setting-up-a-robust-minecraft-server-on-a-raspberry-pi/) to set it up. You also need the [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice) server plugin.
- some DT sensors and a DT studio project
- python

## Example

My front door has a DT proximity sensor attached to it. Next to the front door is a DT touch sensor "doorbell".

We've built a model of our house in Minecraft, and we want the front door connected to the real front door, so that when the front door opens or shuts, so does the Minecraft "twin". Also, when somebody triggers the touch sensor, we should hear a bell ringing in Minecraft...

## Setup

You can run the integration directly on the Minecraft server, or on a different PC. It uses two key python packages:

- DT's excellent [python API client](https://developer.disruptive-technologies.com/api/libraries/python/index.html), `disruptive`. We use the streaming API to receive event data from the sensors.
- the [`mcpi`](https://github.com/martinohanlon/mcpi) package, which communicates with the minecraft server via the RaspberryJuice plugin. The package has a companion book *Adventures in Minecraft* - see [here](https://www.stuffaboutcode.com/p/adventures-in-minecraft.html) for more information

First install the python dependencies
```
pip install -r requirements.txt
```

Then set up an environment file (e.g. `.env`) with all the configuration and secrets in it:

```sh
# DT credentials
DT_PROJECT=<your-project-id>
DT_SVC_KEY=<your-service-account-key>
DT_SVC_SECRET=<your-service-account-secret>
DT_SVC_EMAIL=<your-service-account-key>
# MC server
MC_SERVER=localhost
MC_PORT=4711
FRONT_DOOR_COORDS="(49,64,62)" # change as necessary
```




