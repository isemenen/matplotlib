import bs4
from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
from urllib.request import Request, urlopen
import requests
import lxml.html
import lxml.html.soupparser
import json

test_URL = 'https://www.sec.gov/Archives/edgar/data/728447/000095017022000601/evoa-20200930.htm'

def get_data(link):
    hdr = {'User-Agent': 'igor semenenko', 'From': 'igor.semenenko@acadiau.ca'}
    req = requests.get(link, headers=hdr)
    with open('file.txt', 'w') as file:
        file.write(req.text)
    # response_dict = req.text
    # print(response_dict)
    soup = BeautifulSoup(req.content, 'html.parser')
    #print(soup)
    # soup = bs4.BeautifulSoup(req.text, 'html.parser')
    # print(soup.prettify())
    print(soup.find_all(text=True))
get_data(test_URL)

