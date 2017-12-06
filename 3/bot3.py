import telebot
import os   #подключаем модуль ос, нужен будет для получения списка файлов в папке
import random  #модуль рандом... для рандома

token = 'TOKEN' #токен
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text']) #хэндлер обрабатывающий любой введенный нами текст
def rand_photo(message):
    directory = 'C:/telegramBot/3/img/'  #присваеваем переменной директори значение пути к папке с нашими фоточками
    files = os.listdir(directory)  #присваеваем переменной файлс значение соответствующее списку всех имен файлов в нашей папке
    random_file = random.choice(files)  #присваиваем переменной рэндомфайл значение равное случайно выбранному имени файла из нашего списка
    photo = open(directory + '/' + random_file, 'rb')  #присваиваем переменной фото значение пути к нашему случайному файлику
    bot.send_photo(message.chat.id, photo) #бот посылает нам случайное фото

if __name__ == '__main__':
     bot.polling(none_stop=True)  #и опять пулим
