#########################################################
##                                                     ## 
##  Submission by: John Christian Linaban              ##
##  Last updated: 07/30/24                             ##
##  For: Data Scraping Bootcamp: Virtuals Protocol     ##
##                                                     ##
#########################################################

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import re

urls = [
    'https://www.ranker.com/list/best-lady-tsunade-quotes/ranker-anime',
    'https://animemotivation.com/tsunade-quotes-naruto/',
    'https://www.quoteambition.com/tsunade-quotes/',
    'https://www.upgradingoneself.com/tsunade-quotes/',
]

def extract_ranker(soup):
    quotes = []
    try:
        divs = soup.find_all('div', class_='richText_container__Kvtj0')
        for div in divs:
            paragraphs = div.find_all('p')
            for p in paragraphs:
                quotes.append(p.text)
    except Exception as e:
        print(f"Error extracting from ranker: {e}")
    return quotes

def extract_animemotivation(soup):
    quotes = []
    try:
        blocks = soup.find_all('blockquote')
        for block in blocks:
            paragraphs = block.find_all('p')
            for p in paragraphs:
                quotes.append(p.text)
    except Exception as e:
        print(f"Error extracting from animemotivation: {e}")
    return quotes

def extract_quoteambition(soup):
    quotes = []
    try:
        h2 = soup.find_all('h2')
        for h in h2:
            for sibling in h.find_next_siblings():
                if sibling.name == 'h4':
                    break
                if sibling.name == 'p':
                    quotes.append(sibling.text)
    except Exception as e:
        print(f"Error extracting from quoteambition: {e}") 
    return quotes

def extract_upgradingoneself(soup):
    quotes = []
    try:
        div_up = soup.find('div', class_ = 'entry-content clear')
        h4 = div_up.find_all('h4')
        for h in h4:
            quotes.append(h.text)
    except Exception as e:
        print(f"Error extracting from upgradingoneself: {e}")
    return quotes

def extract_text_from_url(url):
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    if url == 'https://www.ranker.com/list/best-lady-tsunade-quotes/ranker-anime':
        return extract_ranker(soup)
    elif url == 'https://animemotivation.com/tsunade-quotes-naruto/':
        return extract_animemotivation(soup)
    elif url == 'https://www.quoteambition.com/tsunade-quotes/':
        return extract_quoteambition(soup)
    elif url == 'https://www.upgradingoneself.com/tsunade-quotes/':
        return extract_upgradingoneself(soup)
    return []

# Clean data
def data_cleaning(quotes):
    cleaned_quotes = []
    for quote in quotes:
        quote = re.sub(r'["“”]', '', quote)  # Remove quotation marks
        quote = re.sub(r'\d+\.\s*', '', quote)  # Remove numbers followed by a period
        cleaned_quotes.append(quote)
    return cleaned_quotes

# Collect quotes from all of the URLs
all_quotes = []
for u in urls:
    data = extract_text_from_url(u)
    if data:
        cleaned_data = data_cleaning(data)
        all_quotes.extend({'Quote': quote} for quote in cleaned_data)

# Create and save DataFrame
pd_quotes = pd.DataFrame(all_quotes)
pd_quotes.to_csv('tsunade_quotes.csv', index=False)

print(pd_quotes)
