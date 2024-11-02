import json
import os

def read_config():
    with open('config.json', 'r') as file:
        return json.load(file)
