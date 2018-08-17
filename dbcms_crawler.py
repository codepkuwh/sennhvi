import requests
from bs4 import BeautifulSoup


# 爬取影评
def get_comment():
    comments = ''
    url = 'https://movie.douban.com/subject/25845910/reviews?start=0'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # 提取影评
    ret = soup.find_all(attrs='short-content')
    for comment in ret:
        comments += comment.contents[0]
    return comments


print(get_comment())
