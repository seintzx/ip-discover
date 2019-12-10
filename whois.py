#!/usr/bin/env python3

import subprocess


def my_whois_native(ip):
    # import whois
    # w = whois.whois(ip)
    # for key, value in w.items():
    #     print(key + ": " + str(value))
    return (0)


def get_info(ip):
    mycmd = str("whois " + str(ip))
    cmd = subprocess.Popen(mycmd, shell=True, stdout=subprocess.PIPE)
    res = ""
    res += "\n- **whois**\n"
    res += "\t```\n".expandtabs(4)
    for line in cmd.stdout:
        line = line.strip()
        if len(line) != 0 and \
           chr(line[0]) != "%" and \
           chr(line[0]) != "#":
            res += "\t".expandtabs(4) + line.decode("utf-8") + "\n"
    res += "\t```\n".expandtabs(4)
    return (res)
