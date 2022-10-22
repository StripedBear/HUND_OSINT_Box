import requests
from bs4 import BeautifulSoup
import re


def main(url):
    try:
        url = re.search(r'https?:\/\/[\w\d.-]*\.\w{2,4}', url).group()
    except Exception:
        url = 'https://' + re.search(r'[\w\d.-]*\.\w{2,4}', url).group()
    try:
        page = requests.get(url + '/sitemap.xml')
        if page.status_code == 200:
            return get_data_page(page)
        else:
            page = requests.get(url + '/sitemap.txt')
            if page.status_code == 200:
                return get_data_page(page)
            else:
                return 'File sitemap not found!'
    except Exception as e:
        return 'Error', e


def get_data_page(page):
    data_list = []
    for i in BeautifulSoup(page.text, 'lxml').find_all('loc'):
        data_list.append(i.text)
    return '\n'.join(data_list)


def my_func(target, write=False):
    result = main(target)
    if write:
        return result
    print(result)
