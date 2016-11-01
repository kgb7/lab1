#!/usr/bin/env python

# Write a Python program using ciscoconfparse that parses thr cisco_ipsec.txt
# config file.
# Note, this config file is not fully valid (i.e. parts of the configuration
# are missing).
# The script should find all of the crypto map entries in the
# file (lines that begin with 'crypto map CRYPTO') and for each crypto map
# entry print out its children.

from ciscoconfparse import CiscoConfParse

ccfg = CiscoConfParse("cisco_ipsec.txt")

crypto_map = ccfg.find_objects(r"^crypto map CRYPTO")

cyrpt_cmap = ccfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

ccmap = ccfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES-")


for i in range(len(crypto_map)):
    print "\n"
    print crypto_map[i]
    for child in crypto_map[i].children:
        print child

print "\nparents with pfs group2\n"

for i in cyrpt_cmap:
    print i

print "\nparents not using AES\n"

for i in ccmap:
    print i
