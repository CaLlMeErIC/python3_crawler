import requests
import re
import json
from urllib.parse import urlencode
def get_page():
    params = {
        "offset": "0",
        "aid":"24",
        "app_name" : "web_search",
        "format": "json",
        "keyword": "南京",
        "autoload": "true",
        "count": "20",
        "from": "search_tab"
    }
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
        "Cookie":'''s_v_web_id=doesntmatter'''
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    #url='https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E5%8D%97%E4%BA%AC&autoload=true&count=20&from=search_tab'
    try:
        response = requests.get(url,headers=headers)
        if response.content:
            return response

    except requests.ConnectionError:
        return None



def main():
    #print(get_page().json())
    for items in get_page().json().get('data'):
        item=items.get('abstract')
        url=items.get('article_url')
        if item:
            print(item,url)
        pass
main()