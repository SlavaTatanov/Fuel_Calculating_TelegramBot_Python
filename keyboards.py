from telebot import types

keyboards = {}


def keyboards_create():
    keyboard_init()


def keyboard_init():
    init_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button = types.KeyboardButton('Fuel calculating')
    init_k.add(button)
    keyboards['keyboard_init'] = init_k


def keyboard_people():
    people_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton("I'm going alone")
    button2 = types.KeyboardButton('2')
    button3 = types.KeyboardButton('3')
    button4 = types.KeyboardButton('4')
    people_k.add(button1)
    people_k.add(button2, button3, button4)
    keyboards['keyboard_people'] = people_k
