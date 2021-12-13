import re
import os
import time
import sys
import json


def data_to_json(path):
    '''filtre les données
    args : path
    raise : aucun
    return : data(dict)'''

    files_names = []
    for file_name in os.listdir(path+'data_file\\'):
        if file_name[-4:] == ".txt":
            files_names.append(file_name)