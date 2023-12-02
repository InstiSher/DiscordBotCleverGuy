from ytmusicapi import YTMusic

def GetLyricsMain(SongName):
    ytmusic = YTMusic("oauth.json")    # Регистрируемся Под своим аккаунтом в ytmusic
    playlistId = ytmusic.create_playlist('test1', 'test description')   # Создаем Плейлист где сохраним нашу песню
    search_results = ytmusic.search(SongName)   # Ведём поиск 10 самых популярных выводов(Популярное, песни, альбомы и т.д)
    try:     # В этом блоке мы пробуем Сохранить песню в плейлист
        count = 0  # Подсчет на каком мы сейчас месте из 10 найденых выводов
        for i in search_results:   # i берет первый вывод проходится по алгоритму если не вышло, то берет второй вывод
            if i['category'] == 'Songs' or i['category'] == None:  # Так как нам нужны рекомендации и песни сделаем на них проверку
                Title = search_results[count]['title']  # сохраняем название песни в переменную Title
                Artists = search_results[count]["artists"][0]["name"]
                if Title[0:2].upper() == SongName[0:2].upper():  # сравниваем Два первых символа названия Песни которую мы нашни, и которую пользователь задал
                    ytmusic.add_playlist_items(playlistId, [search_results[count]['videoId']])  # Добавляем песню в плейлист
                    break   # завершаем цикл for
            count += 1

        playlist = ytmusic.get_watch_playlist(search_results[count]['videoId'])  # Просматриваем песню которую сохранили в плейлисте

        lyrics_song = ytmusic.get_lyrics(playlist["lyrics"])  # Сохраняем текст песни
        lyrics_song["Title"] = Title  # Сохраняем название песни
        lyrics_song["Artists"] = Artists # Сохраняем автора песни
    except Exception as e:  # Если на каком-то моменте вышла ошибка или песня не имеет текста, ты мы получим
        lyrics_song = {"lyrics": ""}  # Пустой словарь
        print(e)
    finally:  # Даже если была или не было ошибки Удалить созданный плейлист
        # DELITING PLAYLIST
        ytmusic.delete_playlist(playlistId)

    return lyrics_song  # Возвращаем текст песни по названию песни


# SongName = "astral step"
def Lyrics(SongName):
    global Author
    global Flag
    try:
        print('Первый')
        lyrics = GetLyricsMain(SongName)
        return lyrics
    except Exception as e:
        print(e)



# print(Lyrics(SongName))
