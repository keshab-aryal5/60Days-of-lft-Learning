empire_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
import requests
from bs4 import BeautifulSoup
response = requests.get(url=empire_url)
soup = BeautifulSoup(response.text,"html.parser")
movie_list = soup.find_all("h3",class_="title")
movie = [movie.getText() for movie in movie_list]

with open("movie.txt","w",encoding="UTF-8") as file:
    for x in range(len(movie)-1,-1,-1):
        file.write(movie[x])
        file.write("\n")
