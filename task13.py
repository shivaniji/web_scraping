import json
from task4 import scrape_top_list
from task12 import scrape_movie_cast

def scrape_movie_details(url):
    list=[]
    a=scrape_top_list(url)
    b=scrape_movie_cast(url)
    list.append(a)
    list.append(b)
    with open("task13.json","w")as file:
        json.dump(list,file,indent=4)
    return list
scrape_movie_details("https://www.rottentomatoes.com/m/toy_story_4")
