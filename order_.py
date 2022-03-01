from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

# get exe file path
driver = webdriver.Chrome('C:/Users/klay1/chromedriver')
# get url
driver.get('https://my.min-fx.tv/login?service=https%3A%2F%2Fmy.min-fx.tv%2Fmypage%2Fj_spring_cas_security_check%3Ftarget-path%3D%2Findex')
# input ID,PASS
texts = driver.find_element_by_name('username')
texts.send_keys('klay.11.kc@gmail.com')
texts = driver.find_element_by_name('password')
texts.send_keys('AdGj1357')
# click login button
btn = driver.find_element_by_id('memberlogin')
btn.click()
sleep(4)
# click "FX" button
btn = driver.find_element_by_id('dropdownSTrelease')
btn.click()
# click "Webトレーダー" button
btn = driver.find_element_by_link_text('Webトレーダー')
btn.click()
# click "IFD" button
btn = driver.find_elements_by_class_name('ember-view')
btn[104].click()
btn = driver.find_elements_by_class_name('ember-power-select-selected-item')
btn[4].click()
btn = driver.find_elements_by_class_name('text-symbol-label')
#select = Select(element)
btn[4].click()
texts = driver.find_elements_by_class_name('form-control')
# pre order
texts[1].send_keys(75.34)
texts[2].send_keys(80.43)
texts[3].send_keys(74.12)