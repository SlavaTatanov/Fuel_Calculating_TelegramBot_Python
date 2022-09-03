import telebot
import config as cf
import keyboards as k
import calc as cl


bot = telebot.TeleBot(cf.TOKEN)

k.keyboards_create()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi, I'm a bot that can calculate fuel and the amount of money spent on it on "
                                      "a trip.", reply_markup=k.keyboards['keyboard_init'])


@bot.message_handler(content_types=['text'])
def init(message):
    mess = message.text
    user = message.from_user.id
    if mess == 'Fuel calculating':
        cl.date_create(user)
        bot.send_message(message.chat.id, 'How many kilometers is the trip?')
        bot.register_next_step_handler(message, base_values)
    else:
        bot.send_message(message.chat.id, 'Please use the button', reply_markup=k.keyboards['keyboard_init'])


def base_values(message):
    pass


bot.polling(none_stop=True)
