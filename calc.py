date = {}


def calculating(mess, user):
    if len(date[user]) != 3:
        val = check_mess(mess)
        if val:
            date[user].append(float(val))
            if len(date[user]) == 1:
                return 'Введите расход топлива в литрах на 100 км'
            elif len(date[user]) == 2:
                return 'Введите цену топлива за литр'
        else:
            return 'Введите число'
    elif len(date[user]) == 3:
        if mess == "Я еду один":
            date[user].append(1)
        else:
            val = check_int(mess)
            if val:
                date[user].append(int(val))
            else:
                return False
        res = result(user)
        liters = liters_calc(user)
        res = f'С тебя {res} руб.\nПотрачено {liters} л. топлива' if mess == "Я еду один" \
            else f'С каждого по {res} руб.\nПотрачено {liters} л. топлива'
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


def liters_calc(user):
    return round((date[user][0]/100) * date[user][1], 1)


def date_create(user):
    date[user] = []
