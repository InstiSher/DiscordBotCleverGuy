from config import token
import discord
from discord.ext import commands
import json
from SongFinder import Lyrics
import datetime

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


intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='/', intents=intents)


# С помощью декоратора создаём первую команду
@bot.command(aliases=['text', 'текст', 'Текст', 'ТЕкст', 'Text', 'test'])
async def ping(ctx, SongName): #/text 'Предложение в кавычках'
    start = datetime.datetime.now()
    print('Время старта: ' + str(start))
    lyrics = Lyrics(SongName)
    global flagForBigger
    # print(SongName)
    # print(lyrics)
    #                                СДЕЛАТЬ ОТНОШЕНИЕ К РОЛЯМ
    if lyrics["lyrics"] == "":
        await ctx.send("Текст песни не найден")
        flagForBigger = 4
    elif lyrics["lyrics"] == "Вы создаёте слишком много Плейлистов":
        await ctx.send("YtMusic получает слишком много запросов")
    else:
        length = len(lyrics['lyrics'])
        if length > 1990 and length < 3980:
            lyrics = Bigger1990(lyrics)
            flagForBigger = 1
        elif length > 3980:
            lyrics = Bigger3980(lyrics)
            flagForBigger = 2

    if flagForBigger == 0:
        try:
            await ctx.send(f"Найдена следующая песня:\n{lyrics['Title']} {lyrics['Artists']}")
            await ctx.send(lyrics['lyrics'])
        except Exception as e:
            await ctx.send('Ошибка Компиляции Текста')
            print(e)
    elif flagForBigger == 1:
        try:
            await ctx.send(f"Найдена следующая песня:\n{lyrics['Title']} {lyrics['Artists']}")
            await ctx.send(lyrics['lyrics'])
            await ctx.send(lyrics['lyrics2'])
        except Exception as e:
            await ctx.send('Ошибка Компиляции Текста')
            print(e)
    elif flagForBigger == 2:
        try:
            await ctx.send(f"Найдена следующая песня:\n{lyrics['Title']} {lyrics['Artists']}")
            await ctx.send(lyrics['lyrics'])
            await ctx.send(lyrics['lyrics2'])
            await ctx.send(lyrics['lyrics3'])
        except Exception as e:
            await ctx.send('Ошибка Компиляции Текста')
            print(e)

    finish = datetime.datetime.now()
    print('Время окончания: ' + str(finish))

    print('Время работы: ' + str(finish - start))

if __name__ == "__main__":
    flagForBigger = 0
    bot.run(token)

