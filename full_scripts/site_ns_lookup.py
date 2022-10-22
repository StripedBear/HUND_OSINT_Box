import re
from nslookup import Nslookup


def main(user_in):
    try:
        domain = re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}', user_in).group()
    except Exception as e:
        return e

    dns_query = Nslookup(dns_servers=['1.1.1.1'])

    ips_record = dns_query.dns_lookup(domain)
    all_records = []
    for i in ips_record.response_full:
        all_records.append(i)

    soa_record = dns_query.soa_lookup(domain)
    for i in soa_record.response_full:
        all_records.append('\n'.join(i.split('. ')))
    return '\n'.join(all_records)

def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)