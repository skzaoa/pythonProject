# coding=utf-8
from selenium import webdriver
import time
from log import logging


def main():
    browser = webdriver.Chrome()
    # 将浏览器最大化显示
    browser.maximize_window()
    # 设置宽高
    browser.set_window_size(1400, 900)
    browser.get('https://www.baidu.com')

    # browser.find_element_by_id("kw").send_keys("selenium")
    # t1 = browser.find_element_by_tag_name("input").send_keys("selenium 1111")\

    # xpath: attributer （属性）
    # input 标签下 id =kw 的元素
    # browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

    # xpath: idRelative （id相关性）
    # 在/form/span/input 层级标签下有个 div 标签的 id=fm 的元素
    browser.find_element_by_xpath("//div[@class='s_form_wrapper soutu-env-nomac soutu-env-index']/form/span/input").send_keys("selenium")
    browser.find_element_by_id("su").click()

    logging.info(browser.title)
    # logging.info(t1)

    time.sleep(1)
    # 后退
    browser.back()
    time.sleep(1)
    # 前进
    browser.forward()
    time.sleep(1)
    
    browser.quit()


def read_emil(browser):
    browser.implicitly_wait(5)
    browser.find_element_by_xpath("//body/header/nav/div/ul/li[@title='收件箱']").click()

    browser.implicitly_wait(5)

    # class="tv0"  获取内容列表
    read_list = browser.find_elements_by_class_name('tv0')
    logging.info(type(read_list))
    for read in read_list:
        logging.info(read.text)  # 输出列表内容

    # 邮件标题
    read_list2 = browser.find_elements_by_xpath("//div[@class='tv0']/div[starts-with(@class,'rF0')]")
    list2_len = len(read_list2)
    logging.info(list2_len)
    for i in range(1, list2_len+1):
        logging.info(i)
        logging.info(type(i))
        read = browser.find_element_by_xpath("//div[@class='tv0']/div[starts-with(@class,'rF0')][{}]".format(i))
        logging.info('邮件标题：', read.text, type(read))
        read.click()

        # 切换到iframe架构中
        browser.implicitly_wait(5)
        frame1 = browser.find_element_by_class_name('oD0')
        logging.info(frame1.get_attribute("id"))

        browser.switch_to.frame(frame1)  # 把iframe赋值给frame1，然后传递给方法
        content = browser.find_element_by_xpath("//div[@class='netease_mail_readhtml']")  # 这是某个未读邮件的class
        logging.info('邮件内容：' + str(content.text))
        # 回到上一层架构：(多表单时，进入一个表单要切回上一层架构，在切入到另一个表单中)
        browser.switch_to.default_content()
        time.sleep(2)
        browser.find_element_by_xpath("//body/header/nav/div/ul/li[@title='收件箱']").click()
        browser.refresh()


def login(username, password):
    browser = webdriver.Chrome()
    browser.get("https://mail.163.com/")

    browser.implicitly_wait(5)
    ele = browser.find_elements_by_tag_name('iframe')
    logging.info(ele)
    for e in ele:
        logging.info(e)
        logging.info(e.get_attribute("id"))

    browser.switch_to.frame(ele[0].get_attribute("id"))
    browser.find_element_by_name("email").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_id("dologin").click()
    browser.implicitly_wait(5)

    browser.switch_to.default_content()
    name = browser.find_element_by_id("spnUid").text
    logging.info(name)

    if name[0:-8] == username:
        logging.info(u"登录成功")
        # 登录成功后获取cookie
        cookie = browser.get_cookies()
        read_emil(browser)
    else:
        logging.info(u"登录失败")

    # browser.find_element_by_link_text("退出").click()
    browser.find_element_by_id("spnUid").click()
    browser.find_element_by_id("_mail_component_72_72").click()
    time.sleep(3)
    browser.quit()


if __name__ == '__main__':
    # main()
    username = "sknull"
    password = "********"
    login(username, password)
