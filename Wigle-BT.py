import requests
import json
import argparse
import sys

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Error: config file not found')
        return None

def get_location(netid, config):
    headers = {
        'Authorization': 'Basic ' + config['api_auth']
    }

    url = 'https://api.wigle.net/api/v2/bluetooth/search?onlymine=false&netid=' + netid
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Error: ' + response.text)
        return None

    data = response.json()

    if not data['results']:
        print('Error: no results found')
        return None

    location = (data['results'][0]['trilat'], data['results'][0]['trilong'])
    return location

def format_output(location, output_formats):
    """Format location data based on requested output formats"""
    lat, lon = location
    results = []
    
    for fmt in output_formats:
        if fmt == 'full-coordinate':
            results.append(f"({lat}, {lon})")
        elif fmt == 'latitude':
            results.append(str(lat))
        elif fmt == 'longitude':
            results.append(str(lon))
        elif fmt == 'google-maps':
            results.append(f"https://www.google.com/maps/place/{lat},{lon}")
    
    return results

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Wigle-BT - Bluetooth Device Trilateration Tool')
    parser.add_argument('--mac', type=str, help='Bluetooth MAC address to search for')
    parser.add_argument('--output', type=str, help='Output format(s): full-coordinate, latitude, longitude, google-maps (comma-separated)')
    
    args = parser.parse_args()
    
    config = load_config()
    if not config:
        return

    # Command-line mode
    if args.mac:
        if not args.output:
            print('Error: --output parameter is required when using --mac')
            sys.exit(1)
        
        # Parse output formats
        output_formats = [fmt.strip() for fmt in args.output.split(',')]
        valid_formats = ['full-coordinate', 'latitude', 'longitude', 'google-maps']
        
        for fmt in output_formats:
            if fmt not in valid_formats:
                print(f'Error: Invalid output format "{fmt}". Valid formats: {", ".join(valid_formats)}')
                sys.exit(1)
        
        # Get location
        location = get_location(args.mac, config)
        
        if location:
            results = format_output(location, output_formats)
            for result in results:
                print(result)
        else:
            sys.exit(1)
        
        return

    # Interactive mode
    # Display ASCII art once at startup
    print('------------------------------------------------------')
    print('|                  kkNXK0OOOkkOOO0                   |') 
    print('|              kkkNXK0OOOkkOOO0KXNkkkk               |')
    print('|           dNX0OOkkkkkkkkkkkkkkkkOO0XNd             |')
    print('|         ;N0OkkkkkkkkkkdokkkkkkkkkkkkkkO0N:         |')
    print('|       ,XOkkkkkkkkkkkkkx  okkkkkkkkkkkkkkkOX;       |')
    print('|      OOkkkkkkkkkkkkkkkx    ckkkkkkkkkkkkkkkO0      |')
    print('|     XOkkkkkkkkkkkkkkkkx      :kkkkkkkkkkkkkkOX     |')
    print('|    0kkkkkkkkkkkkkkkkkkx        ;kkkkkkkkkkkkkkK    |')
    print('|   dOkkkkkkkkkkkkkkkkkkx          ,kkkkkkkkkkkkkd   |')
    print('|  .Okkkkkkkkkkkkkkkkkkkx    .o       kkkkkkkkkkkO   |')
    print('|  xkkkkkkkkkd  ;kkkkkkkx    .OKd      .kkkkkkkkkkx  |')
    print('|  Okkkkkkko      ,kkkkkx    .kkOKx      .kkkkkkkkO. |')
    print('| ;kkkkkkkkOXo       kkkx    .kkkk       NOkkkkkkkk: |')
    print('| okkkkkkkkkkOKx      .kx    .kx       N0kkkkkkkkkko |')
    print('| xkkkkkkkkkkkkOKk                  .N0kkkkkkkkkkkkx |')
    print('| kkkkkkkkkkkkkkkOKO              .N0kkkkkkkkkkkkkkk |')
    print('| OkkkkkkkkkkkkkkkkOK0           XOkkkkkkkkkkkkkkkkO |')
    print('| kkkkkkkkkkkkkkkkkkkOKx      .XOkkkkkkkkkkkkkkkkkkk |')
    print('| kkkkkkkkkkkkkkkkkkkc           kkkkkkkkkkkkkkkkkkk |')
    print('| kkkkkkkkkkkkkkkkk:               kkkkkkkkkkkkkkkkk |')
    print('| dkkkkkkkkkkkkkk;           .       xkkkkkkkkkkkkkd |')
    print('| lkkkkkkkkkkkk,      lXx    .0N.      dkkkkkkkkkkkl |')
    print('| ,kkkkkkkkkk       dKOkx    .kk0N.      dkkkkkkkkk, |')
    print('|  kkkkkkkkk      xKOkkkx    .kkkk;      cOkkkkkkkk  |')
    print('|  lkkkkkkkk0N  kKOkkkkkx    .kk       lXOkkkkkkkkl  |')
    print('|  .kkkkkkkkkk0KOkkkkkkkx    ..      dKOkkkkkkkkkk.  |')
    print('|   :kkkkkkkkkkkkkkkkkkkx          xKOkkkkkkkkkkkc   |')
    print('|    dkkkkkkkkkkkkkkkkkkx        kKOkkkkkkkkkkkkd    |')
    print('|     xkkkkkkkkkkkkkkkkkx      0KOkkkkkkkkkkkkkd     |')
    print('|      lkkkkkkkkkkkkkkkkx    KKOkkkkkkkkkkkkkkl      |')
    print('|       .kkkkkkkkkkkkkkkx  N0Okkkkkkkkkkkkkkk.       |')
    print('|          kkkkkkkkkkkkkxN0kkkkkkkkkkkkkkkk.         |')
    print('|            .kkkkkkkkkkOkkkkkkkkkkkkkkk.            |')
    print('|                  dkkkkkkkkkkkkkkd                  |')
    print('|                                                    |')
    print('|----------------------------------------------------|')
    print('|   Wigle-BT --- Bluetooth Device Trilateration Tool |')
    print('|----------------------------------------------------|')

    while True:
        print('|----------------------------------------------------|')
        print('|                1. Get Device Location              |')
        print('|                2. Exit                             |')
        print('|----------------------------------------------------|')
        choice = input('        Enter choice (1/2): ')

        if choice == '1':
            netid = input('Enter Bluetooth network MAC address: ')
            location = get_location(netid, config)

            if location:
                print('Location: ' + str(location))
                print('Google Maps URL:  https://www.google.com/maps/place/' + str(location).replace(' ', '').replace('(', ''))
        elif choice == '2':
            break
        else:
            print('Error: invalid choice')

if __name__ == '__main__':
    main()
