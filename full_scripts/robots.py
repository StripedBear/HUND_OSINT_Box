import re
import requests


def main(url):
    try:
        url = re.search(r'https?:\/\/[\w\d.-]*\.\w{2,4}', url).group()
    except Exception:
        url = 'https://' + re.search(r'[\w\d.-]*\.\w{2,4}', url).group()
    finally:
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.43 (KHTML, like Gecko) '
                            'Chrome/91.0.4472.101 Safari/537.36 '
                            'OPR/77.0.4054.90'}
        try:
            page = requests.get(url + '/robots.txt', headers=head)
            if page.status_code != 404:
                return page.text
            else:
                return 'File "robots.txt" not found'
        except Exception as e:
            return e


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)
