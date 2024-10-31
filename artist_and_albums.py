artist_and_albums = {

    "Stevie Wonder": ["Talking book", "Hotter then July"],

    "Pink Floyd": ["The Wall", "Whish you were here", "Pulse"], 

    "Lady Gaga": [], 

    "Elvis Presley": []

}







while True:

    
    print("1. Lägg till artist")
    add_artist = input("Namn på artist: ")
    
    if add_artist not in artist_and_albums:
        artist_and_albums[add_artist] = []
        
    else:
        print("Oh no, den finns redan")
        
    
    print(artist_and_albums)
    
    print("2. Lägg till album till artist")
    artist_name = input("Namn på artist: ")
    if artist_name in artist_and_albums:
        artist_and_albums[artist_name] = input("Ange album")

    else:
        print("Artist saknas!")

    print(artist_and_albums)
    print("3. Avsluta")

    choice = input(">>>")



    if choice == "1":

        pass



    elif choice == "2":

        pass

   

    elif choice == "3":

        break

    else:

        print("Ogiltligt val")