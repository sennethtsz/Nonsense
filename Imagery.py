from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os

run = True

def StartSearch():
    global run

    search = input("Search for:")

    if search == "stop":
        run = False
    else:
        params = {"q": search}
        dir_name = search.replace(" ", "_").lower()

        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

        r = requests.get("https://www.bing.com/images/search", params=params)

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.findAll("a", {"class": "thumb"})
        i = 1

        for item in links:
            try:
                img_obj = requests.get(item.attrs["href"])
                print("getting", item.attrs["href"])
                print("downloading", i, "picture/s")
                i = i + 1
                title = item.attrs["href"].split("/")[-1]

                try:
                    img = Image.open(BytesIO(img_obj.content))
                    img.save("./" + dir_name + "/" + title, img.format)
                except:
                    print("Could not save image.")

            except:
                print("Could not request Image")


while run:
    StartSearch()


