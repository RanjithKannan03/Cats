from bs4 import BeautifulSoup
import requests

response=requests.get("https://unsplash.com/s/photos/domestic-cat")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_cat_image_tags=soup.select('.MorZF img')
cat_images=[]
for img in all_cat_image_tags:
    cat_images.append(img['src'])

response=requests.get("https://unsplash.com/s/photos/animal")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_animal_image_tags=soup.select('.MorZF img')
animal_images=[]
for img in all_animal_image_tags:
    animal_images.append(img['src'])

