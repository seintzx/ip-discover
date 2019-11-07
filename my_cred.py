#!/usr/bin/env python3


def my_cred():
    import configparser
    config = configparser.ConfigParser()
    config.read("config.txt")
    api_key = config.get("configuration", "API")
    return (api_key)
