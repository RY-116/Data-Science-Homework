import requests
from bs4 import BeautifulSoup
import time
import random


def get_content(str):
    # 用于获得内含标签的str中的纯文本
    ans = ""
    write = False
    for i in str:
        if i == '>':
            write = True
        elif i == '<':
            write = False
        else:
            if write:
                ans += i
    return ans


PROXY_POOL_URL = 'http://127.0.0.1:5555/random'


def get_proxy():
    # 获取ip代理
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text.strip()
    except ConnectionError:
        return None


base_url = 'https://so.jstv.com/?keyword=%E7%96%AB%E6%83%85&page=' # 搜索结果所在网址
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
proxies = {
    'http': 'http://' + get_proxy()
}


filename = 'lizhinews.txt' # 存放爬取结果
start_page = 19
end_page = 3715
error_count = 0

for i in range(start_page, end_page + 1):
    real_url = base_url + str(i)
    r = requests.get(real_url, headers=head, proxies=proxies)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.content, 'html.parser')
    list = soup.find('div', class_="lzxw_lxz").find('ul').find_all('li')

    for element in list:
        try:
            title = str(element.find('span').find('a').string)
            href = str(element.find('span').find('a')['href'])

            news_r = requests.get(href, headers=head)
            news_soup = BeautifulSoup(news_r.content, 'html.parser')

            time1 = str(news_soup.find('p', class_='info fL').find('span', class_='time').string)
            source = str(news_soup.find('p', class_='info fL').find('span', class_='source').string)

            text = str(news_soup.find('div', class_='content').find_all('p', style=""))
            content = get_content(text)

            temp = title + '\n' + href + "\n" + time1 + "  " + source + '\n' + content + '\n' + '\n'
            f = open(filename, 'a', encoding='utf-8')
            f.write(temp)
        except Exception:
            error_count += 1
            continue


    print("爬取第" + str(i) + "页已完成")
    time.sleep(random.random())

print("爬取" + str(start_page) + "-" + str(end_page) + "页完成")
print("共产生" + str(error_count) + "处错误")



