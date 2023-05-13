from dns.resolver import *


def lookup(host: str, rqtype: str) -> query:
    return query(host, rqtype, raise_on_no_answer=False)


def lookup_mails(mails_records: query):
    if mails_records.rrset == None:
        return

    mails_records = sorted(mails_records)

    mails_ip = []

    for mail in mails_records:
        mail_domain = mail.exchange.to_text(omit_final_dot=True)

        mail_ips = lookup(mail_domain, "a").rrset

        for ip in mail_ips:
            mails_ip.append({"domain": mail_domain, "ip": ip})

    return mails_ip


domain = "google.com"
rqtype = "mx"

mails_records = lookup(domain, rqtype)

mails_ip = lookup_mails(mails_records)

if not mails_ip == None:
    for mail in mails_ip:
        print(f"{mail['domain']}:{mail['ip']}")
