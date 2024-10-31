artist_and_albums = {

    "Stevie Wonder": ["Talking book", "Hotter then July"],

    "Pink Floyd": ["The Wall", "Whish you were here", "Pulse"], 

    "Lady Gaga": [], 

    "Elvis Presley": []

}







while True:

    print("1. Lägg till artist")
    
    
    
    
    print("2. Lägg till album till artist")

    print("3. Avsluta")

    choice = input(">>>")



    if choice == "1":

        user_input_artist = input("Lägg till en artist i listan: ")
        if user_input_artist not in artist_and_albums:
            artist_and_albums[user_input_artist] = []
        else:
            print("Oh no, den finns redan!!!")
            
        print(artist_and_albums)


    elif choice == "2":
        
        user_input_artist = input("Vilken artist vill du komma åt: ")
        if user_input_artist in artist_and_albums:
            
            user_input_album = input("Skriv ett album du vill lägga tillhörande artisten: ")
            if user_input_album not in artist_and_albums:
                artist_and_albums[user_input_artist].append(user_input_album)
        else:
            print("Artist saknas!")
        print(artist_and_albums)        
    elif choice == "3":

        break

    else:

        print("Ogiltligt val")