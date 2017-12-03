import telebot
from telebot import types

token = 'TOKEN'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Sayori',
        'Natsuki', 'Yuri', 'Monika']])
    msg = bot.send_message(message.chat.id, 'Who will you choose?',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, girl)

@bot.message_handler(content_types=['text'])
def girl(message):
    if message.text == "Sayori":
        bot.send_message(message.chat.id,
        'ehehe...')
        bot.send_photo(message.chat.id,
        photo='https://tcrf.net/images/thumb/5/5f/DDLC-Sayuri-early.png/320px-DDLC-Sayuri-early.png')
    elif message.text == "Natsuki":
        bot.send_message(message.chat.id,
        'Baka!')
        bot.send_photo(message.chat.id,
        photo='https://goo.gl/SMnG5n')
    elif message.text == "Yuri":
        bot.send_message(message.chat.id,
        'We can read together')
        bot.send_photo(message.chat.id,
        photo='https://goo.gl/vEr9UG')
    elif message.text == "Monika":
        bot.send_message(message.chat.id,
        'Just Monika')
        bot.send_photo(message.chat.id,
        photo='https://tcrf.net/images/thumb/1/12/DDLC-Monika-early.png/320px-DDLC-Monika-early.png')
    else:
        bot.send_message(
        message.chat.id,
        '{ololo} is not in the club!'.format(ololo=message.text))

if __name__ == '__main__':
     bot.polling(none_stop=True)
