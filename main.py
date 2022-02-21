#需要修改带♀号注释的部分
#需要安装selenium、ddddocr库
#并下载最新版本chrome和Chrome浏览器驱动，并在Path环境变量配置好

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddddocr
import random


def python_program():  # 保证出现问题后循环执行 如遇到问题程序会自动重启
    option = webdriver.ChromeOptions()
    option.add_argument('headless')


    #wd = webdriver.Chrome(chrome_options=option) #如果想无界面运行，取消本行注释，并注释掉下一行
    wd = webdriver.Chrome() #有界面运行，默认

    i = 1

    while True:

        wd.get('https://yz.chsi.com.cn/apply/cjcx/t/10594.dhtml') # ♀ 此处10594处改成你们学校的相应代码

        numberrad = random.randint(3, 10)   #执行访问网站速度 默认3-10秒一个循环

        time.sleep(numberrad)

        element = wd.find_element(By.CSS_SELECTOR,
                                  '#app > div > form.ivu-form.ivu-form-label-right > div:nth-child(1) > div > div.large-input.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text > input')

        element.send_keys('XXX')    # ♀ 改成你名字

        element = wd.find_element(By.CSS_SELECTOR,
                                  '#app > div > form.ivu-form.ivu-form-label-right > div:nth-child(2) > div > div.large-input.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text > input')

        element.send_keys('222222222222222222') # ♀ 改成身份证号

        element = wd.find_element(By.CSS_SELECTOR,
                                  '#app > div > form.ivu-form.ivu-form-label-right > div:nth-child(3) > div > div.large-input.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text > input')

        element.send_keys('222222222222222') # ♀ 改成准考证号

        # 截图
        if i >= 6:
            time.sleep(1)
            ele = wd.find_element(By.XPATH, '//*[@id="app"]/div/form[2]/div[5]/div/div[2]/img')
            ele.screenshot('ele.png')
            # OCR
            ocr = ddddocr.DdddOcr()
            with open(r'ele.png', 'rb') as f:
                img_bytes = f.read()
            resss = ocr.classification(img_bytes)
            # 输入
            element = wd.find_element(By.CSS_SELECTOR,
                                      '#app > div > form.ivu-form.ivu-form-label-right > div:nth-child(5) > div > div.large-input.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text > input')

            element.send_keys(resss)

        if i < 6:
            element = wd.find_element(By.CSS_SELECTOR,
                                      '#app > div > form.ivu-form.ivu-form-label-right > div:nth-child(5) > div > button > span')

            element.click()
        if i >= 6:
            element = wd.find_element(By.CSS_SELECTOR,
                                      '#app > div > form.ivu-form.ivu-form-label-right > div:nth-child(6) > div > button')
            element.click()

        time.sleep(3)

        element2 = wd.find_element(By.TAG_NAME, 'body').text
        if ('无查询结果' not in element2):
            print(element2)
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            print("======可能查到成绩信息，并将截图同时保存在本文件夹下======")
            wd.save_screenshot('resultos' + str(numberpic) + '.png')
            numberpic = random.randint(23425, 67311)

        i += 1

if __name__ == '__main__':
    while True:
        try:
            python_program()
        except:
            continue
