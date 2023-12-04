import telebot
from config import token
from telebot import types
from SongFinderTg import Lyrics

bot = telebot.TeleBot(token)

def Poisk(message):
    print(message.text)
    lyrics = Lyrics(message.text)
    if lyrics['lyrics'] == "":
        bot.send_message(message.chat.id, text="Текст песни не найден")
    elif lyrics["lyrics"] == "Вы создаёте слишком много Плейлистов":
        bot.send_message(message.chat.id, text="YtMusic получает слишком много запросов, повторите позже")
    else:
        bot.send_message(message.chat.id, text=f"Найдена следующая песня:\n{lyrics['Title']}, {lyrics['Artists']}")
        bot.send_message(message.chat.id, text=f"{lyrics['lyrics']}")


@bot.message_handler(commands=['start'])
def welcome(message):
    # Создание Кнопок для пользователя
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать поиск❓")
    markup.add(btn1)
    saves = '0'
    # Вывод сообщения и выдача пользовательских кнопок
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот, который поможет тебе в поиске текстов песен".format(
                         message.from_user), reply_markup=markup)  ## Разметка ответов reply_markup
    ## {0.first_name} От лица пользователя используется формат: message.from_user


@bot.message_handler(content_types=['text'])
def ytmusic(message):
    if message.text == "Начать поиск❓":
        bot.send_message(message.chat.id, text="Введите название песни, затем автора по возможности")
        bot.register_next_step_handler(message, Poisk)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать поиск❓")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Не знаю таких слов", reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()
