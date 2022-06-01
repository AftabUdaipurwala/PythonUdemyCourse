from datetime import *

def validatecard(expDate):

    if expDate>datetime.now().date():
        return "Valid Card"
    else:
        raise RuntimeError('Invalid Card')

validatecard(date(2023,2,21))