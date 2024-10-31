user_input = input("ange en text: ")

vertical_word = []
f = open("demofile.txt", "a")

for ch in user_input:
    print(ch)
    vertical_word.append(ch)
    f.write(f"{ch}\n")
    
    
print(vertical_word)





