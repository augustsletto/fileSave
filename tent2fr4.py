def main():
    numbers = []
    
    # Samla in heltal från användaren
    while True:
        user_input = input("Mata in ett heltal (eller 'q' för att avsluta): ")
        if user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Vänligen mata in ett giltigt heltal.")
    
    # Filtrera ut udda och jämna tal
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Sortera talen och räkna förekomster
    odd_count = {num: odd_numbers.count(num) for num in sorted(set(odd_numbers))}
    even_count = {num: even_numbers.count(num) for num in sorted(set(even_numbers))}
    
    # Skriv udda tal till fil
    with open("Udda.txt", "w") as odd_file:
        for num, count in odd_count.items():
            odd_file.write(f"{num} förekommer {count} gång(er)\n")
    
    # Skriv jämna tal till fil
    with open("Jämna.txt", "w") as even_file:
        for num, count in even_count.items():
            even_file.write(f"{num} förekommer {count} gång(er)\n")

    print("Udda och jämna tal har sparats till respektive filer!")

if __name__ == "__main__":
    main()
