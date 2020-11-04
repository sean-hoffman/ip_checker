#!/usr/local/bin/python3

import argparse
import sys
import ipaddress

parser = argparse.ArgumentParser(description='Check if an IP address is in a subnet.')
parser.add_argument('-a', '--address', metavar = '<IP Address>')
parser.add_argument('-s', '--subnet', metavar = '<Subnet>')
parser.add_argument('-i', '--iplist', metavar = '<IP List Input File>')
parser.add_argument('-n', '--networklist', metavar = '<Network List Input File>')

args = parser.parse_args()

def check_ip_against_subnet(ip, subnet):
    ip = ip.rstrip()
    subnet = subnet.rstrip()
    if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(subnet):
        print(ip + " is in " + subnet)

def get_help():
    print("Please see help info for valid inputs: ip_checker.py -h")
    sys.exit()
 

if args.address and args.subnet:
    check_ip_against_subnet(args.address, args.subnet)
    sys.exit()

elif args.iplist and args.networklist:
    print('Checking IPs in: ' + args.iplist)
    print('Checking against subnets in: ' + args.networklist)

    ip_file = open(str(args.iplist), 'r')
    subnet_file = open(str(args.networklist), 'r')

    ips = ip_file.readlines()
    subnets = subnet_file.readlines()
    ip_file.close()
    subnet_file.close()

    ip_count = 0
    for ip in ips:
        for subnet in subnets:
            check_ip_against_subnet(ip, subnet)
        ip_count = ip_count + 1

    print('Checked {} IPs'.format(ip_count))

else:
    get_help()

