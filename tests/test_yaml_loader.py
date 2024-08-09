"""
@author rain
@date 8/10/2024 7:34 AM
"""

import yaml

with open('test.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print(type(data))
    for key in data:
        print(key, ':',  data[key])
