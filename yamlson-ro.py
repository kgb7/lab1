#!/usr/bin/env python

import yaml
import json


with open('config.yml', 'r',) as infile:
    yf = yaml.safe_load(infile)

with open('config.json', 'r',) as infile:
    jf = json.load(infile)

print yaml.dump(yf, default_flow_style=False)
print json.dumps(jf, indent=4, sort_keys=True)
#yaml.dump(my_list, default_flow_style=True)  #or False for flow style.e
