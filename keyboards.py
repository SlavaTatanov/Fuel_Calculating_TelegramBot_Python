from telebot import types

keyboards = {}


def keyboards_create():
    keyboard_init()
    keyboard_remove()
    keyboard_people()
    keyboard_admin()


def keyboard_init():
    init_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton('Расчет топлива')
    init_k.add(button)
    keyboards['keyboard_init'] = init_k


def keyboard_people():
    people_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Я еду один")
    button2 = types.KeyboardButton('2')
    button3 = types.KeyboardButton('3')
    button4 = types.KeyboardButton('4')
    people_k.add(button1)
    people_k.add(button2, button3, button4)
    keyboards['keyboard_people'] = people_k


def keyboard_remove():
    remove_k = types.ReplyKeyboardRemove()
    keyboards['keyboard_remove'] = remove_k

def keyboard_admin():
    admin_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_1 = types.KeyboardButton("Счетчик пользователей")
    button_2 = types.KeyboardButton("Назад")
    admin_k.add(button_1, button_2, row_width=1)
    keyboards["keyboard_admin"] = admin_k
