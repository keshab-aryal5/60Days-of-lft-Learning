from bs4 import BeautifulSoup
import requests

unfamiliar_skills = input("Enter your unfamiliar skills: ")
print(f"Filitering out {unfamiliar_skills}")
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=&cboWorkExp1=0').text
soup = BeautifulSoup(html_text,"lxml")
tags = soup.find_all("li" ,class_="clearfix job-bx wht-shd-bx")
for x in tags:
    text = x.find("span",class_="sim-posted").get_text()
    if 'few' in text:
        skills = x.find("span",class_="srp-skills").text.strip()
        if unfamiliar_skills not in skills:
            title = x.h2.a.text.strip()
            company = x.find("h3",class_="joblist-comp-name").text.strip()
            link = x.h2.a["href"]
            with open("job.txt","a") as jobs:
                jobs.write(f"Title: {title}\n\n")
                jobs.write(f"Skills: {skills}\n\n")
                jobs.write(f"Company name: {company}\n\n")
                jobs.write(f"Link: {link}\n\n")
                jobs.write("\n\n")
                