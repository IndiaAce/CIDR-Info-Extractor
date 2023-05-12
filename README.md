# CIDR-Info-Extractor
This Python application takes a CIDR block as input and returns the following:
* Netmask
* First IP address in the range
* Last IP address in the range
* Total number of hosts

## Requirements
Python 3.7 or higher

## Usage
Clone the repository:
git clone https://github.com/IndiaAce/CIDR-Info-Extractor.git

## Navigate to the directory:
cd CIDR_Info_Extractor

## Run the Python script:
python cidr_info.py

## When prompted, enter the CIDR block:
Enter CIDR: 192.168.1.0/23

The application will output the requested information, for example:
* Netmask: 255.255.254.0
* First IP: 192.168.1.1
* Last IP: 192.168.2.254
* Total Hosts: 510
### Note
*The 'First IP' and 'Last IP' are calculated by adding and subtracting 1 from the network address and the broadcast address respectively. This is because in a network, the first address is reserved for the network identifier and the last one is reserved for the broadcast address.*

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
