#此版本本人在试验中，未必能用，只是提供思路

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

#=========请自行修改以下信息，以便能查四级成绩==============
global xxnumber
global xxpassword
xxnumber = '17777777777' #姓名
xxpassword = 'xxxxxxxxxx' #证件号码/准考证号
#===============请自行修改以上信息======================

def python_program():  # 将主程序放在此函数下
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    #wd = webdriver.Chrome(chrome_options=option) #如果想要无界面运行，取消本行注释并注释掉下一行
    wd = webdriver.Chrome() #如果想要有界面运行，取消本行注释并注释掉上一行
    print("=====================================")
    print('系统已经启动了，正在查询中，有消息会在控制台通知您')
    print("=====================================")
    i = 1

    while True:
        #学信网登陆
        wd.get('http://cet.neea.edu.cn/html1/folder/21045/4870-1.htm')
        element = wd.find_element(By.CSS_SELECTOR,'#xm')
        element.send_keys(xxnumber)
        element = wd.find_element(By.CSS_SELECTOR, '#no')
        element.send_keys(xxpassword)
        element = wd.find_element(By.CSS_SELECTOR, '#submitButton')
        element.click()

        #进入查询界面
        #wd.get('https://yz.chsi.com.cn/apply/cjcxa/')

        #切换窗口
        #for handle in wd.window_handles:
         #   wd.switch_to.window(handle)
          #  if '全国硕士研究生招生考试部分考生初试成绩查询系统' in wd.title:
           #     break

        #设置延时
        numberrad = random.randint(1, 3)
        time.sleep(numberrad)
        time.sleep(2)

        #采集信息
        element2 = wd.find_element(By.CSS_SELECTOR,'#Content1 > div.schrep').text
        if (element2.strip()!=''):
            print(time.strftime("======查询结果时间：%Y-%m-%d-%H_%M_%S======", time.localtime()))
            print(element2)
            print("======以上信息是可能查到成绩信息======")
            print(" ")




        i += 1

if __name__ == '__main__':
    while True:
        try:
            python_program()
        except:
            continue
