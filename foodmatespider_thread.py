import requests
import time
from selenium import webdriver
from lxml import etree
import re
import json
from threading import Thread
from queue import Queue
import time

foodCookies="""bc08_f0d8_saltkey=uuq9LkLA; bc08_f0d8_lastvisit=1551947293; __gads=ID=36afa0d9ea99e902:T=1551950895:S=ALNI_MbW5qKiQpVxrAz3ARaIA2REwh2OKw; PHPSESSID=d464178523f046163facd1dd08b331a0; bc08_f0d8_lastact=1551966321%09api.php%09js; Hm_lvt_2aeaa32e7cee3cfa6e2848083235da9f=1551950892; Hm_lpvt_2aeaa32e7cee3cfa6e2848083235da9f=1551967142; __tins__2070176=%7B%22sid%22%3A%201551967128901%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201551968942083%7D; __51cke__=; __51laig__=29"""
f_cookies={i.split("=")[0]:i.split("=")[1] for i in foodCookies.split("; ")}


def retry(func):
    """添加功能，获取网页时等待一段时间后获取不到，重复尝试获取，次数共三次，如果还是获取不到，则有可能网络不佳"""
    def wrapper(*args, **kwargs):
        try_times = 0
        while try_times < 3:
            try:
                func(*args, **kwargs)
                break
            except:
                try_times = try_times + 1
                continue

    return wrapper

class foodmatespider():
    """改成多线程"""
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.start_url="http://db.foodmate.net/yingyang"
        self.url_list=[]
        self.get_detail_url_list_queue=Queue()  # 创建队列，在线程间传递数据
        self.get_content_queue=Queue()
        self.save_content_queue=Queue()

    @retry
    def get_url_list(self,html_str):
        """获取食品种类url"""
        html=etree.HTML(html_str)
        a_list=html.xpath("//div[@id='top']/a")
        for a in a_list:
            href=self.start_url+"/"+a.xpath("./@href")[0]
            kind_name=a.xpath("./text()")[0]  # 大类名
            self.url_list.append((href,kind_name))  # 通过元祖传递url以及大类名

    @retry
    def get_detail_url_list(self,driver):
        """获取食品种类下的各个食品的url"""
        while True:
            url,kind_name=self.get_detail_url_list_queue.get()
            print(url)
            driver.get(url)
            time.sleep(3)
            html_str=driver.page_source    # 用driever的page_source获取html内容
            print(html_str)
            html=etree.HTML(html_str)         # etree.HTML转化为Html对象
            detail_url_elements=html.xpath("//div[@id='dibu']/li/a")   # 通过xpath方式获取元素以及数据，返回列表
            for detail_url in detail_url_elements:
                href=self.start_url+"/"+detail_url.xpath("./@href")[0]  # 获取url地址
                self.get_content_queue.put((href,kind_name))
            self.get_detail_url_list_queue.task_done()


    @retry
    def get_content(self,driver):
        """获取食品营养数据"""
        while True:
            url,kind_name=self.get_content_queue.get()
            driver.get(url)
            time.sleep(3)
            html_str=driver.page_source
            html=etree.HTML(html_str)
            detail_dict={}
            nutrition_data=[]
            content_div=html.xpath("//div[@id='rightlist']")[0]
            print(etree.tostring(content_div).decode())
            name=content_div.xpath("./center/font/b/text()")[0]
            for div in content_div.xpath(".//div[@class='list']"):
                data_dict={}
                div_str=etree.tostring(div,encoding="utf-8")
                div_str=div_str.decode()
                print(div_str)
                ret=re.match(r"<div class=\"list\"><div class=\"list_m\">(.*?)</div>(.*?)</div>",div_str)
                nutrition_name=ret.group(1)
                nutrition_number=ret.group(2)
                data_dict[nutrition_name]=nutrition_number
                nutrition_data.append(data_dict)
            detail_dict['name']=name
            detail_dict['data']=nutrition_data
            self.save_content_queue.put((detail_dict,kind_name))
            self.get_content_queue.task_done()


    def save_content(self):
        """保存数据"""
        while True:
            detail_dict,kind_name=self.save_content_queue.get()
            filename=kind_name
            with open("data/%s"%filename,'a',encoding="utf-8") as f:
                f.write(json.dumps(detail_dict,ensure_ascii=False))
                f.write("\n")
            self.save_content_queue.task_done()


    def run(self):
        self.driver.get(self.start_url)
        print("ok")
        html_str=self.driver.page_source
        self.driver.quit()
        self.get_url_list(html_str)
        for url in self.url_list:
            self.get_detail_url_list_queue.put(url)

        driver_list=[]
        for i in range(5):
            #创建5个driver对象，5个线程访问网页
            driver_list.append(webdriver.Chrome())

        t_detail=Thread(target=self.get_detail_url_list,args=(driver_list[0],))
        t_get_content1=Thread(target=self.get_content,args=(driver_list[1],))
        t_get_content2=Thread(target=self.get_content,args=(driver_list[2],))
        t_get_content3=Thread(target=self.get_content,args=(driver_list[3],))
        t_get_content4=Thread(target=self.get_content,args=(driver_list[4],))
        # 两个线程保存数据
        t_save_content1=Thread(target=self.save_content)
        t_save_content2=Thread(target=self.save_content)

        thread_list=[t_detail,t_get_content1,t_get_content2,t_get_content3,t_get_content4,t_save_content1,t_save_content2]
        queue_list = [self.get_detail_url_list_queue, self.get_content_queue, self.save_content_queue]
        for t in thread_list:
            t.setDaemon(True)  # 设置为守护进程
            t.start()

        for q in queue_list:
            # 队列阻塞
            q.join()

        for d in driver_list:
            # 退出浏览器
            d.quit()


if __name__=="__main__":
    t1=time.time()
    f=foodmatespider()
    f.run()
    t2=time.time()
    print(t2-t1)
    #print(f_cookies)
    #print(type(f_cookies))

    #driver=webdriver.Chrome()
    #driver.add_cookie({'a':'a','b':'b'})
    #print(driver.get_cookies())



