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
    elif idd == '00000008':
        pass
    elif idd == '0000000A':
        pass
    elif idd == '0000000B':
        pass
    elif idd == '0000000C':
        pass
    elif idd == '0000000D':
        pass
    elif idd == '00000099':
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
    elif idd == '02070081':
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
    elif idd == '04010000':
        pass
    elif idd == '04020000':
        pass
    elif idd == '04030000':
        pass
    elif idd == '04040000':
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
        for i, y in enumerate(data[idd]['saved_data']):
            y = y[:5]
            # hex2dec
            y = int(y, 16)
            saved_data.append(y)
        data[idd]['saved_data'] = saved_data
    elif idd == '04530000': # Inverter 3 SpI and I (inv3SP) - SpId SpIq Intd Intq
        pass
    elif idd == '04540000':
        pass
    elif idd == '04630000': # Inverter 3 SVM amplitude and SVM angle (inv3SP) - SpId SpIq Intd Intq
        pass
    elif idd == '04640000': # Inverter 4 SpI and I (inv4SP) - SpId SpIq Intd Intq
        pass
    elif idd == '04730000': # Inverter 3 Ia Ib Ic
        pass
    elif idd == '04740000': # Inverter 4 Ia Ib Ic
        pass
    elif idd == '04830000': # Inverter 3 I and V (inv3IV) - Iq Id Vq Vd (all BE i16)
        pass
    elif idd == '04840000': # Inverter 4 I and V (inv4IV) - Iq Id Vq Vd (all BE i16)
        pass
    elif idd == '04930000': # Inverter 3 Cos Sin
        pass
    elif idd == '04940000': # Inverter 4 Cos Sin
        pass
    elif idd in ['08000080', '08010080']: # ok
        # hex2dec(y)
        # def pourcentage(value, max):
        # 100% APPS (full travel) corresponds to 63534
        max = 65354
        saved_data = []
        for i, y in enumerate(data[idd]['saved_data']):
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
        for i, y in enumerate(data['08020080']['saved_data']):
            # hex2dec
            y = int(y, 16)
            # transformer en degré
            y =  0.0184*y-53.174
            saved_data.append(y)
        data['08020080']['saved_data'] = saved_data
    raise ValueError

