import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/New-Apple-iPhone-Mini-128GB/product-reviews/B08L5VN68Y/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
code = requests.get(url)

soup = BeautifulSoup(code.content,'html.parser')
print(soup.prettify())

names = soup.select('span.a-profile-name')[2:]

titles = soup.select('a.review-title span')
titles

dates = soup.select('span.review-date')[2:]

stars = soup.select('i.review-rating span.a-icon-alt')[2:]

reviews = soup.select('span.review-text-content span')

cust_name = []
rev_date = []
ratings = []
rev_title = []
rev_content = []
for i in range(len(names)):
  cust_name.append(names[i].get_text())
  rev_date.append(dates[i].get_text().replace("Reviewed in India on ",""))
  ratings.append(stars[i].get_text())
  rev_title.append(titles[i].get_text())
  rev_content.append(reviews[i].get_text().strip("\n "))

import pandas as pd

df = pd.DataFrame()
df['Customer Name'] = cust_name
df['Date'] = rev_date
df['Ratings'] = ratings
df['Review Title'] = rev_title
df['Reviews'] = rev_content

df.to_csv("amazon.csv")

cust_name = []
rev_date = []
ratings = []
rev_title = []
rev_content = []
for page in range(1,35):
  url = "https://www.amazon.in/New-Apple-iPhone-Mini-128GB/product-reviews/B08L5VN68Y/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(page)
  code = requests.get(url)
  if str(code) == "<Response [200]>":
    soup = BeautifulSoup(code.content,'html.parser')
    names = soup.select('span.a-profile-name')[2:]
    titles = soup.select('a.review-title span')
    dates = soup.select('span.review-date')[2:]
    stars = soup.select('i.review-rating span.a-icon-alt')[2:]
    reviews = soup.select('span.review-text-content span')
    for i in range(len(names)):
      cust_name.append(names[i].get_text())
      rev_date.append(dates[i].get_text().replace("Reviewed in India on ",""))
      ratings.append(stars[i].get_text())
      rev_title.append(titles[i].get_text())
      rev_content.append(reviews[i].get_text().strip("\n "))

str(code) == "<Response [200]>"

df = pd.DataFrame()
df['Customer Name'] = cust_name
df['Date'] = rev_date
df['Ratings'] = ratings
df['Review Title'] = rev_title
df['Reviews'] = rev_content

