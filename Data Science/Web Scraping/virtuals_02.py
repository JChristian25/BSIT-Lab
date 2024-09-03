#########################################################
##                                                     ## 
##  Submission by: John Christian Linaban              ##
##  Last updated: 07/31/24                             ##
##  For: Data Scraping Bootcamp: Virtuals Protocol     ##
##    [ ACTIVITY #2]                                   ##
#########################################################

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import re

SCRAPING_PROJECT_NAME = 'Tsunade Facts'

urls = [
    'https://naruto.fandom.com/wiki/Tsunade',
    'https://hero.fandom.com/wiki/Tsunade',
    'https://www.ranker.com/list/things-you-didnt-know-about-tsunade-trivia/anna-lindwasser',
    'https://wiki.sportskeeda.com/naruto/tsunade',
]


facts = []

for url in urls:
    response = requests.get(url)
    print(response.status_code)
    html_raw = bs(response.text, 'lxml')

    if url == urls[0]:
        pass
        query = html_raw.find_all('p')
        for q in query:
            if not q.find('span', class_='headnote') and not q.find_parent('table') and not q.find_parent('figcaption'):
                text = q.text.strip()
                if text:
                    facts.append({'Fact': q.text.strip(), 'URL': url})
        

    elif url == urls[1]:
        pass
        query = html_raw.find_all('p')
        
        for q in query:
            if not q.find_parent('table') and not q.find_parent('aside') and not q.find_parent('div', class_='notifications-placeholder') and not q.find_parent('div', class_='pi-item') and q.name != 'h3' and q.get('class') != ['caption']:
                text = q.text.strip()
                if text:
                    facts.append({'Fact': q.text.strip(), 'URL': url})

    elif url == urls[2]:
        pass
        query = html_raw.find_all('p')

        for q in query:
            if not q.find_parent('div', class_='description_text__mzzMt'):
                text = q.text.strip()
                if text:
                    facts.append({'Fact': q.text.strip(), 'URL': url})

    else:
        pass
        query = html_raw.find_all('p')
        for q in query:
            text = q.text.strip()
            if text:  # Only append if the text is not empty
                facts.append({'Fact': text, 'URL': url})

scraped_facts = pd.DataFrame(facts)
scraped_facts.to_csv('tsunade_facts.csv', index=True)


print(scraped_facts)