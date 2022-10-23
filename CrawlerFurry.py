from pickle import NONE
import re
from datetime import datetime
from os import error
from urllib import request, error
import ssl
import time
import json
ssl._create_default_https_context = ssl._create_unverified_context
def crawler_furry():
    try:
        state_code = 0
        resp = request.urlopen("https://bot.hifurry.cn/everyfurry?date=today")
        json_data = json.loads(resp.read().decode("utf-8"))
        
        #爬取状态代码
        state_code = json_data['StateCode']
        
        #爬取图片作者name
        write_name = json_data['AuthorName']
        # print(write_name)
        
        #爬取图片简介
        pic_text = json_data['WorkInformation']
        #print(pic_text)
        
        #print("okk")
        # 原动态链接
        source_link = json_data['SourceLink'] 
        #爬取图片url
        pic_url = json_data['PictureUrl']

        
        #编辑消息内容
        msg_one = "嗷呜，{}月{}日兽兽推送".format(time.strftime("%m", time.localtime()), time.strftime("%d", time.localtime()))
        msg_two = "来源：{}\n简介：{}\n原文链接：{}\n详情：https://furry.lihouse.xyz/index.php?ftime={}".format(write_name, pic_text, source_link, time.strftime("%Y%m%d", time.localtime()))
        #print(msg_two)
        
        today_fur_dic = {'StateCode': state_code, 'Date': time.strftime("%Y%m%d", time.localtime()), 'PictureUrl': pic_url, 'AuthorName': write_name, 'WorkInformation': pic_text, 'SourceLink': source_link}
        return [time.strftime("%Y%m%d", time.localtime()), msg_one, msg_two, pic_url, state_code,  today_fur_dic]

    except:
        today_fur_json = {"StateCode": 0, "Date": "", "PictureUrl": "", "AuthorName": "", "WorkInformation": ""}
        today_fur_json = json.dumps(today_fur_json, ensure_ascii=False)
        print("error")
        if state_code != 1:
            #编辑消息内容
            msg_one = None
            msg_two = msg_one
            pic_url = None
            today_fur_dic = today_fur_json
        state_code = 0
        pic_url = None
        return [time.strftime("%Y%m%d", time.localtime()), msg_one, msg_two, pic_url, state_code, today_fur_dic]

        
