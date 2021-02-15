from db import * 

############# Webscrapping de mes infos depuis Maison du Monde: infos sur les Tapis 
c.name_carpet()
c.price_carpet()
c.zip_list_carpet()

############# Création de ma table avec les infos de mon webscrapping 
t.erase_table()
t.create_table()
t.insert_info()