# coding:utf-8
import requests
from bs4 import BeautifulSoup
import threading
from multiprocessing import Pool
import time


def get_zhaopin(page):
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=python&sm=0&p={0}'.format(page)
    print("第{0}页".format(page))
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata,'lxml')
    job_name = soup.select("table.newlist > tr > td.zwmc > div > a")
    salarys = soup.select("table.newlist > tr > td.zwyx")
    locations = soup.select("table.newlist > tr > td.gzdd")
    times = soup.select("table.newlist > tr > td.gxsj > span")
    for name, salary, location, time in zip(job_name, salarys, locations, times):
        data = {
            'name': name.get_text().strip(),
            'salary': salary.get_text(),
            'location': location.get_text(),
            'time': time.get_text(),
        }
        print(data)
if __name__ == '__main__':
    starttime = time.time()
    pool = Pool(processes=8)
    pool.map_async(get_zhaopin, range(1, 519 + 1))
    pool.close()
    pool.join()
    print(time.time()-starttime)