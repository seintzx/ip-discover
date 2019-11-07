#!/usr/bin/env python3


def my_machinae(ip):
    import subprocess
    mycmd = str("machinae " + str(ip))
    cmd = subprocess.Popen(mycmd, shell=True, stdout=subprocess.PIPE)
    print("- machinae ============================")
    for line in cmd.stdout:
        line = line.strip()
        if len(line) != 0:
            if "Requesting" not in str(line) and \
               "Error" not in str(line) and \
               "--list-sites" not in str(line) and \
               chr(line[0]) != '*':
                print(line.decode("utf-8"))
