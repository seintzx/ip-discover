#!/usr/bin/env python3

import subprocess


def get_reputation(ip):
    mycmd = str("machinae " + str(ip))
    cmd = subprocess.Popen(mycmd, shell=True, stdout=subprocess.PIPE)
    res += ""
    res += "- machinae ============================\n"
    for line in cmd.stdout:
        line = line.strip()
        if len(line) != 0:
            if "Requesting" not in str(line) and \
               "Error" not in str(line) and \
               "--list-sites" not in str(line) and \
               chr(line[0]) != '*':
                res += line.decode("utf-8") + "\n"
    return (res)
