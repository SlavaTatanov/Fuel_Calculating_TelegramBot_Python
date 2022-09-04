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
    elif len(date[user]) == 3:
        if mess == "I'm going alone":
            date[user].append(1)
        else:
            val = check_int(mess)
            if val:
                date[user].append(int(val))
            else:
                return False
        res = result(user)
        del date[user]
        return str(res)


def check_mess(mess):
    mess = mess.strip()
    mess = mess.replace(',', '.')
    if mess.replace('.', '').isdigit():
        return mess
    else:
        return False


def check_int(mess):
    mess = mess.strip()
    if mess.isdigit():
        return mess
    else:
        return False


def result(user):
    res = (date[user][1]*date[user][2]/100) * date[user][0]
    res = int(res/date[user][3])
    return res


def date_create(user):
    date[user] = []
