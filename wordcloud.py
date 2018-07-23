# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:26:17 2018

@author: karim
"""
import nltk
from nltk.corpus import stopwords 
import string

from urllib import request

import requests
import bs4 as bs
import re

from selenium import webdriver 
browser = webdriver.Firefox()



from tinydb import TinyDB
db = TinyDB("myfile.json")

url = db.all()[4]['link']

def get_word_list(url):
    
    browser.get(url)
    #resp = requests.get(url, headers=headers)
    #soup = bs.BeautifulSoup(resp.text, "lxml")
    soup = browser.page_source(url)
    
    for script in soup(['script', 'style']):
        script.decompose()
        
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)
    text = re.sub("[0-9]|\*", "", text)
    stop = stopwords.words("english") + list(string.punctuation)
    final = [i for i in nltk.word_tokenize(text.lower()) if i not in stop and len(i) > 3]
    
    return final

full_list = []
for job in db.all():
    print (job["link"])
    full_list += get_word_list(job['link'])

fdist = nltk.FreqDist(final)
fdist.most_common(30)



nltk.word_tokenize(text)


import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() +"\\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get(url)

driver.page_source