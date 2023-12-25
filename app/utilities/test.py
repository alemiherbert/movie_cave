from tmdbv3api import TMDb
from tmdbv3api import Movie, Search
import json
import re

def clean_movie_title(title):
    # Replace dots with spaces
    title_without_dots = title.replace('.', ' ')

    # Remove everything after and including '480p', '720p', or '1080p'
    cleaned_title = re.sub(r'\s*480p.*$|\s*720p.*$|\s*1080p.*$', '', title_without_dots)

    return cleaned_title.strip()

def get_movie_poster_url(title):
    tmdb = TMDb()
    tmdb.api_key = 'b89c31ea2c0f88622172bf5eadf42ea5'  # Replace with your TMDb API key

    search = Search()
    search_results = search.movies(title)
    print(search_results)
    if search_results['results']:
        print(search_results)
        first_result = search_results['results'][0]
        movie = Movie()
        # details = movie.details(first_result['id'])
        poster_url = f'https://image.tmdb.org/t/p/w400{first_result["poster_path"]}'
        return [poster_url, first_result]
    else:
        return ['','']

def process_data(input_data):
    output_data = []

    for entry in input_data[:20]:
        title = entry["data"]["title"]
        title = clean_movie_title(title)
        poster_url = get_movie_poster_url(title)
        print(poster_url)

        entry["data"]["image"] = poster_url[0]
        # entry
        output_data.append(entry)

    return output_data

# Example usage:
# (Make sure to replace 'your_tmdb_api_key' with your actual TMDb API key)


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
