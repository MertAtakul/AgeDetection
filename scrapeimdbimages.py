import os
import requests
from bs4 import BeautifulSoup

count = 0

def download_images(url, save_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    lister_list = soup.find("div", class_="lister-list")
    image_elements = lister_list.findAll("img")
    global count

    if not os.path.exists(save_path):
        os.makedirs(save_path)


    for img_element in image_elements:
        img_url = img_element["src"]
        response = requests.get(img_url)
        file_name = f"image_{count+1}.jpg"

        with open(os.path.join(save_path, file_name), "wb") as f:
            f.write(response.content)

        count += 1

base_url = "https://www.imdb.com/list/ls023573954/?sort=list_order,asc&mode=grid&page="
save_path = "C:\\Users\\pc\\Desktop\\AI_Project\\images\\old"

for i in range(1, 6):
    url = base_url + str(i)
    print(f"Downloading images from page {i}")
    download_images(url, save_path)

print("All images have been downloaded.")