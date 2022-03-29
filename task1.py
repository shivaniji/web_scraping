import json 
import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
# print(soup)
def scrape_top():
    main=soup.find("div" , class_="panel-body content_body allow-overflow")
    table=main.find("table" ,class_= "table")
    trs=table.find_all("tr")
    # print(trs)
    l=[]
    for i in trs:
        td =i.find_all("td")
        # print(td)
        dict={}
        for j in td:
            rank=i.find("td" ,class_="bold").get_text()[:-1]
            dict["Rank"]=int(rank)

            rating=i.find("span", class_="tMeterScore").get_text()[1:3]
            dict["Rating"]=float(rating)

            name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dict["Name"]=name
            # print(name)

            reviews=i.find("td" ,class_="right hidden-xs").get_text()
            dict["Reviews"]=int(reviews)
            # print(reviews)

            year=i.find("a",class_="unstyled articleLink").get_text()
            year=year.strip()
            dict["Year"]=int (year[-5:-1])
            # print(year)


            moveurl=i .find("a",class_="unstyled articleLink")["href"]
            link=("https://www.rottentomatoes.com/")+moveurl
            dict["moveurl"]=link

            # print(moveurl)

         
        l.append(dict)
    if {} in l:
        l.remove({})

    with open("task1.json","w")as f:
        json.dump(l,f,indent=4)
    return l
           
movie_details=scrape_top()