#esercizio_8.7

def make_album(artist_name:str, album_title:str, n_song:int = 0) -> dict [str:str]:
    return {"name":artist_name, "album":album_title, "n":n_song}

user_1 = make_album("Bruno", "Parla di me", 7)
user_2 = make_album("Giovanna", "D'Arco")
user_3 = make_album("Bob", "Marley")

print(user_1["name"])
print(user_1["album"])
print(user_1["n"])

print(user_2["name"])
print(user_2["album"])

print(user_3["name"])
print(user_3["album"])