import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4

response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 
maison_du_monde = response.text 
data = BeautifulSoup(maison_du_monde,"html.parser") #permet de récupérer la data de ma page sous forme HTML 


class Carpet: 
    def __init__(self):
        self.carpet_name_list = []
        self.carpet_price_list = []
        self.final_carpet = []

    def name_carpet(self):
        carpet_name = []
        title_name = data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        for k, item in enumerate(title_name):
            title = item.getText()
            carpet_name.append(title)
            self.carpet_name_list.append(carpet_name[k])

        return self.carpet_name_list

    def price_carpet(self):
        carpet_price = []
        price_text = data.find_all("div", class_="ml-auto font-weight-semibold price")

        for k, item in enumerate(price_text): 
            price = item.getText()
            carpet_price.append(price)
            self.carpet_price_list.append(carpet_price[k].split()[0])

        return self.carpet_price_list
    
    def zip_list(self): 
        result= zip(self.carpet_name_list, self.carpet_price_list)
        self.final_carpet = set(result)
        return self.final_carpet

c = Carpet()
print(c.name_carpet())
print(c.price_carpet())
print(c.zip_list())
