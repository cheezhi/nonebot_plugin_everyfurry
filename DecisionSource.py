import time
from .CrawlerFurry import crawler_furry
import os
path = os.path.split(os.path.realpath(__file__))[0]
img_msg_file = path + '/today_furry_msg.txt'

def decision():
    with open(img_msg_file,'r',encoding='UTF-8') as f: 
        file_text = f.read()

    if len(eval(file_text)) == 0:
        print('无缓存，正在爬虫获取')
        file_text = crawler_furry()
        with open(img_msg_file,'w',encoding='UTF-8') as f:
            f.write(str(file_text))
    else:
        file_text = eval(file_text)
    old_time = file_text[0]
    new_time = time.strftime("%Y%m%d", time.localtime())

    if old_time != new_time or file_text[4] == 0:
        print('缓存信息为旧，正在启动爬虫')
        new_file_text = crawler_furry()
        with open(img_msg_file,'w',encoding='UTF-8') as f:
            f.write(str(new_file_text))
        return new_file_text
    else:
        print('已找到匹配缓存')
        print(file_text)
        print(file_text[4])
        return file_text