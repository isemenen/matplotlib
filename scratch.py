#process text file
from bs4 import BeautifulSoup
import requests

filename = 'filing_urls.txt'
#contents = []

headers = {'User-Agent': 'igor.semenenko@acadiau.ca', 'Accept-Encoding': 'gzip, deflate'}

sample_url = 'https://data.sec.gov/submissions/CIK0001318605.json'
webpage = requests.get(url=sample_url, headers=headers)
soup = BeautifulSoup(webpage.content, 'html.parser')
print(soup)

# with open(filename) as f:
#     lines = f.readlines()
# #print(contents)
#     i = 0
#     for link in lines:
#         webpage = requests.get(link, headers)
#         soup = BeautifulSoup(webpage.content, "html.parser")
#         print(soup)
#         i += 1
#         if i == 10:
#             break
