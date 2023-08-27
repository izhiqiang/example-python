import csv
import os
import time

from lxml import etree
import requests

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 251, 25)]

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
    'Connection': 'Keep-Alive',
}


def GetHtml(url):
    try:
        requests.packages.urllib3.disable_warnings()
        return requests.get(url, headers=headers, verify=False).text
    except:
        pass


# "https://book.douban.com/top250?start=0"
def BookDoubanStartOne(OneUrl):
    html = GetHtml(OneUrl)
    try:
        s = etree.HTML(html)
        books = s.xpath('//*[@id="content"]/div/div[1]/div/table')
        for div in books:
            name = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
            author = div.xpath('./tr/td[2]/p[1]/text()')[0]
            quote = div.xpath('./tr/td[2]/p[2]/span/text()')[0]

            # 需要处理的函数
            print(name, author, quote)

    except Exception as err:
        print(err)
        # pass



if __name__ == '__main__':
    for url in urls:
        BookDoubanStartOne("https://book.douban.com/top250?start=0")

