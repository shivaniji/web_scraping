import json
import requests
import os
from task1 import scrape_top
movies=scrape_top ()
def scrape_movie_details(a):
    for i in movies:
        # print(i)
        path="/home/admin123/Desktop/web_scraping/task8/"+i["Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w+")
            url=requests.get(i["moveurl"])
            create.write(url.text)
            create.close()
scrape_movie_details(movies)