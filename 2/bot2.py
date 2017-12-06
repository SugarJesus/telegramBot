#для начала нужно установить библиотеку pyTelegramBotAPI

import telebot
from telebot import types    #для подключения клавиатуры

token = 'TOKEN' #токен бота выданный Botfather
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  #запускаем хэндлер (специальный обработчик для разных типов сообщений) обрабатывающий команду "старт"
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  #создаем клавиатуру и меняем размер, чтобы кнопки не были огромными
    keyboard.add(*[types.KeyboardButton(name) for name in ['Sayori',
        'Natsuki', 'Yuri', 'Monika']])  #небольшой цикл, чтобы не задавать каждую кнопку отдельно
    bot.send_message(message.chat.id, 'Who will you choose?',   #текстовый ответ бота на команду старт
        reply_markup=keyboard) #завершаем создание клавиатуры

@bot.message_handler(content_types=['text'])   #хэндлер обрабатывающий наши текстовые сообщения
def girl(message):
    if message.text == "Sayori":   #запускаем оператор ветвления реагирующий на определенные слова
        bot.send_message(message.chat.id,
        'ehehe...')              #текстовый ответ бота на определенное сообщение
        bot.send_photo(message.chat.id,      #отправляем картинку на определенное сообщение
        photo='https://tcrf.net/images/thumb/5/5f/DDLC-Sayuri-early.png/320px-DDLC-Sayuri-early.png')  #
    elif message.text == "Natsuki":           #повторяем в зависимости от количества нужных нам вариантов у нас их всего 4
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
    else:    #закрываем оператор ветвления
        bot.send_message(message.chat.id,
        '{ololo} is not in the club!'.format(ololo=message.text))  #на любые сообщения не удовлетворяющие описанным выше бот будет отвечать
                                                                   #текстом этого сообщения и припиской о том, что "текст" не состоит в клубе
if __name__ == '__main__':
     bot.polling(none_stop=True)  #запускаем лонг пулинг, параметр говорит, что бот должен стараться не прекращать работу при возникновении ошибок
