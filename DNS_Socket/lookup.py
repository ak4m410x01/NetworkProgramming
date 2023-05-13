from dns.resolver import *

DNS_RECORDS = ["a", "aaaa", "ns", "mx", "cname", "txt"]


def lookup(host: str, rqtype: str) -> str:
    return query(host, rqtype, raise_on_no_answer=False).rrset


domain = "google.com"

for record in DNS_RECORDS:
    ans = lookup(domain, record)

    if not ans == None:
        print(ans)
