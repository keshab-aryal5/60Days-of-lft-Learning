import requests
from bs4 import BeautifulSoup

goldstar = "https://www.goldstarshoes.com/products/category/1/men"

response = requests.get("https://www.goldstarshoes.com/products/category/1/men").text

soup = BeautifulSoup(response,"lxml")

tags = soup.select("div.product-item div.st-cont2")
print(len(tags))
for x in tags:
    details = x.find("div", class_="st-cont2")
    details = x.find("div",class_="st-cont2 st-cont Dfx flxWrp tMb-0 tMt-0 mPt-5 mPb-5 TxAl-m sfCol_100 TxAl-c Pt-10 Pb-0 Pl-20 Pr-20 tPl-10 tPr-10 tPt-0 tPb-0 mPl-10 mPr-10")
    print(details)
    print("Inside")
    name = x.find('a').string
    print(name)
    details = x.find("a",class_="st-cont2 st-cont Dfx flxWrp tMb-0 tMt-0 mPt-5 mPb-5 TxAl-m sfCol_100 TxAl-c Pt-10 Pb-0 Pl-20 Pr-20 tPl-10 tPr-10 tPt-0 tPb-0 mPl-10 mPr-10")
    print(details)
    print(type(details))
    title = details.find('a').getText
    link = details.get("href")
    print(title)
    print(link)
    print("hi")
    break

