#!/usr/bin/env python3

import clipboard
import configuration
import digger
import parameters
import reputation
import virustotal
import whois


def main():
    args = parameters.param()

    ip = args.ip
    hash_ = args.hash

    result = ""

    if args.hash:
        result += virustotal.get_report(hash_, configuration.get_config())
    elif args.machinae:
        result += reputation.get_reputation(ip)
        result += whois.get_info(ip)
        result += digger.dig(ip)
    else:
        result += whois.get_info(ip)
        result += digger.dig(ip)

    clipboard.copy(result)
    print(result)


if __name__ == "__main__":
    main()
