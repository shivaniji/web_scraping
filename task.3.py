from task1 import movie_details
import json

def group_by_decade(movies):
    decade_year = []
    index = 0
    while index < len(movies):
        for key in movies[index]:
            if key == "Year":
                mod = movies[index][key]%10
                decade = movie_details[index][key]-mod
                decade_year.append(decade)
        index += 1

    decade_year.sort()
    movies_dic = {}
    i = 0
    while i < len(movies):
        dec = decade_year[i]+10
        year_list = []
        j = 0
        while j < len(decade_year):
            if movies[j]["Year"] > decade_year[i] and movies[j]["Year"] <dec:
                year_list.append(movies[j])
            movies_dic[decade_year[i]]=year_list
            j += 1
        i += 1
        
    with open("task3.json","w+") as year_info:
        json.dump(movies_dic, year_info,indent=4)
        return movies_dic
   
store=group_by_decade(movies=movie_details)