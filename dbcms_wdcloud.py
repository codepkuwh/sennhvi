import requests
from bs4 import BeautifulSoup
import jieba.analyse
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread


# 爬取影评，豆瓣只允许爬取200条影评
def get_comment(count=10):
    page = 0
    page2 = 25
    limit = 20
    comment = ''
    for i in range(count):
        # 如果是第二页,page=25
        if i == 1:
            page = page2
        url = 'https://movie.douban.com/subject/25845910/comments?start=' \
              + str(page) + '&limit=20&sort=new_score&status=P'
        response = requests.get(url)
        # print(response.text)
        # response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        # 提取影评
        for j in range(limit):
            css = '#comments > div:nth-of-type' + \
                  '(' + str(j + 1) + ')' + '> div.comment > p > span.short'
            info = soup.select(css)
            print("info 0", info[0])
            try:
                comment += str(info[0].string)
            except Exception as e:
                print(e)
                print(info[0])
        # 下一页
        page += limit

    return comment


# 主程序
def main():
    # 读取文本
    txt = get_comment()
    # 分词
    result = jieba.analyse.textrank(str(txt), topK=50, withWeight=True)
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]
    print(keywords)
    # 打开图片
    image = imread('timg.jpg')
    # 实例化词云
    wc = WordCloud(font_path='simhei.ttf', background_color='White',max_words=50,mask=image)
    # 绘制词云
    # wc.generate(keywords)
    wc.generate_from_frequencies(keywords)
    # 收集原图色彩
    image_color = ImageColorGenerator(image)
    # 使用原图色彩着色词云
    wc.recolor(color_func=image_color)
    # 保存图像
    wc.to_file('door.png')


main()
