import json
with open ("task5.json","r")as file:
    a=json.load(file)
    # print(a)
def analyse_movies_directors():
    dic={}
    for i in a:
        # print(i)
        if "Drector" in i:
            d=i["Drector"]
        for i in d:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
    with open("task7.json","w")as file:
        json.dump(dic,file,indent=4)
    return dic

analyse_movies_directors()



 