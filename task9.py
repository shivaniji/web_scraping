import requests
import os
import time
import random
from task1 import scrape_top
movies=scrape_top ()
def scrape_movie_details(a):
    for i in movies:
        # print(i)
        path="/home/admin123/Desktop/web_scraping/task9/"+i["Name"]+".text"
        random_sleep = random.randint(1,5)
        if os.path.exists(path):
            pass
        else:
            time.sleep(random_sleep)
            create=open(path,"w+")
            url=requests.get(i["moveurl"])
            create.write(url.text)
            create.close()
scrape_movie_details(movies)

