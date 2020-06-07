#!/usr/bin/env python

import os
import re
import json

TRUE, pout = os.popen4('/bin/bash -c /usr/local/bin/BluetoothConnector')
devicesRaw = pout.read()

deviceMacs = []
deviceNames = []
airPodsPosition = -1

macsRegex = r"^([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})"
macsMatches = re.finditer(macsRegex, devicesRaw, re.MULTILINE)

for matchNum, match in enumerate(macsMatches, start=1):
    if match.group() != '':
        deviceMacs.append(match.group())

namesRegex = r"(?<=\s-\s).*"
namesMatches = re.finditer(namesRegex, devicesRaw, re.MULTILINE)

for matchNum, match in enumerate(namesMatches, start=1):
    if match.group() != '':
        deviceNames.append(match.group())
        # Save AirPods device position
        if "AirPods" in match.group():
            airPodsPosition = matchNum

# Remove AirPods and prepend them
if airPodsPosition != -1:
    deviceMacs.insert(0, deviceMacs.pop(airPodsPosition - 1))
    deviceNames.insert(0, deviceNames.pop(airPodsPosition - 1))

menu = {
    "items": [
    ]
}

for i, mac in enumerate(deviceMacs):
    item = {
        "type": "default",
        "title": deviceNames[i],
        "subtitle": "MAC: " + mac + ("  (These probably are your AirPods!)" if "AirPods" in deviceNames[i] else ""),
        "arg": mac,
        "icon": {
            "path": "icon.png"
        }
    }
    menu["items"].append(item)

print(json.dumps(menu))
