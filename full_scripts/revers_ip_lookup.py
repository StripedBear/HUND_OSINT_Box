import requests


def main(ip):
    try:
        page = requests.get(
            'https://api.hackertarget.com/reverseiplookup/?q=' + ip)
        return page.text
    except Exception as e:
        return e


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)