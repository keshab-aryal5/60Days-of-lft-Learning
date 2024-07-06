import requests
from bs4 import BeautifulSoup

with open("sample.html") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,"lxml")

print(soup.prettify())
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
# for child in soup.find(class_="container"):
#     print(child)

# cont = soup.find(class_="container")
# print(cont.name)
# cont.name = "keshab"
# print(cont.name)
# cont["class"] = "myclass class2"
# cont.string = "I am a string"
# print(cont)

# prepare

# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# soup.html.body.insert(-1,ulTag)
# with open("modified.html","w")as f:
#     f.write(str(soup))
    

# cont = soup.find(class_="container")
# print(cont.has_attr("contenteditable"))

# def has_class_but_no_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# print(soup.find_all(has_class_but_no_id))

