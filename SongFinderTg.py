from ytmusicapi import YTMusic

def GetLyricsMain(SongName):
    ytmusic = YTMusic("oauth.json")    # Регистрируемся Под своим аккаунтом в ytmusic, с VPN не работет
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

        if count != 10:
            playlist = ytmusic.get_watch_playlist(search_results[count]['videoId']) # Просматриваем песню которую сохранили в плейлисте
            lyrics_song = ytmusic.get_lyrics(playlist["lyrics"]) # Сохраняем текст песни
            lyrics_song["Title"] = Title # Сохраняем название песни
            lyrics_song["Artists"] = Artists # Сохраняем автора песни
        else:
            lyrics_song = {"lyrics": ""}# При выходе за пределы
    except Exception as e:  # Если на каком-то моменте вышла ошибка или песня не имеет текста, ты мы получим
        lyrics_song = {"lyrics": ""}  # Пустой словарь
        print(e)
    finally:  # Даже если была или не было ошибки Удалить созданный плейлист
        # DELITING PLAYLIST
        ytmusic.delete_playlist(playlistId)

    return lyrics_song  # Возвращаем текст песни по названию песни

def GetLyricsSecond(SongName):
    ytmusic = YTMusic("oauthsecond.json")
    playlistId = ytmusic.create_playlist('test1', 'test description')
    search_results = ytmusic.search(SongName)
    try:
        count = 0
        for i in search_results:
            if i['category'] == 'Songs' or i['category'] == None:
                Title = search_results[count]['title']
                Artists = search_results[count]["artists"][0]["name"]
                if Title[0:2].upper() == SongName[0:2].upper():
                    ytmusic.add_playlist_items(playlistId, [search_results[count]['videoId']])
                    break
            count += 1
        if count != 10:
            playlist = ytmusic.get_watch_playlist(search_results[count]['videoId'])
            lyrics_song = ytmusic.get_lyrics(playlist["lyrics"])
            lyrics_song["Title"] = Title
            lyrics_song["Artists"] = Artists
        else:
            lyrics_song = {"lyrics": ""}
    except Exception as e:
        lyrics_song = {"lyrics": ""}
        print(e)
    finally:
        # DELITING PLAYLIST
        ytmusic.delete_playlist(playlistId)

    return lyrics_song

def GetLyricsThird(SongName):
    ytmusic = YTMusic("oauththird.json")
    playlistId = ytmusic.create_playlist('test1', 'test description')
    search_results = ytmusic.search(SongName)
    try:
        count = 0
        for i in search_results:
            if i['category'] == 'Songs' or i['category'] == None:
                Title = search_results[count]['title']
                Artists = search_results[count]["artists"][0]["name"]
                if Title[0:2].upper() == SongName[0:2].upper():
                    ytmusic.add_playlist_items(playlistId, [search_results[count]['videoId']])
                    break
            count += 1
        if count != 10:
            playlist = ytmusic.get_watch_playlist(search_results[count]['videoId'])
            lyrics_song = ytmusic.get_lyrics(playlist["lyrics"])
            lyrics_song["Title"] = Title
            lyrics_song["Artists"] = Artists
        else:
            lyrics_song = {"lyrics": ""}
    except Exception as e:
        lyrics_song = {"lyrics": ""}
        print(e)
    finally:
        # DELITING PLAYLIST
        ytmusic.delete_playlist(playlistId)

    return lyrics_song


# SongName = "Paralyzed NF"
def Lyrics(SongName):
    global Author
    global Flag
    try:
        print('Первый')
        lyrics = GetLyricsMain(SongName)
        return lyrics
    except:
        try:
            print('Второй')
            lyrics = GetLyricsSecond(SongName)
            return lyrics
        except:
            # insti333@gmail.com QGPZ26MP
            print('Третий')
            lyrics = GetLyricsThird(SongName)
            return lyrics


# print(Lyrics(SongName))
