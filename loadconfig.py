import json

with open('config.json') as config_file:
    data = json.load(config_file)

proto = data['proto']
directory = data['directory']
