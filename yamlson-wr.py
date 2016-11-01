#!/usr/bin/env python

import yaml
import json

my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]['ip_addr'] = '192.168.58.110'
my_list[-1]['attribs'] = range(7)

with open('config.yml', 'w',) as outfile:
    yaml.dump(my_list, outfile, default_flow_style=False)

with open('config.json', 'w',) as outfile:
    json.dump(my_list, outfile)
    
#yaml.dump(my_list, default_flow_style=True)  #or False for flow style.e
