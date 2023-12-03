import telebot
from config import token
from telebot import types
from SongFinderTg import Lyrics

bot = telebot.TeleBot(token)


def Bigger1990(lyrics):
    dict_lyrics = {
        'lyrics': '',
        'lyrics2': '',
    }
    count = 0
    flag = 0
    x = 0
    for i in lyrics['lyrics']:
        if count < 1990 and flag == 0:
            dict_lyrics['lyrics'] = dict_lyrics['lyrics'] + i  # После 1900 найти \n и после как нашлось изменить флаг на lyrics2
            if count > 1900 and i == '\n':  # Да, это один символ
                x = count + 1990
                flag += 1
        elif count < x and flag == 1:
            dict_lyrics['lyrics2'] = dict_lyrics['lyrics2'] + i
        count += 1
    return dict_lyrics

def Bigger3980(lyrics):
    dict_lyrics = {
        'lyrics': '',
        'lyrics2': '',
        'lyrics3': '',
    }
    count = 0
    flag = 0
    x = 0
    for i in lyrics['lyrics']:
        if count < 1990 and flag == 0:
            dict_lyrics['lyrics'] = dict_lyrics['lyrics'] + i  # После 1900 найти \n и после как нашлось изменить флаг на lyrics2
            if count > 1900 and i == '\n':  # Да, это один символ
                x = count + 1990
                flag += 1
        elif count < x and flag == 1:
            dict_lyrics['lyrics2'] = dict_lyrics['lyrics2'] + i
            if count > x - 90 and i == '\n':  # Да, это один символ
                flag += 1
        else:
            dict_lyrics['lyrics3'] = dict_lyrics['lyrics3'] + i
        count += 1
    return dict_lyrics


def Poisk(message):
    lyrics = Lyrics(message.text)
    if lyrics['lyrics'] == "":
        bot.send_message(message.chat.id, text="")
    elif lyrics["lyrics"] == "Вы создаёте слишком много Плейлистов":
        bot.send_message(message.chat.id, text="YtMusic получает слишком много запросов, повторите позже")
    else:
        bot.send_message(message.chat.id, text=f"Найдена следующая песня:\n{lyrics['Title']} {lyrics['Artists']}")
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
