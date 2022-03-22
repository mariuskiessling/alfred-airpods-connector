#!/usr/bin/env python3

import os
import re
import json
import sys
from bluetooth_status_parser_utils import get_connection_status
from bluetooth_status_parser_utils import is_failed_status
from bluetooth_status_parser_utils import create_menu_json
from bluetooth_status_parser_utils import get_configured_mac
from bluetooth_status_parser_utils import is_invalid_mac_configured
from bluetooth_status_parser_utils import STATUS_NOT_FOUND
from bluetooth_status_parser_utils import STATUS_CONNECTED
from bluetooth_status_parser_utils import STATUS_DISCONNECTED
from bluetooth_status_parser_utils import STATUS_UNCONFIGURED

ICON_PATH = "icon.png"
DISCONNECT_ICON_PATH = "disconnect.png" # used when connected
UNCONFIGURED_ICON_PATH = "unconfigured.png" 
ERROR_ICON_PATH = "error.png" 

if is_invalid_mac_configured():
    # This is an exit strategy to avoid showing connection options when a MAC is not configured
    # We can't show an error status here because this is triggered for the initial config too
    sys.exit()

mac = get_configured_mac()

status = get_connection_status(False)

title = "Cancel (AirPods not found)"
icon_path = ERROR_ICON_PATH

if status == STATUS_DISCONNECTED:
    title = "Connect AirPods"
    icon_path = ICON_PATH
elif status == STATUS_CONNECTED:
    title = "Disconnect AirPods"
    icon_path = DISCONNECT_ICON_PATH

subtitle = "Status: " + status
if status == STATUS_NOT_FOUND:
    subtitle = "Cancel/exit without taking action. (MAC = " + str(mac) + ")" 

menu = create_menu_json(title, subtitle, status, icon_path)

print(json.dumps(menu))

if is_failed_status(status):
    # Prevent processing output for next stage since it failed
    sys.exit()


