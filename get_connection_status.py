#!/usr/bin/env python

import os
import re
import json
import sys

mac = os.getenv('AIRPODS_MAC')

if mac == None or mac == "":
    menu = {
        "items": [
            {
                "uid": 0,
                "type": "default",
                "title": "Your setup isn't completet yet.",
                "subtitle": "Configure your AirPods device to get started.",
                "arg": "unconfigured",
                "icon": {
                    "path": "unconfigured.png"
                }
            }
        ]
    }
    print(json.dumps(menu))
    sys.exit()

devices = os.popen('/bin/bash -c "system_profiler SPBluetoothDataType"').read()

connectedRegex = r"(Address: " + mac.upper() + "(.*\n)*?.*Connected: )(Yes|No)"
statusMatch = re.finditer(connectedRegex, devices, re.MULTILINE)

status = ""

for matchNum, match in enumerate(statusMatch):
    if match.group() != '':
        if match.group(3) == "Yes":
            status = "connected"
        else:
            status = "disconnected"

menu = {
    "items": [
        {
            "uid": 0,
            "type": "default",
            "title": "Disconnect AirPods" if status == "connected" else "Connect AirPods",
            "subtitle": "Status: " + status,
            "arg": status,
            "icon": {
                "path": "icon.png" if status == "disconnected" else "disconnect.png"
            }
        }
    ]
}

print(json.dumps(menu))
