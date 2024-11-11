import requests
from bs4 import BeautifulSoup
import csv
import os
import urllib.parse

# 发送请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

def request_soup(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'  # 设置编码
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print("请求失败，状态码：", response.status_code)
        return None


def name_user_count(url):
    soup = request_soup(url)
    forums = soup.select('.ba_info')  # 选择器可能需要调整
     # 提取每个分类的名称和用户数量
    for forum in forums:
        name = forum.select_one('.ba_name').get_text(strip=True)  # 分类名称
        user_count = forum.select_one('.ba_m_num').get_text(strip=True)  #用户数量
        ba_p_num = forum.select_one('.ba_p_num').get_text(strip=True)  #帖子数量
        write_to_csv([[name,user_count,ba_p_num]]) 
        print(f"分类名称: {name}, 用户数量: {user_count} 用户数量: {user_count}" )


def run_user_count_pagination_links(url):
    """获取分页链接"""
    soup = request_soup(url)
    # 获取分页链接
    for link in soup.select('.pagination a'):  # 替换为实际选择器
        href = link.get('href')
        if href:
            full_url = urllib.parse.urljoin(url, href)
            print(f"写入数据: {full_url}")
            name_user_count(full_url)


def forumclass_link():
    url = "https://tieba.baidu.com/f/index/forumclass"
    soup = request_soup(url)
    # 找到分类链接的元素并提取 href 属性
    right_sec = soup.find(id="right-sec")
    if right_sec:
        for link in right_sec.find_all('a'):
            href = link.get('href')
            if href:
                full_url = urllib.parse.urljoin("https://tieba.baidu.com/", href)
                print(f"采集: {full_url}")
                run_user_count_pagination_links(full_url)


# data = [['分类1', '1000'], ['分类2', '2000']]
# write_to_csv(data)
def write_to_csv(data, csv_file='baidu.csv'):
    """将抓取的数据写入 CSV 文件"""
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入数据
        writer.writerows(data)
    print(f"数据已追加写入 {csv_file}")

if __name__ == "__main__":
    forumclass_link()
