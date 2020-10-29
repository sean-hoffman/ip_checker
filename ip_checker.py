#!/usr/local/bin/python3

import argparse
import sys
import ipaddress

parser = argparse.ArgumentParser(description='Check if an IP address is in a subnet.')
parser.add_argument('-a', '--address', metavar = '<IP Address>')
parser.add_argument('-s', '--subnet', metavar = '<Subnet>')

args = parser.parse_args()

def check_ip_against_subnet(ip, subnet):
    ip = ip.rstrip()
    subnet = subnet.rstrip()
    if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(subnet):
        print(ip + " is in " + subnet)
 
if args.address and args.subnet:
    check_ip_against_subnet(args.address, args.subnet)
    sys.exit()
else:
    print('Checking IPs in: ' + sys.argv[1])
    print('Checking against subnets in: ' + sys.argv[2])

    ip_file = open('./ips_accessed.txt', 'r')
    subnet_file = open('./anyconnect_subnets.txt', 'r')

    ips = ip_file.readlines()
    subnets = subnet_file.readlines()
    ip_count = 0

    for ip in ips:
        for subnet in subnets:
            check_ip_against_subnet(ip, subnet)
        ip_count = ip_count + 1

    print('Checked {} IPs'.format(ip_count))

# string.rstrip() removes trailing whitespace including newline characters (\n)
# this is important because the ipaddress functinos only take numerical values and 
# the python readlines() function includes the newline character at the end of the string

