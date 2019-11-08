#!/usr/bin/env python3

import parameters
import configuration
import digger
import reputation
import virustotal
import whois


def main():
    args = parameters.param()

    ip = args.ip
    hash_ = args.hash

    if args.hash:
        virustotal.get_report(hash_, configuration.get_config())
    elif args.machinae:
        reputation.get_reputation(ip)
        whois.get_info(ip)
        digger.dig(ip)
    else:
        whois.get_info(ip)
        digger.dig(ip)


if __name__ == "__main__":
    main()
