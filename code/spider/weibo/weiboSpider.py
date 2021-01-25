import requests
from bs4 import BeautifulSoup
import time
import random


def get_content(str):
    # 用于获得内含标签的str中的纯文本
    ans = ""
    write = False
    count = 0
    for i in str:
        if i == '>':
            write = True
        elif i == '<':
            write = False
        elif i == '#':
            count += 1
        else:
            if write and (count % 2 == 0):
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

# 搜索结果所在网址
base_url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%E7%96%AB%E6%83%85&advancedfilter=1&hasori=1&starttime=20200310&endtime=20200630&sort=time&page='
head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': '_T_WM=71345515258; SCF=Aqde6NoTDhsEfl8BJwQI0Z5vgtEA7CtnP64n-cbOfSrhZGWfRsM1x_sFlXR-UOz-5RW39QwcA9Ej_8s6wbVnTLg.; SUB=_2A25NCGUqDeRhGeBP6VEQ9CrIzDqIHXVu8wtirDV6PUJbktANLUzakW1NRX8UHFN3Jey8SxqcHqtLDGi4HmQte34B; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhseaBECl4pMTT9KQMmhDS95NHD95QceKz0eKBXShMcWs4DqcjsMrSr9NSr',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
proxies = {
    'http': 'http://' + get_proxy()
}

filename = 'weibo.txt' # 存放爬取结果
start_page = 1
end_page = 267
error_count = 0

for i in range(start_page, end_page):
    real_url = base_url + str(i)
    r = requests.get(real_url, headers=head, proxies=proxies)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.content, 'html.parser')
    list = soup.find_all('div', class_='c')


    for j in list:
        try:
            # print(j.find('div').find('a')['href'])
            # print(j.find('div').find('a').string)
            # print(get_content(str(j.find('div'))))
            # print(j.find_all('div')[-1].find_all('a')[-4].string)
            # print(j.find_all('div')[-1].find_all('a')[-3].string)
            # print(j.find_all('div')[-1].find_all('a')[-2].string)
            # print(j.find_all('div')[-1].find('span', class_='ct').string)


            user_name = str(j.find('div').find('a').string)
            user_http = str(j.find('div').find('a')['href'])
            content = get_content(str(j.find('div')))
            zan = str(j.find_all('div')[-1].find_all('a')[-4].string[-2])
            zhuan = str(j.find_all('div')[-1].find_all('a')[-3].string[-2])
            ping = str(j.find_all('div')[-1].find_all('a')[-2].string[-2])
            other = str(j.find_all('div')[-1].find('span', class_='ct').string).split(" ")
            time1 = other[0] + " " + other[1]
            source = other[2]

            open(filename, 'a').write("a")
            open(filename, 'a').write(user_name + '\n' + user_http + '\n' + content + '\n' + zan + '\n' + zhuan + '\n' + ping + '\n' + time1 + '\n' + source + '\n' + '\n')

        except Exception:
            error_count += 1
            continue

    time.sleep(random.random())
    print("爬取第" + str(i) + "页已完成")

print("爬取" + str(start_page) + "-" + str(end_page) + '页已完成')
print("共产生" + str(error_count) + "处错误")





