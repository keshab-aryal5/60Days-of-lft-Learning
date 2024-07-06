import requests
from bs4 import BeautifulSoup
url = "https://timesofindia.indiatimes.com/"

response = requests.get(url)
print(response.status_code)

with open("rough.html","w",encoding="UTF-8") as thml:
    thml.write(response.text)
