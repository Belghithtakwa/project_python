import requests
from bs4 import BeautifulSoup
import re

file= open("main.html", "w")
file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style.css">
    <title>jobs list</title>
</head>
<body>''')

jobTitle=input("Entrez le nom du job recherché : ")
ville=input("Entrez la ville : ")
url ='http://localhost:3000/database'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    
response = requests.get(f'https://www.jobijoba.com/fr/query/?what={jobTitle}&where={ville}-departement&where_type=department')
file.write(f'''<h1 class="title"> Liste des offres </h1>''')
file.write(f'''<div>''')

if response is not None:
 html = BeautifulSoup(response.content, 'html.parser')

 results = html.find_all("div", class_="content")
 for result in results:
     location = result.find("span", class_="new_feature")
     description = result.find("div", class_="c_text_secondary description")
     date = result.find("span", class_="publication_date recent")
     title = result.find("span", class_="c_link_annonces")
     title = re.sub('^null|$','', str(title))
     date = re.sub('^null|$','', str(date))
     description = re.sub('^null|$','', str(description))
     requests.post(url, {"title": " ".join(title.split()),"date": " ".join(date.split()),"description": " ".join(description.split())}, headers)
     file.write(f'''<div class="parag">
 <h5 class="titleJob" >title job: {title} </h5>
<li><span class="des" > La date de l'annonce :</span>{date}</li>  
<li><span class="des" > lieu du travail :</span> {location}</li>
<span class="des" >L'annonce : </span> <br>
<p>{description}</p>
</div>
</div>''')

file.write('''
</body>
</html>''')