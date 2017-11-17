# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:39:03 2017

@author: Prof.J
"""
import re
import requests


class Spider:
    def __init__(self):
        self.session = requests.Session()
    
    def run(self,start_url):
        img_ids = self.get_img_item_ids(start_url)
        for img_id in img_ids:
            img_item_info = self.get_img_item_info(img_id)
            exit()
            
    #根据套图id获取套图信息，拼接出一个url,有个无奈的选择
    def get_img_item_info(self,img_id):
        img_item_url =  "http://photo.hupu.com/nba/" + img_id + ".html"
        response = self.download(img_item_url)
        if response:
            data = response.text
            print(data)
        
    #返回套图id列表    
    def get_img_item_ids(self,start_url):
        response = self.download(start_url)
        if response:
            html = response.text
            ids = re.findall(r'/nba/(\w+).html',html)
            return set(ids)
        
        
    # 下载器    
    def download(self,url):
        try:        
            return self.session.get(url)
        except Exception as e:
            print(e)
        

if __name__ == '__main__':
    spider = Spider()
    start_url = 'http://photo.hupu.com/nba/tag/%E7%A7%91%E6%AF%94'
    spider.run(start_url)
