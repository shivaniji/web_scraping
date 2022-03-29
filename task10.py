import requests
import json

with open("task5.json","r+")as file:
    detail=json.load(file)
def analyse_language_directors():
    b={}
    v=[]
    for i in detail:
        for j in i["Drector"]:
            if j not in v:
                v.append(j)
    for k in v:
        b1={}
        for l in detail:
            if k in l["Drector"]:
                if "Language" in l:
                    g=l["Language"]
                    for j in g:
                        if j not in b1:
                            b1[j]=1
                        else:
                            b1[j]+=1
            b[k]=b1
    with open("task10.json","w+")as file10:
        json.dump(b,file10,indent=6)

analyse_language_directors() 




