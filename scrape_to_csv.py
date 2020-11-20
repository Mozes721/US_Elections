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

# driver = webdriver.PhantomJS('/home/mozes721/Documents/chromedriver')
# driver.add_argument('--headless')


#URL of website
driver.get('https://www.politico.com/2020-election/results/president/')


#print(driver.page_source)

wait = WebDriverWait(driver, 10)
state_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div/div/div[5]')))
state_btn.click()
time.sleep(5)
#state_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME ,'mui-popper jsx-644046148')))

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




def state_scrape(link_set):
    pass

    

# magic_link(state_link)


def states_links(state_result):
    # link = http.request('GET', state_result)
    # link_page =link.data.decode('utf-8')
    # link_soup = BeautifulSoup(link_page, 'html.parser')
    # state = link_soup.find('h1', {'id': 'us-election-2020-state-results'}).text.strip().split(' ')[0]
    browser.get(state_result)
    
    browser.refresh()
    
    table = browser.find_elements_by_id("us-election-2020-state-results")
    print(table.innerHTML)

# first_link = link_set[0]   

#states_links(first_link)

