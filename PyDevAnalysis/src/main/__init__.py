#===============================================================================
# This is a first test for reading in the JSON data and doing something
# really lame with it. - Jeff
#===============================================================================

import json
from pprint import pprint

# Get a file pointer
data = open('../../Data/RawJSONData.txt')

for e in data:
    print e

# close the file pointer
data.close()

