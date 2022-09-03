date = {}


def check_mess(mess):
    mess = mess.strip()
    mess = mess.replace(',', '.')
    if mess.replace('.', '').isdigit():
        return mess
    else:
        return False


def date_create(user):
    date[user] = []
