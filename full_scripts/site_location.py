import re
import pygeoip
from os.path import abspath
import socket
from inspect import getsourcefile


def location(user_input):
    p = abspath(getsourcefile(lambda:0))
    gi = pygeoip.GeoIP(str(p)[:-16] + 'GeoIPCity.dat')
    city = gi.record_by_addr(user_input)
    info = []
    for key in city:
        if city[key] is None or city[key] == 0:
            continue
        else:
            info.append(f"{key}: {city[key]}")        
    return '\n'.join(info)



def main(user_input):
    try:
        if re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}', user_input).group():
             user_input = socket.gethostbyname(user_input)
        return location(user_input)
    except Exception:
        return 'Wrong input or nothing to show'


def my_func(target, write=False):
    result = main(target)
    if write:	
        return result
    print(result)
    
    
