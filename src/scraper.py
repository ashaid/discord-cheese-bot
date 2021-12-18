import requests
import bs4 as bs
import urllib
import re


url = "http://www.nourishinteractive.com/healthy-living/free-nutrition-articles/110-list-cheeses"
result = requests.get(url)
soup = bs.BeautifulSoup(result.content, 'html.parser')

print(soup.string)





