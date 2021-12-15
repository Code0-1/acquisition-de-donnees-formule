'''fichier avec main loop'''
import json
import os
import filter_data
import formule

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
    # filtre les datas
    for key in data.keys:
        formule.get_y_value(key, data)
    # save data after treatment
    filter_data.data_to_json(file, data)

# Commencer à afficher les graphiques
'''ne pas oublier
repeat_time = data[idd]['data_saved'].get('n_graph', 1)
for i in repeat_time:
    # créer un subplot
    pass'''

