#!/usr/bin/env python3

from __future__ import print_function
from bluetooth_status_parser_utils import get_connection_status

print(get_connection_status(True), end='')