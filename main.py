from bs4 import BeautifulSoup
import requests
import os

def download_images(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
    print("Download completed.")

# Replace with the URL of the website you want to download images from
url = "https://www.vexels.com/vectors/preview/70405/classic-style-vintage-floral-pattern"
# Replace with the name of the folder you want to store images in
folder = "images"
download_images(url, folder)
