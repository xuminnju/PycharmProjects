# coding:utf-8
import requests
from bs4 import BeautifulSoup
import threading
from multiprocessing import Pool


def get_shouji(page):
    url = 'https://search.jd.com/Search?keyword=三星手机&enc=utf-8&qrst=1&rt=1&stop=1&vt=3&bs=1&wq=三星手机&ev=exbrand_三星（SAMSUNG）%5E&page={0}'.format(2*page-1)
    print("第{0}页".format(page))
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata,'lxml')
    names = soup.select("div.p-name > a > em ")
    prices = soup.select("div.p-price > strong > i")
    for name, price in zip(names, prices):
        data = {
            'name': name.get_text().strip(),
            'price': price.get_text(),
        }
        print(data)
if __name__ == '__main__':
    for page in range(52):
        get_shouji(page)