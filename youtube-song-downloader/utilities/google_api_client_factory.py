#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from googleapiclient.discovery import build

def get_api_key(filename):
   with open(filename) as json_file:
       json_data = json.load(json_file)

   api_key = json_data['apiKey']
   return api_key

def get_authenticated_client(service_name, version, api_key_file):
    api_key = get_api_key(api_key_file)
    client = build(service_name, version, developerKey=api_key)
    return client
