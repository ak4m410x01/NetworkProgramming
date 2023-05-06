import dns.resolver

dns_records = ["a", "aaaa", "ns", "mx", "cname", "txt"]


def lookup(_domain: str, _rqtype: str):
    return dns.resolver.query(_domain, _rqtype, raise_on_no_answer=False).rrset


domain = "google.com"
rqtype = "a"

for record in dns_records:
    ans = lookup(domain,record)
    if not ans == None:
        print(ans)
    
