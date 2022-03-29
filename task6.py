import json
import requests
from bs4 import BeautifulSoup

with open("task5.json","r")as file:
    a=json.load(file)
    # print(a)
def get_movie_details():
    dict1={}
    for i in a:
        # print(i)
        if "Language" in i:
            d=i["Language"]
            # print(d)
        for i in d:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
                # print(dict1)
    with open("task6.json","w")as file:
        json.dump(dict1,file,indent=4)
    return dict1
get_movie_details()



