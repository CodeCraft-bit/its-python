#esercizio_8.8

def make_album(artist_name:str, album_title:str, n_song:int = None) -> dict [str:str]:
    album ={"artist":artist_name, "title":album_title}
    if n_song:
        album["n_song"] = n_song
    return album
    
while True:
    artist_name = input("Write the name of the artist (write quit to stop) ").lower()
    if artist_name == "quit":
        break
    album_title = input("Write the name of the album ")
    n_song = input("You want to enter the number of songs (yes/no) ")
    if n_song == "yes":
        n_song:int = input("Enter the number of songs: ")
        b_b= make_album(artist_name, album_title, n_song)
        print(b_b)
    else:
        a_a = make_album(artist_name, album_title)
        print(a_a)
   


