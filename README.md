# [Alfred AirPods Connector](https://www.packal.org/workflow/airpods-connector)

> This [Alfred v4](https://www.alfredapp.com/) workflow helps you to quickly connect to your AirPods using the Alfred search or a hotkey.

###### See it in action
![Workflow demo](https://github.com/mariuskiessling/alfred-airpods-connector/raw/master/demo.gif "Workflow demo")

## Installation
1) Install the `BluetoothConnector` utility using
   ```
   brew install bluetoothconnector
   ```
   Make sure to have [`brew`](https://brew.sh/) installed. This will install the latest version of BluetoothConnector. Unfortunately BluetoothConnector is not @-versioned. Thus, make sure that brew installs version `2.0.0+` of BluetoothConnector or upgrade using
   ```
   brew upgrade bluetoothconnector
   ```
   in case you update from an older version of this workflow.

2) Download the workflow file [↗ here](https://github.com/packal/repository/raw/master/de.mariuskiessling.alfred-airpods-connector/airpods_connector.alfredworkflow) and import it.

It is recommended to have `HOMEBREW_PREFIX` defined, for M1 Macs this will be `/opt/homebrew/`.

###### In case of errors
If you encounter any errors running the workflow double-check the steps above and test whether you have Python 3.x installed on your system (Python 2.x is no longer compatible with this workflow).

## Usage
On your first run, you have to select the bluetooth device that are your AirPods. Once you have done this you can use the **`airp`** keyword to connect / disconnect your AirPods. Whenever you want to change the device you can use the **`airp config`** keyword to select a new bluetooth device.

By default, this workflow also offers the ability to trigger a connect / disconnect action using a hotkey. The default hotkey is **`⌃ Ctrl + ⇧ Shift + ⌘ Cmd + A`**.

## Acknowledgments 
* Big thanks to Daniel Schäfer ([@JohnAZoidberg](https://github.com/JohnAZoidberg)) for helping design the RegEx used in this workflow.
