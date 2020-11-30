from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json



driver = webdriver.Chrome('/home/mozes721/Desktop/chromedriver')
#URL of website
driver.get('https://www.politico.com/2020-election/results/president/')

#make webdriver wait for elements to be rendered in the page so they would be tracable
wait = WebDriverWait(driver, 10)
state_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div/div/div[5]')))
state_btn.click()
time.sleep(5)

#states list
state_list = driver.find_element_by_xpath('//*[@id="find-your-state-menu"]')

#get the state names from the ul list 
link_set = []
for list in state_list.find_elements_by_tag_name('li'):
    link_set.append(list.text)

#list comprehension to change array format
link_set = [each_string.lower().replace('.', '').replace(',', '').replace(' ', '-') for each_string in link_set]

#get the state urls
state_urls = []
for link in link_set:
    state_urls.append('https://www.politico.com/2020-election/results/' + link + '/')
time.sleep(5)

#get the state names
state_names = []
for state in link_set:
    state_names.append(state)

#create a list for result storage
trump_result_list = []
biden_result_list = []

def scrape_results(link_set):
    #get table
    table = link_set.find_element_by_xpath('//*[@id="__next"]/div[5]/div[1]/div/div[1]/div[1]/div[2]/table/tbody')
    #get two rows
    row1 = table.find_element_by_xpath('./tr[1]')
    row2 = table.find_element_by_xpath('./tr[2]')
    #votes and percentage from rows
    list_values1 = row1.find_elements_by_tag_name('td')
    list_values2 = row2.find_elements_by_tag_name('td')
    #get row name
    row1_name = row1.find_element_by_xpath('./td[1]/div[1]')

    #assign the row to the proper canditate
    if row1_name.get_property('innerHTML') == 'Joe Biden':
        biden_results(list_values1)
        trump_results(list_values2)
    else:
        biden_results(list_values2)
        trump_results(list_values1)



#get the state and vote results for the candiate and add it to a dictionary and append to the list
def trump_results(list):     
    state = state_name.title()          
    votes = list[1].text 
    percent = list[2].text
    print("Trump had %s votes and %s percentage in %s state elections " % (votes, percent, state))
    state_results = {}
    state_results['state'] = state
    state_results['votes'] = votes 
    state_results['percent'] = percent  
    trump_result_list.append(state_results)

    
def biden_results(list):
    state = state_name.title() 
    votes = list[1].text 
    percent = list[2].text
    print("Biden had %s votes and %s percentage in %s state elections " % (votes, percent, state))
    state_results = {}
    state_results['state'] = state
    state_results['votes'] = votes 
    state_results['percent'] = percent  
    biden_result_list.append(state_results)
   

#iterate through 5 as a test run
# five_states_urls = state_urls[:5]
# five_state_names = state_names[:5]

#run the state name and url simultaniously to recive all required values
for state_name, state_url in  zip(state_names, state_urls):
    #open new webriver on each url iteration to scrape the table values
    states_driver = webdriver.Chrome('/home/mozes721/Desktop/chromedriver')
    states_driver.get(state_url)
    scrape_results(states_driver)

#save to json file
with open('trump_results.json', 'w') as trump_file:
        json.dump(trump_result_list, trump_file)

with open('biden_results.json', 'w') as biden_file:
        json.dump(biden_result_list, biden_file)
