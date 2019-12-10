#!/usr/bin/env python3

import dns.resolver


def dig(ip):
    ids = [
        'NONE',
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
    ]

    myResolver = dns.resolver.Resolver()
    myResolver.nameservers = ['8.8.8.8', '8.8.4.4']
    res = ""
    res += "- **dig**\n"
    res += "\t```\n".expandtabs(4)
    for a in ids:
        try:
            myAnswers = myResolver.query(ip, a)
            for rdata in myAnswers:
                res += "\t".expandtabs(4) + a + ': ' + rdata.to_text() + "\n"
        except Exception as e:
            pass
    res += "\t```\n".expandtabs(4)
    return (res)
