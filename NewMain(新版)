#目前这是个半成品 访问量小情况下可用 验证码问题有待解决
#目前懒得弄验证码 稍后我用ddddOCR搞一搞就能用了

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

#=========请自行修改以下信息，以便登陆学信网===============
global xxnumber
global xxpassword
xxnumber = '17777777777' #手机号
xxpassword = 'xxxxxxxxxx' #密码
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
        wd.get('https://account.chsi.com.cn/passport/login?entrytype=yzgr&service=https%3A%2F%2Fyz.chsi.com.cn%2Fj_spring_cas_security_check')
        element = wd.find_element(By.CSS_SELECTOR,'#username')
        element.send_keys(xxnumber)
        element = wd.find_element(By.CSS_SELECTOR, '#password')
        element.send_keys(xxpassword)
        element = wd.find_element(By.CSS_SELECTOR, '#fm1 > div.yz-pc-loginbtn > input.yz_btn_login')
        element.click()

        #进入查询界面
        wd.get('https://yz.chsi.com.cn/apply/cjcxa/')

        #切换窗口
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
            if '全国硕士研究生招生考试部分考生初试成绩查询系统' in wd.title:
                break

        #设置延时
        numberrad = random.randint(1, 5)
        time.sleep(numberrad)
        time.sleep(3)

        #采集信息
        element2 = wd.find_element(By.TAG_NAME, 'body').text
        if ('无查询结果' not in element2):
            print(time.strftime("======查询结果时间：%Y-%m-%d-%H_%M_%S======", time.localtime()))
            print(wd.find_element(By.CSS_SELECTOR,'#app > div.cjcx-box').text)
            print("======以上信息是可能查到成绩信息======")
            print(" ")
        i += 1

if __name__ == '__main__':
    while True:
        try:
            python_program()
        except:
            continue
