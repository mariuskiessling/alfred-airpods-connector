#!/usr/bin/env python3

from __future__ import print_function
import os
import re

STATUS_NOT_FOUND = "not found"
STATUS_CONNECTED = "connected"
STATUS_DISCONNECTED = "disconnected"
STATUS_UNCONFIGURED = "unconfigured"

def get_connection_status(assume_disconnected=False):
    mac = get_configured_mac()
    
    if not is_valid_mac(mac):
        return STATUS_UNCONFIGURED

    initial_status = os.popen('/bin/bash -c "/opt/homebrew/bin/BluetoothConnector --status "' + mac).read()

    if 'Disconnected' in initial_status:
        return STATUS_DISCONNECTED
    elif 'Connected' in initial_status:
        return STATUS_CONNECTED
    else:
        # Status would be "Not paired to device"
        return STATUS_NOT_FOUND
    

def is_failed_status(status):
    return status != STATUS_CONNECTED and status != STATUS_DISCONNECTED

def create_menu_json(title, subtitle, arg, icon_path):
    menu = {
        "items": [
            {
                "uid": 0,
                "type": "default",
                "title": title,
                "subtitle": subtitle,
                "arg": arg,
                "icon": {
                    "path": icon_path
                }
            }
            ]
        }
    return menu

def is_valid_mac(mac):
    return mac != None and mac != ""

def get_configured_mac():
    return os.getenv('AIRPODS_MAC')

def is_invalid_mac_configured():
    mac = get_configured_mac()
    return not is_valid_mac(mac)

