import telebot

token = 'TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat(message):
    bot.send_message(message.chat.id, "ehehe...")
    bot.send_photo(message.chat.id, photo='https://tcrf.net/images/thumb/5/5f/DDLC-Sayuri-early.png/320px-DDLC-Sayuri-early.png')

if __name__ == '__main__':
     bot.polling(none_stop=True)
