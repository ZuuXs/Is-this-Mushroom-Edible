import requests
import csv
from bs4 import BeautifulSoup

"""
def comestible(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            header = soup.find('div', class_='cat_link').find('a').text.strip().upper()
            if "POISONOUS" in header:
                return "P"
            elif "INEDIBLE" in header:
                return "I"
            elif "EDIBLE" in header:
                return "E"
            elif "SLIME" in header:
                return ""
            else:
                return ""
        else:
            return ""  
    except Exception as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return ""  

def color(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            profil = soup.find('div', class_='mprofile').find_all('p')
            if profil:
                colorElement = profil[0].find_all('a')
                if colorElement:
                    colors = []
                    for color in colorElement:
                        colors.append(color.text.strip())
                    return "-".join(colors)
                else:
                    return "Pas de couleurs trouvé"
            else:
                return "Profil untrouvable"
    except Exception as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return ""  

def shape(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            profil = soup.find('div', class_='mprofile').find_all('p')
            if profil:
                shapeElement = profil[1].find_all('a')
                if shapeElement:
                    shapes=[]
                    for shape in shapeElement:
                        shapes.append(shape.text.strip().replace(' ',''))
                    return '-'.join(shapes)
                else:
                    return "Pas de shape trouvé"
            else:
                return "Profil untrouvable"
    except Exception as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return ""  

def surface(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            profil = soup.find('div', class_='mprofile').find_all('p')
            if profil:
                surfaceElement = profil[2].find('a')
                if surfaceElement:
                    surfaces = []
                    for surface in surfaceElement:
                        surfaces.append(surface.text.strip().replace(' ',''))
                    return '-'.join(surfaces)
            else:
                return "Profil untrouvable"
    except Exception as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return ""  

"""
## pour l'optimisation on fait pas appel aux methodes précedentes car il parcours le site plusieurs fois par champignon
def csvPattern(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            ##TYPE
            comestible = soup.find('div', class_='cat_link').find('a').text.strip()
            comestible = comestible[0] if comestible.startswith(("P", "I", "E")) else ""

            ##PROFIL
            profil = soup.find('div', class_='mprofile').find_all('p')
            if profil:
                couleur = " "
                shape = " "
                surface = " "

                for element in profil:
                    label=element.find('strong').text.strip()
                    data=element.find_all('a')
                    if("Color:" in label):
                        ##COULEUR
                        couleur = "-".join([color.text.strip() for color in data])

                    elif("Shape:" in label):
                        ##SHAPE
                        shape = "-".join([shape.text.strip().replace('-','').replace(' ','') for shape in data])

                    elif("Surface:" in label):
                        ##SURFACE   
                        surface = '-'.join([surface.text.strip().replace('-','').replace(' ','') for surface in data])

                    else:
                        continue

            else:
                return " "
            
            return comestible+","+couleur+","+shape+","+surface
            
            
    except Exception as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return ""


def writeToCsv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file :
        writer = csv.writer(file)
        writer.writerow(["Edible", "Color", "Shape", "Surface"])  # Header
        for row in data:
            writer.writerow(row)


def getAllLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []
    content_div = soup.find("div", class_="content")
    c=0
    if content_div:
        for link in content_div.find_all('a'):
            href = link.get('href')
            if href and href.startswith('https://ultimate-mushroom.com/') and "action=" not in href :
                print(href)
                c+=1
                links.append(href)
    print (c)
    return links


# Main

url1 = "https://ultimate-mushroom.com/poisonous/103-abortiporus-biennis.html"    
url2 = "https://ultimate-mushroom.com/edible/1010-agaricus-albolutescens.html"
url3 = "https://ultimate-mushroom.com/inedible/452-byssonectria-terrestris.html"

"""
print(csvPattern(url1))
print(color(url2))
print(color(url3))
print(shape(url1))
print(shape(url2))
print(shape(url3))
"""


### Parsing all the mushrooms
urls = getAllLinks("https://ultimate-mushroom.com/mushroom-alphabet.html")
mushroom_data = []
i=0

for url in urls:
    print(i)
    details = csvPattern(url).split(",")
    if details:
        mushroom_data.append(details)
    i+=1


csv_file = "data/champignons.csv"
writeToCsv(csv_file,mushroom_data)

print(f"Data for {len(mushroom_data)} mushrooms written to {csv_file}.")

