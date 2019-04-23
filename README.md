# Alfred AirPods Connector

> This [Alfred](https://www.alfredapp.com/) workflow helps you to quickly connect to your AirPods using the Alfred search or a hotkey.

###### See it in action
![Workflow demo](https://github.com/mariuskiessling/alfred-airpods-connector/raw/master/demo.gif "Workflow demo")

## Installation
1) Install the `BluetoothConnector` utility using
   ```
   brew install bluetoothconnector
   ```
   Make sure to have [`brew`](https://brew.sh/) installed.

2) Download the workflow file [here]() and import it.

###### In case of errors
If you encounter any errors running the workflow double-check the steps above and test wether you have Python installed on your system (version 2.7 and version 3.* are compatible with this workflow).

## Usage
On your first run, you have to select the bluetooth device that are your AirPods. Once you have done this you can use the **`airp`** keyword to connect / disconnect your AirPods. Whenever you want to change the device you can use the **`airp config`** keyword to select a new bluetooth device.

By default, this workflow also offers the ability to trigger a connect / disconnect action using a hotkey. The default hotkey is **`⌃ Ctrl + ⇧ Shift + ⌘ Cmd + A`**.

## Acknowledgments 
* Big thanks to Daniel Schäfer ([@JohnAZoidberg](https://github.com/JohnAZoidberg)) for helping design the RegEx used in this workflow.
