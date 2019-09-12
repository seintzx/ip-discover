#!/usr/bin/env python3


def my_whois_native(ip):
    # import whois
    # w = whois.whois(ip)
    # for key, value in w.items():
    #     print(key + ": " + str(value))
    return (0)


def my_whois(ip):
    import subprocess
    mycmd = str("whois " + str(ip))
    cmd = subprocess.Popen(mycmd, shell=True, stdout=subprocess.PIPE)
    for line in cmd.stdout:
        line = line.strip()
        if len(line) != 0:
            if "%" not in str(line):
                print(line.decode("utf-8"))
