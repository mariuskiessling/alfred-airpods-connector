#!/usr/bin/env python3

from __future__ import print_function
import os
import re

STATUS_NOT_FOUND = "not found"
STATUS_CONNECTED = "connected"
STATUS_DISCONNECTED = "disconnected"
STATUS_UNCONFIGURED = "unconfigured"

def get_connection_status(assume_disconnected=False):
    mac = os.getenv('AIRPODS_MAC')

    # New technique for extracting MAC during config uses dashes instead of colons, but this system_profiler output uses colons, so fix that here
    mac = mac.replace("-", ":").upper()

    paired_bt_devices_header = "Paired Bluetooth Devices:"
    paired_bt_header_len = len(paired_bt_devices_header)

    devices = os.popen('/bin/bash -c "system_profiler SPBluetoothDataType"').read()
    start_search_index = devices.find("Paired Bluetooth Devices:") + paired_bt_header_len + 1
    paired_devices = devices[start_search_index:]

    re_mac = re.escape(mac)
    mac_match_re = rf"Address: ({re_mac})"
    mac_found = len(re.findall(mac_match_re, paired_devices)) > 0

    status = STATUS_DISCONNECTED if assume_disconnected else STATUS_NOT_FOUND

    if mac_found:
        connected_regex = rf"Address: ({re_mac})\n\s*(Connected:) (Yes|No)"
        status_match_iter = re.finditer(connected_regex, paired_devices, re.MULTILINE)

        # When paired but not connected, we don't see "Connected: No" like I think we used to in older versions of 
        # macOS (based on how the old logic here was written)
        # Since we got into this mac_found block, the new "fall back" status becomes "disconnected" instead of "not found"
        status = STATUS_DISCONNECTED
        
        for match_num, match in enumerate(status_match_iter):
            # group(0) is the full match, index 1 is the MAC, 2 is "Connected" (if present), 3 is "Yes" or "No" (if present)
            # Note that if we got into this 'if', then groups 2 and 3 should be present
            if len(match.groups()) > 2 and match.group() != '' and match.group(1) == mac:
                if match.group(3) == "Yes":
                    status = STATUS_CONNECTED
                else:
                    status = STATUS_DISCONNECTED

    return status

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

def get_configured_mac(format_upper_with_colons=False):
    # New technique for extracting MAC during config uses dashes instead of colons, 
    # but system_profiler output uses colons, so optionally format the MAC to adhere
    if format_upper_with_colons:
        mac = os.getenv('AIRPODS_MAC')
        if is_valid_mac(mac):
            return mac.replace("-", ":").upper()
        else:
            return None
    else:
        return os.getenv('AIRPODS_MAC')

def is_invalid_mac_configured():
    mac = get_configured_mac()
    return not is_valid_mac(mac)

