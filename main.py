#!/usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()
# options are the values we are entering

parser.parse_args()

interface = input("interface > ")
new_Mac = input("new MAC >")
# use 'raw_input' instead of 'input' if using python 2.7

print("[+] Changing Mac Address for " + interface + " to " + new_Mac)

# for security reasons, we shall use lists instead of plain strings#

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_Mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])

# subprocess.call("sudo ifconfig " + interface + " down", shell=True)
# subprocess.call("sudo ifconfig " + interface + " hw ether " + new_Mac, shell=True)
# subprocess.call("sudo ifconfig " + interface + " up", shell=True)
