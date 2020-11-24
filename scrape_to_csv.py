from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
#work headless without opening a browser
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  , chrome_options=options
driver = webdriver.Chrome('/home/mozes721/Desktop/chromedriver')
#states_driver = webdriver.Chrome('/home/mozes721/Desktop/chromedriver')

# driver = webdriver.PhantomJS('/home/mozes721/Documents/chromedriver')
# driver.add_argument('--headless')


#URL of website
driver.get('https://www.politico.com/2020-election/results/president/')


#print(driver.page_source)

wait = WebDriverWait(driver, 10)
state_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div/div/div[5]')))
state_btn.click()
time.sleep(5)

state_list = driver.find_element_by_xpath('//*[@id="find-your-state-menu"]')

#get the state names from the ul list 
link_set = []
for list in state_list.find_elements_by_tag_name('li'):
    link_set.append(list.text)

#list comprehension to change array format
link_set = [each_string.lower().replace('.', '').replace(',', '').replace(' ', '-') for each_string in link_set]

state_urls = []
for link in link_set:
    state_urls.append('https://www.politico.com/2020-election/results/' + link + '/')
time.sleep(5)




def scrape_results(link_set):
    trump_list = []
    biden_list = []

    table = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody')

    first_row_name = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div[1]')
    second_row_name = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div[1]')

    #first row votes and percent                      
    #first_row_votes = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[2]')
    #first_row_percent = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[1]')
    
    #second row votes and percent
    #second_row_votes = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]')
    #second_row_percent = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]')
    #get td row values of each canditate                 //*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]

    #get two rows
    row1 = table.find_element_by_xpath('./tr[1]')
    row2 = table.find_element_by_xpath('./tr[2]')

    list_values1 = row1.find_elements_by_tag_name('td')
    list_values2 = row2.find_elements_by_tag_name('td')
    #get row name
    row1_name = row1.find_element_by_xpath('./td[1]/div[1]')
    # row2_name = row2.find_element_by_xpath('.//td[1]/div[1]')

    #row1_votes = row1.find_element_by_xpath('./td[2]/div[2]')
    #row1_percentage = row1.find_element_by_xpath('./td[2]/div[1]')

    if row1_name.get_property('innerHTML') == 'Joe Biden':
        biden_results(list_values1)
        trump_results(list_values2)
    else:
        biden_results(list_values2)
        trump_results(list_values1)




def trump_results(list):               
    votes = list[1].text 
    percent = list[2].text
    print("Trumps votes %s and precentage %s" % (votes, percent))
    
def biden_results(list):
    votes = list[1].text 
    percent = list[2].text
    print("Biden votes %s and precentage %s" % (votes, percent))


while True:
    states_driver = webdriver.Chrome('/home/mozes721/Desktop/chromedriver')
    states_driver.get(state_urls[1])
    break


scrape_results(states_driver)


