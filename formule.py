


def pourcentage_custum(value, max):
    return 100*value/max

def get_y_value(idd, data):
    '''retourne la valeur y traiter
    args : idd(str)[id+'id_found']
    raise : ValueError('idd non valide')
    return : liste_formules(list)
    '''
    if idd == '00000004':
        pass
    elif idd == '00000008': # LEDIMD:color
        # useless
        pass
    elif idd == '0000000A': # frameUpRight
        # useless
        pass
    elif idd == '0000000B': # frameUpLeft:label
        # useless
        pass
    elif idd == '0000000C': # frameDownRight:label
        # useless
        pass
    elif idd == '0000000D': # frameDownLeft:label
        # useless
        pass
    elif idd == '00000099':
        pass
    elif idd == '01000002':
        # rtdPressedBox:color(fl.GREEN)
        # aucune donnée est collectée
        pass
    elif idd == '01310000':
        pass
    elif idd == '01800000':
        pass
    elif idd == '02010001':
        pass
    elif idd == '02020080':
        pass
    elif idd == '02020180':
        pass
    elif idd == '02020280':
        pass
    elif idd == '02020380':
        pass
    elif idd == '02020480':
        pass
    elif idd == '02020580':
        pass
    elif idd == '02020680':
        pass
    elif idd == '02020780':
        pass
    elif idd == '02020880':
        pass
    elif idd == '02020980':
        pass
    elif idd == '02020A80':
        pass
    elif idd == '02020B80':
        pass
    elif idd == '02020C81':
        pass
    elif idd == '02030080':
        pass
    elif idd == '02030180':
        pass
    elif idd == '02030280':
        pass
    elif idd == '02030380':
        pass
    elif idd == '02030480':
        pass
    elif idd == '02030580':
        pass
    elif idd == '02030680':
        pass
    elif idd == '02030780':
        pass
    elif idd == '02030880':
        pass
    elif idd == '02030980':
        pass
    elif idd == '02030A80':
        pass
    elif idd == '02030B80':
        pass
    elif idd == '02030C80':
        pass
    elif idd == '02030D80':
        pass
    elif idd == '02030E80':
        pass
    elif idd == '02030F80':
        pass
    elif idd == '02031080':
        pass
    elif idd == '02031180':
        pass
    elif idd == '02031280':
        pass
    elif idd == '02031381':
        pass
    elif idd == '02070081': # id & 0xFFFF0000 == 0x02070000
        pass
    elif idd == '02090080':
        pass
    elif idd == '02090181':
        pass
    elif idd == '020C0080':
        pass
    elif idd == '020C0180':
        pass
    elif idd == '020C0281':
        pass
    elif idd == '04010000': # inverterFrontL:color
        # useless
        pass
    elif idd == '04020000': # inverterFrontR:color
        # useless
        pass
    elif idd == '04030000': # inverterBackL:color
        # useless
        pass
    elif idd == '04040000': # inverterBackR:color
        # useless
        pass
    elif idd == '04110000':
        pass
    elif idd == '04120000':
        pass
    elif idd == '04130000':
        pass
    elif idd == '04140000':
        pass
    elif idd in ['04430000', '04440000']: # ok
        ''' Motor 3 and 4 speed (BE i16)
            on utilise seulement les 4 premiers chiffres
            de notre donnée'''
        saved_data = []
        for y in data[idd]['saved_data']:
            y = y[:5]
            # hex2dec
            y = int(y, 16)
            saved_data.append(y)
        data[idd]['saved_data'] = saved_data
    elif idd == '04530000': # Inverter 3 SpI and I (inv3SP) - SpId SpIq Intd Intq
        saved_data1 = []
        saved_data2 = []
        saved_data3 = []
        saved_data4 = []
        for y in data[idd]['saved_data']:
            saved_data1.append(int(y[:4], 16))
            saved_data2.append(int(y[4:8], 16))
            saved_data3.append(int(y[8:12], 16))
            saved_data4.append(int(y[12:17], 16))
        data[idd]['saved_data']['y1'] = saved_data1
        data[idd]['saved_data']['y2'] = saved_data2
        data[idd]['saved_data']['y3'] = saved_data3
        data[idd]['saved_data']['y4'] = saved_data4
        data[idd]['saved_data']['n_graph'] = 4
        pass
    elif idd == '04540000':
        pass
    elif idd == '04630000': # Inverter 3 SVM amplitude and SVM angle (inv3SP) - SpId SpIq Intd Intq
        '''Sdata.SVMamp3= data(Sdata.idx.inv3SVM,:);
Sdata.SVMamp3.hex = extractBetween(Sdata.SVMamp3.data,13,14) + extractBetween(Sdata.SVMamp3.data,16,17);
Sdata.SVMamp3.dec = hex2dec(Sdata.SVMamp3.hex);
Sdata.SVMamp3.dec_int = double(typecast(uint16(Sdata.SVMamp3.dec),'int16'))/10;

Les données ne se rendent pas à l'index 19, 20 et 22, 23
Sdata.SVMang3 = data(Sdata.idx.inv3SVM,:);
Sdata.SVMang3.hex = extractBetween(Sdata.SVMang3.data,19,20) + extractBetween(Sdata.SVMang3.data,22,23);
Sdata.SVMang3.dec = hex2dec(Sdata.SVMang3.hex);
Sdata.SVMang3.dec_int = double(typecast(uint16(Sdata.SVMang3.dec),'int16'))/1000;'''
        saved_data1 = []
        saved_data2 = []
        for y in data[idd]['saved_data']:
            saved_data1.append(int(y[12:17], 16))
            # Les données ne se rendent pas à l'index 19, 20 et 22, 23
            saved_data1.append(0)

        data[idd]['saved_data']['y1'] = saved_data1
        data[idd]['saved_data']['y2'] = saved_data2
        data[idd]['saved_data']['n_graph'] = 2
    elif idd == '04640000': # Inverter 4 SpI and I (inv4SP) - SpId SpIq Intd Intq
        saved_data = []
        for y in data[idd]['saved_data']:
            saved_data.append(int(y, 16))
        data[idd]['saved_data'] = saved_data
    elif idd in ['04730000', '04740000']: # Inverter 3 et 4 Ia Ib Ic
        # inexistant dans les fichiers reçus
        pass
    elif idd in ['04830000', '04840000']: # Inverter 3 et 4 I and V (inv3IV) - Iq Id Vq Vd (all BE i16)
        # inexistant dans les fichiers reçus
        pass
    elif idd == ['04930000', '04940000']: # Inverter 3 et 4 Cos Sin
        # inexistant dans les fichiers reçus
        pass
    elif idd in ['08000080', '08010080']: # ok
        # hex2dec(y)
        # def pourcentage(value, max):
        # 100% APPS (full travel) corresponds to 63534
        max = 65354
        saved_data = []
        for y in data[idd]['saved_data']:
            # hex2dec
            y = int(y, 16)
            # valeur en pourcentage
            y = pourcentage_custum(y, max)
            saved_data.append(y)
        data[idd]['saved_data'] = saved_data
    elif idd == '08020080': # 
        '''SPS - Steering position sensor [LE i16 ->need to change from uint16 to int16]
           Need to make a calibration run to know value at full lock both ways and
           then convert data to degree (quick fix). Even better would be to go into
           acquisition module code and calibrate it there (ask VincentD how to).
           Volant full lock gauche: 3970 (80.30deg), droit = 1719 (73.20deg)
           Roues tournent d'environ 20deg de chaque côté'''
        saved_data = []
        for y in data[idd]['saved_data']:
            # hex2dec
            y = int(y, 16)
            # transformer en degré
            y =  0.0184*y-53.174
            saved_data.append(y)
        data[idd]['saved_data'] = saved_data
    else:
        raise ValueError('aucun identifiant connue dans formule.py')

