#!/usr/bin/env python3
# https://developers.virustotal.com/reference#file-report

import requests


def get_report(hasher, api):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api, 'resource': hasher}
    response = requests.get(url, params=params)
    print(response.json())
