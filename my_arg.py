#!/usr/bin/env python3


def my_arg():
    import argparse
    parser = argparse.ArgumentParser(
        description=
        "IP/Domain information discovery tool and Hash search on virus total")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a",
                       "--hash",
                       action="store",
                       help="search hash on virustotal")
    group.add_argument("-i",
                       "--ip",
                       action="store",
                       help="IP address or domain to lookup")
    parser.add_argument("-m",
                        "--machinae",
                        action="store_true",
                        help="also use machinae")

    return (parser.parse_args())
