#!/usr/bin/env python3

import argparse
from my_whois import my_whois
from my_dig import my_dig
from my_machinae import my_machinae


def init_args():
    parser = argparse.ArgumentParser(
        description="IP/Domain information discovery tool")
    parser.add_argument("IP", help="IP address to lookup")
    args = parser.parse_args()
    return (args.IP)


def main():
    IP = init_args()
    print("whois ===============================")
    my_whois(IP)
    print("dig =================================")
    my_dig(IP)
    print("machinae ============================")
    my_machinae(IP)


if __name__ == "__main__":
    main()
