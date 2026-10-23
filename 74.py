def favorite_songs(playlist):
    songs = []
    for song in sorted(playlist, key=lambda song: song["plays"], reverse=True):
        songs.append(song["title"])

    return songs[0:2]
        

print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))