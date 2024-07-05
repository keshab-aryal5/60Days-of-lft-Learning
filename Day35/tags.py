import requests
from bs4 import BeautifulSoup

with open("sample.html") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,"lxml")
# print(soup.prettify())
# print(soup.title)
# print(soup.title,type(soup.title),soup.title.string)
# print(soup.div)
# print(soup.a)
# print(soup.find_all('div')[0])

# for link in soup.find_all("a"):
    # print(link.get("href"))
    # print(link.string)

# s = soup.find(id="link3")
# print(s)
# print(soup.select("div.itallic"))
# print(soup.select("span#itallic"))
# print(soup.span.get("class"))

# print(soup.find(class_="itallic"))
for child in soup.find(class_="container"):
    print(child)