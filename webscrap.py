import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4

response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 

maison_du_monde = response.text 
data = BeautifulSoup(maison_du_monde,"html.parser") #permet de récupérer la data de ma page sous forme HTML 

#print(data.prettify()) #comme le pprint 

carpet_name = []
carpet_name_list = []

title_name = data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

for k, item in enumerate(title_name):
    title = item.getText()
    carpet_name.append(title)
    carpet_name_list.append(carpet_name[k])

print(carpet_name_list)


