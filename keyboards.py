from telebot import types

keyboards = {}


def keyboards_create():
    keyboard_init()


def keyboard_init():
    init_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button = types.KeyboardButton('Fuel calculating')
    init_k.add(button)
    keyboards['keyboard_init'] = init_k
