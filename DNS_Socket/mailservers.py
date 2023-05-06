import dns.resolver


def lookup(_domain: str, _rqtype: str) -> None:
    return dns.resolver.query(_domain, _rqtype, raise_on_no_answer=False)


def lookup_mail(_mail_records):
    if _mail_records.rrset == None:
        return

    _mail_ips = []

    _mail_records = sorted(_mail_records)

    for record in _mail_records:
        mail_name = record.exchange.to_text(omit_final_dot=True)
        mail_name_lookup = lookup(mail_name, "a")
        for ip in mail_name_lookup:
            _mail_ips.append({"domain": mail_name, "ip": ip})

    return _mail_ips


domain = "google.com"
rqtype = "mx"

mail_records = lookup(domain, rqtype)

mail_ips = lookup_mail(mail_records)

for record in mail_ips:
    print(f"{record['domain']}:{record['ip']}")
