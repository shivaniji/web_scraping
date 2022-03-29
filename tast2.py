
import json
from  task1 import  scrape_top_list
# year=scrape_top_list()
file=open("task1.json","r")
date= json.load(file)
def moves():
    d1={}
    for i in date:
        l=[]
        year=i["Year"]
        # print(year)
        if year  not in d1:
            for key in date:
                if year==key["Year"]:
                    l.append(key)
            d1[year]=l
    # print(d1)
    with open("tast2.json","w+")as file:
        json .dump( d1,file,indent=4)
        # a=json.dumps(d1)
        return d1
moves()










