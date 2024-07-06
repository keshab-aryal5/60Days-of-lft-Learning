import requests
from bs4 import BeautifulSoup


with open("sample.html") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,"lxml")
# print(soup.prettify())
prices = soup.find_all("span",class_="a-price-whole")
prices.pop(0)
prices.pop(0)
prices.pop(0)

tag = soup.find_all("span",class_="a-size-medium")
tag.pop(0)

for x in range(len(tag)):
    print(tag[x].string)
    print(prices[x].string)