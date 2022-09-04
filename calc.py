date = {}


def calculating(mess, user):
    if len(date[user]) != 3:
        val = check_mess(mess)
        if val:
            date[user].append(float(val))
            if len(date[user]) == 1:
                return 'Enter fuel consumption per 100 km'
            elif len(date[user]) == 2:
                return 'Enter the price per liter of fuel'
        else:
            return 'Please enter a number'


def check_mess(mess):
    mess = mess.strip()
    mess = mess.replace(',', '.')
    if mess.replace('.', '').isdigit():
        return mess
    else:
        return False


def date_create(user):
    date[user] = []
