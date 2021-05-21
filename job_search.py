# coding=utf-8

import sys 
import os 
import logging
from selenium import webdriver
import time
import bs4
import requests
import re
from selenium.webdriver.common.keys import Keys


# Create logger
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='logs_are_here.txt', level=logging.DEBUG, format=FORMAT)


class FirsScrape:
    

    def __init__(self, address="https://www.jobmaster.co.il/jobs/?ezor=38&l=%D7%97%D7%99%D7%A4%D7%94"):
        self.address = address

    def scraping_to_file(self):
        res = requests.get(self.address)
        text_to_regex = res.text.encode('utf-8')
        print(type(text_to_regex))
        # the id of each element starts with misra, example:id="misra7292039"
        regex_for_misra = re.compile('misra\d+')
        global catch_pattern
        catch_pattern = regex_for_misra.findall(text_to_regex)
        print(catch_pattern)

    def open_browser(self):
        global browser
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get(self.address)
        browser.execute_script("window.scroll(0,300)")

    def click_on_jobs(self,item=0):
        jobs_on_the_page = browser.find_element_by_xpath("//div[@class='misrotList']/article[@id='{}']".format(catch_pattern[item]))
        actions = webdriver.ActionChains(browser)
        actions.click(jobs_on_the_page)
        actions.perform()
        time.sleep(1)

    def apply_for_jobs(self):
        time.sleep(2)
        file_for_job = browser.find_element_by_xpath("//div[@class='jobHead__actionBtn__jobContact']/input[@class='bttn blue full']")
        actions = webdriver.ActionChains(browser)
        actions.click(file_for_job)
        actions.perform()
        time.sleep(1)

# class="body_lock"
# <input class="LoginInput round2" name="pemail" type="email" dir="ltr" value="" placeholder="" autofocus="">


# need to check for if statement
    def if_form(self):
        try:
            input_to_email = browser.find_element_by_xpath("//div[@class='LoginPlaceHolder Mail']/input")
            input_to_password = browser.find_element_by_xpath("//div[@class='LoginPlaceHolder Pass']/input")
            submit_of_form = browser.find_element_by_xpath("//div[@class='LoginPlaceHolder CustomCheck']/input[@class='bttn blue SignInBttn']")
            actions = webdriver.ActionChains(browser)
            actions.click(input_to_email)
            actions.send_keys('xxxxxxxx')
            actions.click(input_to_password)
            actions.send_keys('xxxxxxxxx')
            actions.click(submit_of_form)
            actions.perform()    
            print(input_to_email)
        except Exception:
            try:
                error_fix = browser.find_element_by_xpath("//div[@id='modal_content']/input[@class='bttn']")
                actions = webdriver.ActionChains(browser)
                actions.click(error_fix)
                actions.perform()
                time.sleep(2)
            except:
                try:
                    select_dont_leave_the_site = browser.find_element_by_xpath("//div[@id='modal_content']/div[@id='buttons']/input[@class='bttn']")
                    actions = webdriver.ActionChains(browser)
                    actions.click(select_dont_leave_the_site)
                    actions.perform()
                except:
                    pass


    def send_cv(self):
        browser.execute_script("window.document.getElementById('modal_window').scroll(0,200)")
      #  global input_to_cv_application
        try:
            time.sleep(2)
            select_dont_leave_the_site = browser.find_element_by_xpath("//div[@id='modal_content']/div[@id='buttons']/input[@class='bttn']")
            actions = webdriver.ActionChains(browser)
            actions.click(select_dont_leave_the_site)
            actions.perform()
        except:
            pass
        
        try:
            time.sleep(2)
            select_father_resume = browser.find_element_by_xpath("//div[@id='CVRadioPlaceHolder']/label[@id='korotVersionNumLabel8088450']")
            actions = webdriver.ActionChains(browser)
            actions.click(select_father_resume)
            actions.perform()
        except:
            pass
        try:
            time.sleep(2)
            browser.execute_script("window.document.getElementById('modal_window').scroll(0,500)")
            select_from_options = browser.find_element_by_xpath("//div[@class='UpdateGroup FilterQuestions']/div[@class='UpdateElement']/select[@class='AnswerSelect InputFix']")
            exit_the_question = browser.find_element_by_xpath("//div[@id='buttons']/input[@class='bttn CancelButton']")
            actions = webdriver.ActionChains(browser)
            actions.click(exit_the_question)
            actions.perform()

        except Exception as e:
            print(e, "didn't work out")
            pass
        
        try:
            time.sleep(2)
            select_array_selector = browser.find_elements_by_class_name("AnswerSelect InputFix")[0]
            actions = webdriver.ActionChains(browser)
            actions.click(select_array_selector)
            actions.perform()
        except:
            pass


        try:
            input_to_cv_application = browser.find_element_by_xpath("//div[@id='buttons']/input[@class='bttn blue SaveButton WithCancel']")
            time.sleep(4)
        except Exception:
            time.sleep(4)
            try:
                error_fix = browser.find_element_by_xpath("//div[@class='Show']/div[@id='modal_title']/div[@id='modal_content']/input[@class='bttn']")
                actions = webdriver.ActionChains(browser)
                actions.click(error_fix)
                actions.perform()
            except Exception:
                pass

        try:
            error_fix = browser.find_element_by_xpath("//div[@id='modal_content']/input[@class='bttn']")
            actions = webdriver.ActionChains(browser)
            actions.click(error_fix)
            actions.perform()
        except Exception:
            pass

        try:
            similar_jobs = browser.find_element_by_xpath("//div[@class='MultiSendRadioPlaceHolder']/label[@for='isMultiSendN']")
            actions = webdriver.ActionChains(browser)
            actions.click(similar_jobs)
            actions.perform()
        except Exception:
            pass 
        try:
            actions = webdriver.ActionChains(browser)
            actions.click(input_to_cv_application)
            actions.perform()
        except Exception:
            pass



