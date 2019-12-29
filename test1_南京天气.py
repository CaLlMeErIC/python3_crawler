import requests
import re
def get_one_page(url):

    response = requests.get(url)
    if response.status_code == 200:
        return response
    return None

def get_data(text_str):
    #pattern = re.compile('<h1>.*?（明天）</h1>.*?<p title=.*?class="wea">(.*?)</p>',re.S)
    pattern = re.compile('<h1>.*?（今天）</h1>.*?<p title=.*?class="wea">(.*?)</p>.*?<h1>.*?（明天）</h1>.*?<p title=.*?class="wea">(.*?)</p>', re.S)
    items=re.findall(pattern,text_str)
    print("南京今明天气",items)

def main():
    url = 'http://www.weather.com.cn/weather/101190101.shtml'
    html = get_one_page(url)
    html_doc = str(html.content, 'UTF-8')
    get_data(html_doc)



main()