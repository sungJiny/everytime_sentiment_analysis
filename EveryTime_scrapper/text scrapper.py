import re
import pandas as pd
from selenium import webdriver
import time

df = pd.read_excel('lecture_list.xlsx')
lecture_list = list(df['과목명'].unique())

url_list = []
for i in range(len(lecture_list)):

    driver.get('https://everytime.kr/lecture/search/'+str(lecture_list[i]))
    time.sleep(3)
    list_ = driver.find_elements_by_class_name('lecture')
    for i in range(len(list_)):
        url_list.append(list_[i].get_attribute('href'))

lecture_result = []
for x in a:
    driver.get(x)
    time.sleep(3)
    tmp = driver.find_elements_by_class_name('text')
    star = driver.find_elements_by_class_name('on')

    for i in range(len(star)-1):
        res = driver.find_elements_by_class_name('text')[i].text
        st = star[i + 1].get_attribute('style')
        star_res = pat.sub("", st)

        if res != '':
            lecture_result.append([res, star_res])
