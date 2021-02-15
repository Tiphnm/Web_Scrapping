import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4
import logging 

response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 
maison_du_monde = response.text 
data = BeautifulSoup(maison_du_monde,"html.parser") #permet de récupérer la data de ma page sous forme HTML 

logging.basicConfig(filename='loggings.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an error:')


class Carpet: 
    def __init__(self):
        self.carpet_name_list = []
        self.carpet_price_list = []
        self.final_carpet = []

    def name_carpet(self):
        logging.info('Getting my carpets name from HTML into a list: start')
        carpet_name = []
        title_name = data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        for k, item in enumerate(title_name):
            title = item.getText()
            carpet_name.append(title)
            self.carpet_name_list.append(carpet_name[k])
        logging.info('Getting my carpets name from HTML into a list: end')

        #return self.carpet_name_list

    def price_carpet(self):
        logging.info('Getting my carpets price from HTML into a list: start')
        carpet_price = []
        price_text = data.find_all("div", class_="ml-auto font-weight-semibold price")

        for k, item in enumerate(price_text): 
            price = item.getText()
            carpet_price.append(price)
            self.carpet_price_list.append(carpet_price[k].split()[0])
        logging.info('Getting my carpets price from HTML into a list: end')

        #return self.carpet_price_list
     
    
    def zip_list(self): 
        logging.info('Zipping all my lists in tuple: start')

        result= zip(self.carpet_name_list, self.carpet_price_list)
        #print("This is my result:" , result)
        self.final_carpet = set(result)
        #print(self.final_carpet)
        logging.info('Zipping all my lists in tuple: end')

        #return self.final_carpet




c = Carpet()
#c.name_carpet()
#c.price_carpet()
#c.zip_list()
