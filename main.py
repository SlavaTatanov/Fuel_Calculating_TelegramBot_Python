import telebot
import config as cf
import keyboards as k


bot = telebot.TeleBot(cf.TOKEN)

k.keyboards_create()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi, I'm a bot that can calculate fuel and the amount of money spent on it on "
                                      "a trip.", reply_markup=k.keyboards['keyboard_init'])


bot.polling(none_stop=True)
