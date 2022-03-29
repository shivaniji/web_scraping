# import requests
import json
from bs4 import BeautifulSoup
from task1 import scrape_top
from task4 import scrape_top_list
movies=scrape_top()

# print(movies)
def scrape_movie_details():
    d1=[]
    for i in movies:
        t=i["moveurl"]
        print(t)
        a=scrape_top_list(t)
        d1.append(a)
    print(d1)
    with open("task5.json","w+")as file:
        json.dump(d1,file,indent=4)
        # return d1
scrape_movie_details()
