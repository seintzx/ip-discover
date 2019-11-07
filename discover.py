#!/usr/bin/env python3

from my_arg import my_arg
from my_cred import my_cred
from my_dig import my_dig
from my_machinae import my_machinae
from my_vt import my_vt
from my_whois import my_whois


def main():
    args = my_arg()

    IP = args.ip
    HASH = args.hash

    if args.hash:
        my_vt(HASH, my_cred())
    elif args.machinae:
        my_machinae(IP)
        my_whois(IP)
        my_dig(IP)
    else:
        my_whois(IP)
        my_dig(IP)


if __name__ == "__main__":
    main()
