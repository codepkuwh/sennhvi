import jieba
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread

# 读取文本
lyric = ''
with open('page.txt', 'r', encoding='utf-8') as f:
    lyric = f.readlines()
# 分词
result = jieba.lcut(str(lyric))
# 已空格拼接形成一个字符串
keywords = ' '.join(result)
print(keywords)
# 读取图片
image = imread('timg.jpg')
# 实例化词云
wc = WordCloud(background_color='White', max_words=50, mask=image)
# 绘制词云
wc.generate(keywords)
# 收集原图色彩
image_color = ImageColorGenerator(image)
# 使用原图色彩着色词云
wc.recolor(color_func=image_color)
# 保存图像
wc.to_file('output.png')
