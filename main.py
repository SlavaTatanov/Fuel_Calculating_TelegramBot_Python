import telebot
import config as cf
import keyboards as k
import calc as cl
from tools.admin import admin
from tools.counter import Counter


bot = telebot.TeleBot(cf.TOKEN)

k.keyboards_create()
counter = Counter()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я рассчитываю количество денег потраченных на топливо в поездке",
                     reply_markup=k.keyboards['keyboard_init'])


@bot.message_handler(content_types=['text'])
def init(message):
    mess = message.text
    user = message.from_user.id
    if mess == 'Расчет топлива':
        cl.date_create(user)
        bot.send_message(message.chat.id, 'Сколько километров поездка?',
                         reply_markup=k.keyboards['keyboard_remove'])
        bot.register_next_step_handler(message, base_values)
    elif mess == "admin.run" and admin(message.chat.id):
        bot.send_message(message.chat.id, 'Режим администратора',
                        reply_markup=k.keyboards['keyboard_admin'])
        bot.register_next_step_handler(message, admin_menu)
    else:
        bot.send_message(message.chat.id, 'Если хотите выполнить расчет топлива\nиспользуйте кнопку',
                         reply_markup=k.keyboards['keyboard_init'])


def base_values(message):
    mess = message.text
    user = message.from_user.id
    res = cl.calculating(mess, user)
    if len(cl.date[user]) != 3:
        bot.send_message(message.chat.id, res)
        bot.register_next_step_handler(message, base_values)
    else:
        bot.send_message(message.chat.id, 'На сколько человек делим деньги за поездку?',
                         reply_markup=k.keyboards['keyboard_people'])
        bot.register_next_step_handler(message, final_calc)


def final_calc(message):
    mess = message.text
    user = message.from_user.id
    res = cl.calculating(mess, user)
    if res:
        if not admin(message.chat.id):
            counter.add_id(message.chat.id)
        bot.send_message(message.chat.id, res, reply_markup=k.keyboards['keyboard_init'])
        bot.register_next_step_handler(message, init)
    else:
        bot.send_message(message.chat.id, 'На сколько человек делим деньги за поездку?\nПожалуйста используйте кнопки',
                         reply_markup=k.keyboards['keyboard_people'])
        bot.register_next_step_handler(message, final_calc)

def admin_menu(message):
    if message.text == "Счетчик пользователей":
        bot.send_message(message.chat.id, f"{counter.user_count()}")
        bot.register_next_step_handler(message, admin_menu)
    elif message.text == "Назад":
        bot.send_message(message.chat.id, "Выход из режима администратора",
                         reply_markup=k.keyboards['keyboard_init'])
        bot.register_next_step_handler(message, init)
    else:
        bot.register_next_step_handler(message, admin_menu)

bot.polling(none_stop=True)
