import re
import os
import time
import sys
import json


def get_file(path):
    '''demande le fichier à filtrer
    args : path
    raise : aucun
    return : nom_du_fichier(str)'''
    files_names = []
    for file_name in os.listdir(path+'data_file\\'):
        if file_name[-4:] == ".txt":
            files_names.append(file_name)
    
    # afficher fichier dans data_file
    if not files_names:
        print('Aucun fichier détecter')
    else:
        print(files_names)

    file_to_filter =""
    while True:
        file_to_filter = input("Enter le nom du ficher avec l'extension ici : ")
        if file_to_filter in files_names:
            break
        print('fichier invalide...')
    return file_to_filter

def file_to_data(path, file_to_filter):
    '''filtre les données selon leur identifiant,
    il ne prend pas en contre la provenance ('can1')
    args : path, file_to_filter(str et fini par .txt)
    raise : aucun
    return : tup(file_name(str), data(dict))'''
    print('Traitement des données...')
    txt = open(path+'data_file\\'+file_to_filter, 'r').read()
    raw_data = txt.split('\n')
    data = {}
    for d in raw_data:
        if not re.search('\[', d):
            #C'est pas save, mais ça devrait jamais arriver
            raise ValueError('[x] non présent')
        d = d.split(' ')
        time = d[1][1:-1]
        identifiant = d[5]
        saved_data = "".join(d[10:])
        if not data.get(['identifiant'], ""):
            data[identifiant] = {}
            data[identifiant]['time'] = []
            data[identifiant]['saved_data'] = []
        data[identifiant]['time'].append(time)
        data[identifiant]['saved_data'].append(saved_data)
    return data

def data_to_json(file_name, data):
    '''écrit les datas dans un json
    args : file_name(str), data(dict)
    raise : aucun
    return : aucun'''
    with open(create_file_name_json(file_name), 'w') as fich:
        fich.write(json.dumps(data))

def create_file_name_json(file_name):
    '''prend le nom du fichier et créer un fichier file_name+"_json.txt"
    args : file_name(str)
    raise : aucun
    return : nouveau_nom_du _fichier(str)'''
    file_name = file_name[:-4] + '_json.txt'
    return file_name

def read_json(file_name):
    '''lecture du fichier json
    args : file_name(str)
    raise : aucun
    return : data(dict)'''
    data = {}
    with open(create_file_name_json(file_name), 'w') as fich:
        data = json.loads(fich.read())
    return data

