username_and_password = {

  'KalleAnka': '1234asdf', 

  'Mimmi_PIG': 'Hösten2023', 

  'Jann3Langben': 'password', 

  'Sebastianmentor': 'PyAi23Masters'

  }



while True:

  print('1. Logga in!')

  print('2. Skapa ny användare!')

  print('3. Avsluta')

  choice = input('>>>')



  if choice == '1':


    username = input("Ange användarnamn: ")
    password = input("Ange lösenord: ")



    if username in username_and_password and username_and_password[username] == password:
        print("Woop woop, du är inloggad!")
    else:
        print("Felaktig inloggning.")
    

  elif choice == '2':

    new_username = input("Ange nytt användarnamn: ")
    
    if new_username in username_and_password:
        print("Användarnamnet finns redan. Försök med ett annat.")
    else:
        new_password = input("Ange ett lösenord (minst 6 tecken)<. ")
        
        if len(new_password) > 6:
            confirm_password = input("Bekräfta lösenordet: ")

            if new_password == confirm_password:
                username_and_password[new_username] = new_password
                print("Användare skapad!")
            else:
                print("Lösenordet matchade inte. Försök igen.")
        else:
            print("Lösenordet måste vara längre än 6 tecken.")

  elif choice == '3':
    print("Programmet avslutas.")
    break

  else:

    print('Felaktigt val')