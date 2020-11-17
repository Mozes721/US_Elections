import urllib3
from bs4 import BeautifulSoup
from urllib3 import request
import urllib.request as urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
http = urllib3.PoolManager()
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.bbc.com/news/election/us2020/results'
main_page = http.request('GET', url)

soup = BeautifulSoup(main_page.data, 'html.parser')



states = soup.find_all('ul', {'class': 'css-kx7phl-StateList e193da113'})

for state in states:
    state_link = state.find_all('a')
    
link_set = []
def magic_link(link):
    for each_item in link:
        html_link = each_item.get('href')
        if (html_link is None):
            pass
        else:
            if(not (html_link.startswith('http') or html_link.startswith('https'))):
                link_set.append('https://www.bbc.com' + html_link)
            else:
                link_set.append(html_link)

magic_link(state_link)

# 51 states
electorial_results = {}


def states_links(state_result):
    link = driver.get(state_result)
    soup2 = BeautifulSoup(link, 'html.parser')
    state = soup2.find('h1', {'id': 'us-election-2020-state-results'}).text.strip().split(' ')[0]
    

    body = link.find('div', {'class': 'flex-item main-table'})
    print(body)
    # for table_row in body:
    #     print(table_row)
        # cells = table_row.find_all('th')
        # print(cells)

        # if len(cells) > 0:
        #     trump_votes = cells[2].text
        #     print(trump_votes + 'adssaddsa')
        #     print("Hello")
    # trump_rep = soup2.find('tr', {'class': 'rep'}).text
    # trump_votes = trump_rep.find('td', {'class': 'votes'})
    # trump_pct = trump_rep.find('td', {'class': 'ptc'})

    # biden_dem = soup2.find('tr', {'class': 'dem'})
    # biden_votes = biden_dem.find('td', {'class': 'votes'})
    # biden_pct = biden_dem.find('td', {'class': 'ptc'})

   

states_links(link_set[0])

