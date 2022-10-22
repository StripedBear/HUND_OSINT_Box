import dns.resolver
import re


def main(user_in):
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    try:
        user_in = re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}', user_in).group()
        answers = my_resolver.query(user_in, 'MX')
        records = []
        [records.append(f"'MX record' {rdata.exchange}") for rdata in answers]
        return '\n'.join(records)
    except Exception as e:
        return e


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)
