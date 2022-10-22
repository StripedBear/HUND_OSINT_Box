import re
import whois


def main(user_in):
    try:
        user_in = re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}', user_in).group()
        domain = whois.whois(user_in)
        info = []
        for i in domain:
            if type(domain.get(i)) is list:
                info.append(f"{i}: ")
                for j in domain.get(i):
                    info.append(j)
            else:
                info.append(f"{i}: {domain.get(i)}")
        return '\n'.join(info)
    except:
        return 'Input Error'


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)
