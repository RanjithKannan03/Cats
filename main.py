import io

from bs4 import BeautifulSoup
import requests
from PIL import Image

response=requests.get("https://unsplash.com/s/photos/domestic-cat")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_cat_image_tags=soup.select('.MorZF img')
i=1
for img in all_cat_image_tags:
    response=requests.get(img['src'])
    image=Image.open(io.BytesIO(response.content))
    image.save(f'cats/{i}.png')





response=requests.get("https://unsplash.com/s/photos/animal")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_animal_image_tags=soup.select('.MorZF img')
i=1
for img in all_animal_image_tags:
    response=requests.get(img['src'])
    image=Image.open(io.BytesIO(response.content))
    image.save(f'animals/{i}.png')

