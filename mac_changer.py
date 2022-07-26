#!/usr/bin/env python

from ast import arguments
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option(
            '-i',
            '--interface',
            dest='interface',
            help='Interface to change its MAC address'
        )
    parser.add_option(
            '-m',
            '--mac',
            dest='new_mac',
            help='new MAC address'
        )
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info')
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info')
    return options, arguments

def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}')

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
    


options, arguments = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
print(ifconfig_result.decode())