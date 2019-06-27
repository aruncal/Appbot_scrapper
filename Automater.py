


def downl_reviews(name,driver):
    try:
        while True:
            try:
        
                driver.find_element_by_xpath("//*[@id=\"ma-add-source-btn\"]").click()
                #add new source
                break
            except:
                sleep(1)




        while True:
            try:
        
                driver.find_element_by_xpath("//*[@id=\"sources-root\"]/div/div[2]/div/div/div[1]/div[2]/a[1]").click()
        #clicks google play
        
                break
            except:
                sleep(1)

        while True:
            try:
        
                app_name=driver.find_element_by_id("search_field")
        
                break
            except:
                sleep(1)

        app_name.send_keys(name)
        driver.find_element_by_xpath("//*[@id=\"searchbutton\"]/input").click()


        while True:
            try:
        
                driver.find_element_by_xpath("//*[@id=\"step2\"]/table/tbody/tr[1]/td[3]/form/button").click()
                break
            except:
                sleep(1)


        while True:
            try:
        
                driver.find_element_by_xpath("//*[@id=\"myapps-mount-point\"]/div/div[1]/div[2]/div[2]/div[3]/div/h3/a").click()
                break
            except:
                sleep(1)
        while True:
            try:
        
                driver.find_element_by_xpath("//*[@id=\"b-filter\"]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
                break
            except:
                sleep(1)
        
        elems=driver.find_elements_by_tag_name('li')
        #elems = driver.find_elements_by_xpath("/html/body/div[25]/div/div/div[1]/ul")

        elems[37].click()





       
        while True:
            try:
                export=driver.find_element_by_xpath("//*[@id=\"review-list\"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/button").click()
                                                     #//*[@id="review-list"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/button
                break
            except:
                sleep(1)
        sleep(2)
        elems=driver.find_elements_by_tag_name('li')

        elems[30].click()
        sleep(3)
        manage=driver.find_element_by_xpath("/html/body/nav/div[2]/a[2]").click()
        while True:
            try:
                delete=driver.find_element_by_xpath("//*[@id=\"myapps-mount-point\"]/div/div[1]/div[2]/div[2]/div[7]/button").click()
                break
            except:
                sleep(1)
    
        sleep(2)
        obj = driver.switch_to.alert
        obj.accept()
        driver.refresh()
        done.append(name)
    except:
        error.append(name)
        
    import json

    with open('done.json', 'w') as f:
        json.dump(done, f)
        
#---------------main-------------
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup, Comment
import pandas as pd


import json
chrome_options = webdriver.ChromeOptions() 
import time
start_time = time.time()
# elsewhere...


appids=[]#fill this list with App ids 
driver = webdriver.Chrome(executable_path=r"chromedriver.exe") #have your chromedriver.exe on the same directory of your code file

link = "https://app.appbot.co/myapps"
driver.get(link)
driver.maximize_window()
email = driver.find_element_by_id("user_email")
pwd = driver.find_element_by_id("user_password")
email.send_keys()#enter your Appbot registered emailid 
pwd.send_keys()#enter your Appbot registered password

driver.find_element_by_xpath("//*[@id=\"new_user\"]/input[3]").click()


i=0
d=0
for name in appids:
    i+=1
    if name not in done:
        downl_reviews(name,driver)
        d+=1
        print("done,  "+name+" , appno:  "+str(d))
        print("----------- %s seconds -------------" % (time.time() - start_time))
        
