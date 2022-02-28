from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

# get exe file path
driver = webdriver.Chrome('C:/Users/klay1/chromedriver')
# get url
driver.get('https://sec.himawari-group.co.jp/report/chart/')
# choice interval
dropdown = driver.find_element_by_name('candle_term')
select = Select(dropdown)
select.select_by_value('_ti')
sleep(4)
# choice currency pair
dropdown = driver.find_element_by_name('currency_pair')
select = Select(dropdown)
list_curency = ['USDJPY','EURJPY','GBPJPY','AUDJPY','NZDJPY','CADJPY','CHFJPY','AUDUSD','EURUSD','GBPUSD','NZDUSD']
for i in list_curency:
    select.select_by_value(i)
    # click keep button
    btn = driver.find_element_by_css_selector('.csv_download.btn.btn-lg.center-block')
    btn.click()
    # sleep 8seconds
    sleep(8)
# quit system
driver.quit()