web_surf = FirsScrape()
web_surf.scraping_to_file()
web_surf.open_browser()
web_surf.click_on_jobs()
web_surf.apply_for_jobs()
web_surf.if_form()
web_surf.send_cv()



def next_page_click():
    time.sleep(3)
    nex_page_selector = browser.find_elements_by_class_name("paging")[-1]
    actions = webdriver.ActionChains(browser)
    actions.click(nex_page_selector)
    actions.perform()
    print('-' * 30)
    time.sleep(6)
    print(browser.current_url)
    time.sleep(2)
    webfing_surfing = FirsScrape(browser.current_url)
    webfing_surfing.scraping_to_file()


  # for item in nex_page_selector:
    #  print(item.text)
    


def kick_again():
    y_scroll = 300
    i = 1
#    browser.execute_script("window.scrollTo(0,600)")
    while i < len(catch_pattern):
        if y_scroll >= 1500:
            browser.execute_script("window.scrollTo(0,1650)")
        if y_scroll >= 1650:
            time.sleep(3)
            next_page_click()
            time.sleep(2)
            y_scroll = 300
            i = 1   
            continue
        browser.execute_script("window.scrollTo(0,{})".format(y_scroll))
        time.sleep(3)
        web_surf.click_on_jobs(i)
        time.sleep(3)
        try:
            web_surf.apply_for_jobs()
        except Exception:
            i += 1
            print(y_scroll)
            y_scroll += 170
            continue
        time.sleep(3)
        try:
            web_surf.if_form()
        except Exception:
            pass
        time.sleep(3)
        web_surf.send_cv()
        time.sleep(3)
#        browser.execute_script("window.scrollTo(0,{})".format(y_scroll))
        i += 1
        y_scroll += 170
        print(y_scroll)




#class Jobs:
#
#    firefox_options = webdriver.FirefoxOptions()
#    firefox_options.add_argument("--private")

#    def __init__(self,address='https://www.jobmaster.co.il/jobs/?l=%D7%A6%D7%A4%D7%95%D7%9F'):
#        self.address = address
#        
#    def free_choose(self):
#        global browser
#        browser = webdriver.Firefox(firefox_options=self.firefox_options)
#        browser.maximize_window()
#        browser.get(self.address)
#        inputEl = browser.find_element_by_css_selector("#SearchCategories")
#        time.sleep(4)
#        actions = webdriver.ActionChains(browser)
#        actions.click(inputEl)
#        after_free = actions.perform()


#web_surf = FirsScrape()
#web_surf.scraping_to_file()
#web_surf.open_browser()
#web_surf.click_on_jobs()
#web_surf.apply_for_jobs()
#web_surf.if_form()
#web_surf.send_cv()
kick_again()

#surfing_the_web = Jobs()
#surfing_the_web.free_choose()
