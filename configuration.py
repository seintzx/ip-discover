#!/usr/bin/env python3

import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("config.txt")
    api_key = config.get("configuration", "API")
    return (api_key)
