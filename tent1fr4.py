user_numbers = []
pos_num = []
neg_num = []



try:
    with open("positiva.txt", "r") as file:
        pos_num = [int(line.strip()) for line in file]
except FileNotFoundError:
    pass



try:
    with open("negativa.txt", "r") as file:
        neg_num = [int(line.strip()) for line in file]
except FileNotFoundError:
    pass



while True:
    user_input = input("Ange ett nummer att lägga till i listan eller q för att avsluta: ")

    if user_input == "q":
        with open ("positiva.txt", "w") as file:
            for num in sorted(set(pos_num)):
                file.write(f"{num}\n")
                    
            
            with open ("negativa.txt", "w") as file:
                for num in sorted(set(neg_num)):
                    file.write(f"{num}\n")
                    
        break
    
    try:
    
        number = int(user_input)
        user_numbers.append(number)
    

        if number > 0 and number not in pos_num:
            pos_num.append(number)
        elif number < 0 and number not in neg_num:
            neg_num.append(number)
        
    except ValueError:
        print("Vänligen ange giltigt nummer eller q")