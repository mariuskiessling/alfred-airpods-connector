# [Alfred AirPods Connector](https://github.com/mikeoertli/alfred-airpods-connector)

<p align="center">
<img width="200" alt="Alfred Airpods Connector" src="icon.png"/>
</p>

This [Alfred v4](https://www.alfredapp.com/) workflow helps you to quickly connect to your AirPods using the Alfred search or a hotkey.

Check out the [Raycast variant](https://github.com/mikeoertli/raycast-airpods-connector) too, if you use Raycast instead/also.

## Demo

![Workflow demo](https://github.com/mariuskiessling/alfred-airpods-connector/raw/master/demo.gif "Workflow demo")

## Installation

1. Using [`brew`](https://brew.sh/), install/update `BluetoothConnector` utility using

   ```shell
   brew install bluetoothconnector
   ```

   or

   ```shell
   brew update && brew upgrade bluetoothconnector
   ```

2. Download the workflow file [↗ here](https://github.com/mikeoertli/alfred-airpods-connector/releases) and import it into Alfred.

It is recommended to have `HOMEBREW_PREFIX` defined, for M1 Macs this will be `/opt/homebrew/`.

## Debug

If you encounter any errors running the workflow double-check the steps above and test whether you have Python 3.x installed on your system (Python 2.x is no longer compatible with this workflow).

## Usage

On your first run, you have to select the bluetooth device that are your AirPods. Once you have done this you can use the **`airp`** keyword to connect / disconnect your AirPods. Whenever you want to change the device you can use the **`airp config`** keyword to select a new bluetooth device.

By default, this workflow also offers the ability to trigger a connect / disconnect action using a hotkey. The default hotkey is **`⌃ Ctrl + ⇧ Shift + ⌘ Cmd + A`**.

## Acknowledgments

* Big thanks to Marius Kießling ([@mariuskiessling](https://github.com/mariuskiessling/alfred-airpods-connector)) for creating the original workflow
* Big thanks to Daniel Schäfer ([@JohnAZoidberg](https://github.com/JohnAZoidberg)) for helping design the RegEx used in this workflow.
