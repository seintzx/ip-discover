#!/usr/bin/env python3

import argparse
from my_whois import my_whois
from my_dig import my_dig
from my_machinae import my_machinae


def main():
    parser = argparse.ArgumentParser(
        description="IP/Domain information discovery tool")
    parser.add_argument("IP", help="IP address to lookup")
    parser.add_argument("-m",
                        "--machinae",
                        action="store_true",
                        help="Also use machinae")
    args = parser.parse_args()
    IP = args.IP

    if args.machinae:
        print("- machinae ============================")
        my_machinae(IP)

    print("\n- **whois**")
    print("\t```".expandtabs(4))
    my_whois(IP)
    print("\t```".expandtabs(4))

    print("- **dig**")
    print("\t```".expandtabs(4))
    my_dig(IP)
    print("\t```".expandtabs(4))


if __name__ == "__main__":
    main()
