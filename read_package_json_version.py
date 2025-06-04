import sys
import json

jsonfile = sys.argv[1]
with open(jsonfile, 'r') as j:
    package_json = json.loads(j.read())

print(package_json['version'])
