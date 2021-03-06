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
if os.path.exists(f'data_file/{file[:-4]}.json'):
    '''suppose que le fichier finit en .txt'''
    file = filter_data.create_file_name_json(file)
    data = filter_data.read_json(file)
else:
    data = filter_data.file_to_data(path, file)
    # filtre les datas
    for key in data.keys():
        formule.get_xy_value(key, data)
    # save data after treatment
    filter_data.data_to_json(file, data)

print('Traitement terminée')

# Commencer à afficher les graphiques
'''ne pas oublier
repeat_time = data[idd]['data_saved'].get('n_graph', 1)
for i in repeat_time:
    # créer un subplot
    pass'''

