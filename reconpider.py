#!/bin/python3
"""
An automation python tool for subdoamin enumeration and other features. ( For university presentation )
"""
import requests
import json
import ipaddress
import argparse
import pyfiglet
import datetime
import os
import sys

banner = pyfiglet.figlet_format("ReconPider")
# Import needs package

parser = argparse.ArgumentParser(
    usage="reconpider",
    description="An automation python tool for subdoamin enumeration and other features. ( For university presentation )",
)  # make argument parser
parser.add_argument(
    "-d", dest="domain", type=str, help="Doamin for finding all subdomains"
)
parser.add_argument(
    "-i", dest="input", type=str, help="Input for utilize other feature's"
)
parser.add_argument("-s", dest="search", action="store_true",help="Search ASN for finding CIDR")
parser.add_argument("-c", dest="cidr", help="convert CIDR to IP")
parser.add_argument("-w", dest="wordlist", action="store_true",help="make a wordlist")
parser.add_argument("-o", dest="output", help="Save result to file")
parser.add_argument("-S", dest="silent", action="store_true", help="Show minimal result")
parser.add_argument(
    "-V",
    action="version",
    help="Show version of program",
    version="Version:    1.0.0 - Powered by madisec",
)
args = parser.parse_args()
domain = args.domain
user_input = args.input
search = args.search
cidr = args.cidr
wordlist = args.wordlist
output = args.output
silent = args.silent

def searhc_bgp(input_flag:str):
    response = requests.get(f"https://api.bgpview.io/search?query_term={input_flag}")
    load_json = json.loads(response.text)
    dump_json = json.dumps(load_json, indent=2)
    return dump_json

# Convert CIDR to IP in all of in the range
def cidr_to_ip(cidr):
    ip_network = ipaddress.ip_network(cidr)
    ips = []
    for ip in ip_network.hosts():
        ips.append(ip)
        for trace in ips:
            print(trace)


def call_crt(get_domain:str):
    response = requests.get(f"https://crt.sh/?q={get_domain}&output=json")
    json_data = json.loads(response.text)
    seen_common_name = set()
    try:
        for i in json_data:
            common_name = i["common_name"]
            if common_name not in seen_common_name:
                seen_common_name.add(common_name)
                to_str = str(common_name)
                for j in to_str.splitlines():
                        print(j)
                        
    except:
        print("Error")

def make_wordlist(get_domain):
    proc = os.system(f"subfinder -d {get_domain} -all -silent | rev | cut -d '.' -f3 | rev | sort -u")
    print(proc)

# Subdomain enumeration condition's
if domain and silent and output:
    with open(output, "w") as f:
        f.write(call_crt(domain))
        print("Save result to file")
elif domain and silent:
    call_crt(str(domain))
elif domain and output:
    print(banner)
    result = call_crt(domain)
    with open(output,"w") as f:
        f.write(result)
    print(result)
elif domain:
    print(banner)
    call_crt(str(domain))

    
    
if search and user_input and silent and output:
    result = searhc_bgp(user_input)
    print(result)
    with open(output, "w") as f:
        f.write(result)
        
    print("Seve result to file - Status: OK")
elif search and user_input and silent:
    result = searhc_bgp(user_input)
    print(result)
elif search and user_input and output:
    result = searhc_bgp(user_input)
    with open(output, "w") as f:
        f.write(result)
        
    print("Save result to file - Status: OK")
elif search and user_input:
    print(banner)
    print(result)


resut_wordlist = make_wordlist(domain)
if wordlist and domain and silent and output:
    print(resut_wordlist)
    with open(output, "w") as f:
        f.write(resut_wordlist)
    print("Save result fo file - Status: OK")
elif wordlist and domain and silent:
    print(resut_wordlist)
elif wordlist and domain and output:
    print(banner)
    with open(output, "w") as f:
        f.write(resut_wordlist)
    print("Save result to file - Status: OK")
elif wordlist and domain:
    print(banner)
    print(resut_wordlist)


