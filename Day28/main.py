import requests
from bs4 import BeautifulSoup

url = "https://example.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())
print(soup.title)
print(soup.title.string)
first_article = soup.find('article')
all_articles = soup.find_all('article')
header = soup.header
footer = soup.footer
nav = soup.nav
first_paragraph = soup.p
all_paragraphs = soup.find_all('p')
first_link = soup.a
all_links = soup.find_all('a')
first_image = soup.img
all_images = soup.find_all('img')
meta_tags = soup.find_all('meta')
divs = soup.find_all('div')
spans = soup.find_all('span')
classes = [value for element in all_articles for value in element.get('class', [])]
ids = [element.get('id') for element in all_articles if element.get('id')]
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
texts = soup.get_text()
first_article_text = first_article.get_text()
article_attrs = first_article.attrs
article_children = list(first_article.children)
article_descendants = list(first_article.descendants)
article_strings = list(first_article.stripped_strings)
article_parents = list(first_article.parents)
next_sibling = first_article.find_next_sibling()
previous_sibling = first_article.find_previous_sibling()

for article in all_articles:
    title = article.find('h2').get_text()
    link = article.find('a')['href']
    print(f"Title: {title}, Link: {link}")
