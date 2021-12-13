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
    elif idd == '04430000':
        pass
    elif idd == '04440000':
        pass
    elif idd == '04530000':
        pass
    elif idd == '04540000':
        pass
    elif idd == '04630000':
        pass
    elif idd == '04640000':
        pass
    elif idd == '04830000':
        pass
    elif idd == '04840000':
        pass
    elif idd == '08000080':
        # hex2dec(y)
        # def pourcentage(value, max):
        # 100% APPS (full travel) corresponds to 63534
        max = 65354
        saved_data = []
        for i, y in enumerate(data['08000080']['saved_data']):
            # hex2dec
            y = int(y, 16)
            # valeur en pourcentage
            y = pourcentage_custum(y, max)
            saved_data.append(y)
        data['08000080']['saved_data'] = saved_data
    elif idd == '08010080':
        pass
    elif idd == '08020080':
        saved_data = []
        for i, y in enumerate(data['08020080']['saved_data']):
            # hex2dec
            y = int(y, 16)
            # transformer en degré
            y =  0.0184*y-53.174
            saved_data.append(y)
        data['08020080']['saved_data'] = saved_data
    raise ValueError

