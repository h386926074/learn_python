from selenium import webdriver
import csv
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)


# 网易云音乐歌单第一页的url
url = 'https://music.163.com/#/discover/playlist/' \
      '?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

#用PhantomJS 接口创建一个selenium的 webdriver
driver = webdriver.PhantomJS()

#准备好存储歌单的csv 文件
csv_file = open('playlist.csv','w',newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题','播放数','链接'])

while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame('contentFrame')
    data = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')

    for i in range(len(data)):
        nb = data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0]) > 500:
            msk = data[i].find_element_by_css_selector('a.msk')
            writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])

    url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')

csv_file.close()
