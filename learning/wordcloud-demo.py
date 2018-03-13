"""输入txt文档和图片文件名，根据图片形状和颜色输出txt词云图"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

txt_name = input('输入文档名称：')
text = open(path.join(d, txt_name)).read()

pic_name = input('输入照片名称：')
coloring = np.array(Image.open(path.join(d, pic_name)))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=coloring,
               stopwords=stopwords)
wc.generate(text)

image_colors = ImageColorGenerator(coloring)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

plt.imshow(coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()