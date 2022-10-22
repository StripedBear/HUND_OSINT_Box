import re
from dns import reversename, resolver
import socket


def main(ip):
    try:
        if re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}', ip).group():
            ip = socket.gethostbyname(ip)
        rev_name = reversename.from_address(ip)
        rev_dns = str(resolver.query(rev_name, 'PTR')[0])
        return rev_dns
    except Exception as e:
        return 'Error!', e


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)