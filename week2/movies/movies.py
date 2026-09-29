import json
import os
import requests

with open("data/tspdt_movies.json", encoding="utf-8") as file:
    films = json.load(file)

# for key in films:
#     print(key)

films_list = films["movies"]

# print(f"первый элемент из списка фильмов: {films_list[0]}")

#---------------------------------------------------------------

os.makedirs("week2/movies/posters", exist_ok=True)

def file_name(film):
    title = ""
    for char in film["title_clean"].lower():
        if char.isalnum(): # если буква или цифра (alphanumerical)
            title += char
        elif char == " ":
            title += "_"
    rank = str(film["rank"]).zfill(4)

    return rank + "_" + title + "_" + str(film["year"]) + ".jpg"


first_film = films_list[687]
correct_name = file_name(first_film)
print(correct_name)

for film in films_list:
    path = "week2/movies/posters/" + file_name(film)
    if os.path.exists(path):
        continue

    response = requests.get(film["image_url"])
    if response.status_code == 200:
        with open(path, "wb") as file:
            file.write(response.content)
        print(path)
    else:
        print(f"неудача... {path}, {response.status_code}")




print("Hello world")