import requests
import m3u8_To_MP4

search_param = input("Enter Search: ")

url = f"https://api.consumet.org/anime/gogoanime/{search_param}"

response = requests.get(url, params={})

data = response.json()

titles = [item["title"] for item in data["results"]]

for i, title in enumerate(titles):
    print(f"Title: {title}, Number: {i}")

selected_series = int(input("SELECT SERIES:  "))

series_to_watch = data["results"][selected_series]

response = requests.get(f"https://api.consumet.org/anime/gogoanime/info/{series_to_watch['id']}")

series_data = response.json()

print(series_data["description"])

episodeNumber = int(input(f"Total episodes:{series_data['totalEpisodes']} | which episode to download: "))
episodeId = series_data["episodes"][episodeNumber - 1]["id"]

response = requests.get(f"https://api.consumet.org/anime/gogoanime/watch/{episodeId}")
download_data = response.json()

for i, entry in enumerate(download_data["sources"]):
    print(f"{i}--{entry['quality']}")
quality_selected = int(input("Download in which Quality: "))

download_link = download_data["sources"][quality_selected]["url"]

m3u8_To_MP4.multithread_download(download_link)
