import socket
import re


def main(user_input):
    try:
        host = re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}',
                         user_input).group()
        remote_ip = socket.gethostbyname(host)
        return f"IP address of {host} is {remote_ip}"
    except Exception:
        return 'Error of input or host doesn`t exist'


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)