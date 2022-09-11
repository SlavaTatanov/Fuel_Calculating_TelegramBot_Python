import telebot
import config as cf
import keyboards as k
import calc as cl


bot = telebot.TeleBot(cf.TOKEN)

k.keyboards_create()


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
    else:
        bot.send_message(message.chat.id, 'Если хотите выполнить расчет топлива\nиспользуйте кнопку', reply_markup=k.keyboards['keyboard_init'])


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
        bot.send_message(message.chat.id, res, reply_markup=k.keyboards['keyboard_init'])
        bot.register_next_step_handler(message, init)
    else:
        bot.send_message(message.chat.id, 'На сколько человек делим деньги за поездку?\nПожалуйста используйте кнопки',
                         reply_markup=k.keyboards['keyboard_people'])
        bot.register_next_step_handler(message, final_calc)


bot.polling(none_stop=True)
