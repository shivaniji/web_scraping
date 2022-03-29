from email.mime import image
import json
import requests
from bs4 import BeautifulSoup
def scrape_movie_cast(url):
    re=requests.get(url)
    soup=BeautifulSoup(re.text,"html.parser")
    main_div=soup.find('div',class_='castSection')
    div=main_div.find_all("div",class_="cast-item media inlineBlock")
    div2=main_div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    # print(div2)
    list=[]
    for i in div:
        # print(i)
        di={}
        cast=i.find("a")["href"][11:]
        # print(cast)
        di["Name"]=cast
        list.append(di)
        # print(list)
    for i in div2:
        # print(i)
        div3={}
        cast1=i.find("a")["href"][11:]
        # print(cast1)
        div3["Name"]=cast1
        list.append(div3)
        print(list)
    with open("task12.json","w")as file:
        json.dump(list,file,indent=4)
    return list
scrape_movie_cast("https://www.rottentomatoes.com/m/toy_story_4")



#         dict1={}
#     # for i in div:
#     cast=i.find("a")["href"][11:]
# #         dict1["Name"]=cast
#         list.append(dict
# scrape_movie_cast("https://www.rottentomatoes.com/m/toy_story_4")