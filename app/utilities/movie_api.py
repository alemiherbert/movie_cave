import imdb
import json
import re
import requests
from bs4 import BeautifulSoup

def clean_movie_title(title):
    # Replace dots with spaces
    title_without_dots = title.replace('.', ' ')

    # Remove everything after and including '480p', '720p', or '1080p'
    cleaned_title = re.sub(r'\s*480p.*$|\s*720p.*$|\s*1080p.*$', '', title_without_dots)

    return cleaned_title.strip()


def get_movie_info(title):
    ia = imdb.IMDb()
    movies = ia.search_movie(title)

    if movies:
        movie_id = movies[0].movieID
        movie = ia.get_movie(movie_id)
        access = imdb.IMDb()
        print(movie_id)
        mov = access.get_movie(movie_id)
        print(mov)

        datas = {
            "title": movie["title"],
            "image": "",
            "description": movie["plot outline"] if "plot outline" in movie else ""
        }
        print(datas)
        return  datas
    else:
        print("####################")
        return None

def process_data(input_data):
    output_data = []

    for entry in input_data:
        title = entry["data"]["title"]
        title = clean_movie_title(title)
        movie_info = get_movie_info(title)
        print(title)
        print(movie_info)

        if movie_info:

            entry["data"]["image"] = movie_info["image"]
            entry["data"]["description"] = movie_info["description"]
            output_data.append(entry)

    return output_data

def main():
    input_file = r"C:\Users\user\PycharmProjects\movie_cave\app\data\movies.json"
    output_file = "output_file.json"

    with open(input_file, "r") as file:
        data = json.load(file)

    processed_data = process_data(data)

    with open(output_file, "w") as file:
        json.dump(processed_data, file, indent=2)

if __name__ == "__main__":
    main()
