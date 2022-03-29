import json
with open("task5.json","r")as file:
    movies_genre=json.load(file)
    # print(movies_genre)
def analyse_movies_genre():
    dict2={}
    for i in movies_genre:
        if "Genre"in i:
            k=i["Genre"]
        for i in k:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
    with open("task11.json","w")as file:
        json. dump(dict2,file,indent=4)
analyse_movies_genre()
