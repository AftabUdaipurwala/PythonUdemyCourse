from datetime import *

def validatecard(expDate):
    if expDate>datetime.now().date():
        return "Valid Card"
    else:
        return 'Invalid Card'

validatecard(date(2023,2,21))