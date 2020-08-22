#!/usr/bin/env python3
#
# This script pulls the parameters from F5 ARM templates for use in Ansible playbook
#

import json

# Open the f5 CFT or ARM template file
with open('./azuredeploy.parameters.json') as json_file:  
    # Import the file as a JSON object
    data = json.load(json_file)
    # Loop through each parameter (p) in the parameters section
    paramlist = []
    for p in data['parameters']:
            value = str(data['parameters'][p]['value'])
            paramlist.append(p + ':  "' + value + '"')
    paramlist = (sorted(paramlist))
    for p in paramlist:
        print(p)
