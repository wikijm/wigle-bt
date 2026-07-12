
                                          w@@@@@@@@@@@@@@@@@@@@@@w
                                       w@@@@@@@@@@@@@@@@@@@@@@@@@@@@w,
                                    q@@@@@@@KMM*""````````""*%MK@@@@@@@W
                                  @@@@@@M*`                      `*%@@@@@@,
                                 @@@@@M                              *@@@@@N
                               @@@@@                                   1@@@@@
                              @@@@@                j@W,                 `@@@@@
                             @@@@@                 j@@@@W,               `@@@@@
                            ]@@@@                  j@@@@@@@W              1@@@@N
                            @@@@                   j@@@@@@@@@@w            %@@@@
                            @@@@             ,     j@@@@D*K@@@@@@w         J@@@@N
                            @@@@           ,@@@W   j@@@@H  `@@@@@@M`        @@@@@
                            @@@@          `%@@@@@N j@@@@H,#@@@@@M`           @@@@
                            @@@N            `*@@@@@@@@@@@@@@@@M              @@@@
                            @@@N               *@@@@@@@@@@@@M                @@@@
                            @@@N                 "K@@@@@@K"                  @@@@
                            @@@N                 a@@@@@@@@W                  @@@@
                            @@@N              ,#@@@@@@@@@@@@N                @@@@
                            @@@N            ,@@@@@@K@@@@K@@@@@@p             @@@@
                            @@@@          -@@@@@@M j@@@@H *@@@@@@p           @@@@
                            @@@@           `*@K"   j@@@@H  ,@@@@@@@H         @@@@
                            @@@@H                  j@@@@N@@@@@@@M`          @@@@
                            W@@@@                  j@@@@@@@@@M`            @@@@@
                             @@@@N                 j@@@@@@M"              ]@@@@
                             V@@@@p                j@@@M"                J@@@@
                              %@@@@W               jM"                  z@@@@
                               1@@@@@                                 ,@@@@@
                                @@@@@Np                            ,#@@@@@
                                 @@@@@@Nw,                    ,a#@@@@@@
                                  "%@@@@@@@@@Kpwwwwaaawwwp@@@@@@@@@@M
                                      *K@@@@@@@@@@@@@@@@@@@@@@@@MM

                            # Wigle-BT - Bluetooth Device Trilateration Tool.

# Wigle-BT
This tool allows you to get the approximate location of a Bluetooth device using the long-awaited: Wigle.net API. The tool uses trilateration to calculate the BT device location based on its signal strength and the location of nearby devices.

## Requirements
To use this tool, you need to have Python 3 installed on your system. You also need to create a free account on Wigle.net and obtain an API key.

## Installation
Clone this repository or download the ZIP file and extract it to a directory of your choice.

It is highly recommended to use a Python virtual environment. Open a terminal or command prompt in the directory where you extracted the files and run:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

Then, install the required Python libraries by running:

```bash
pip3 install -r requirements.txt
```

You need a Wigle.net API key to use this tool. When you run the script for the first time, if `config.json` is missing, an interactive assistant will prompt you to enter your API key and will create the configuration file for you automatically.

Alternatively, you can manually create a `config.json` file in the same directory based on the provided `config.json.example` template.

## Usage

### Interactive Mode
Open a terminal or command prompt in the directory where you extracted the files.

Run the command:

```bash
python3 Wigle-BT.py
```

Choose option 1 to get the location of a bluetooth device.

Enter the MAC address of the bluetooth device when prompted.

The tool will display the latitude and longitude of the bt device's location.

### Command-Line Mode
You can also use the tool with command-line parameters for automation and scripting:

```bash
python3 Wigle-BT.py --mac <MAC_ADDRESS> --output <OUTPUT_FORMAT>
```

**Parameters:**
- `--mac`: The MAC address of the Bluetooth device (e.g., `AA:BB:CC:DD:EE:FF`)
- `--output`: Output format(s), comma-separated. Available formats:
  - `full-coordinate`: Display coordinates as `(latitude, longitude)`
  - `latitude`: Display only the latitude value
  - `longitude`: Display only the longitude value
  - `google-maps`: Display Google Maps URL with coordinates

**Examples:**

Get Google Maps URL:
```bash
python3 Wigle-BT.py --mac AA:BB:CC:DD:EE:FF --output google-maps
```

Get latitude and longitude separately:
```bash
python3 Wigle-BT.py --mac AA:BB:CC:DD:EE:FF --output latitude,longitude
```

Get all available output formats:
```bash
python3 Wigle-BT.py --mac AA:BB:CC:DD:EE:FF --output full-coordinate,latitude,longitude,google-maps
```

## License
This tool is licensed under the MIT license. See the LICENSE file for more information.

## Acknowledgments
This tool was created using the Wigle.net API and the trilateration algorithm developed by Thomas Pototschnig. Thanks to the developers of these tools for making this project possible.
