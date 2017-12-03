import telebot
import os
import random

token = 'TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def send_rand_photo(message):
    directory = 'C:/telegramBot/3/img/'
    files = os.listdir(directory)
    random_file = random.choice(files)
    photo = open(directory + '/' + random_file, 'rb')
    bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
     bot.polling(none_stop=True)
