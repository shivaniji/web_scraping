import requests
import json
from bs4 import BeautifulSoup
def scrape_top_list(movieurl):
    # movies_url="https://www.rottentomatoes.com//m/toy_story_4"
    page=requests.get(movieurl)
  
    soup=BeautifulSoup(page.text,"html.parser")
  
    li=soup.find_all("li",class_="meta-row clearfix")
    name=soup.find("h1",class_="scoreboard__title").get_text()
  
    dict={}
    for i in li:
        k=i.text
        n=k.split()
        # print(n)
        for j in n:
            if "Rating" in j:
                dict["Name"]=name
                dict["Rating"]=n[1]
                # print(dict)
            if "Genre" in j:
                a=n[1:]
                n=""
                for i in a:
                    n+=i
                n=n.split(",")
                dict["Genre"]=n
            if "Language" in j:
                dict["Language"]=n[2:] 
            if "Director" in j:
                a=n[1:]
                n=""
                for i in a:
                    n+=i
                n=n.split(",")
                dict["Drector"]=n
                # print(dict)
            if "Producer:" in j:
                a=n[1:]
                n=""
                for i in a:
                    n+=i
                n=n.split(",")
                dict["Producer"]=n
                # print(dict)
            if "Writer:" in j:
                a=n[1:]
                n=""
                for i in a:
                    n+=i
                n=n.split(",")
                dict["Writer"]=n
                # print(dict)
            if "Release " in j:
                a=n[1:]
                n=""
                for i in a:
                    n+=i
                n=n.split(",")
                dict["Release"]=n

            if "Runtime:"in j:
                time=n[1:]
                i=0
                while i<len(time):
                    hour=time[0][0]
                    # print(time)
                    mint=time[1]
                    min=mint[:-1]
                    # print(min)
                    i=i+1
                tom=int(hour)*60+int(min)
                dict["Runtime"]=tom
    # print(dict)
    with open("task4,json","w")as file:
        json.dump(dict,file,indent=4)
        return dict


scrape_top_list("https://www.rottentomatoes.com//m/toy_story_4")















































    