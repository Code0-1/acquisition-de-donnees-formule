'''fichier avec main loop'''
from json.decoder import JSONDecoder
import json
import os
import filter_data

path = os.path.abspath('main.py')[:-7]

# demande le fichier à filtrer
file = filter_data.get_file(path)

data = {}
# regarde si le fichier est déjà filtrer
'''peu importe l'erreur il va :
refiltrer tous les données du fichier'''
try:
    with open(path+file, 'r') as fich:
        data = json.loads(fich.read())
except:
    data = filter_data.file_to_data(path, file)

