def grade(score):
    if not isinstance(score, int) or score < 0 or score > 100:
        return "Ogiltigt"
    
    if score > 90:
        return "A"
    
    if score > 80:
        return "B"
    
    if score > 70:
        return "C"
    
    if score > 60:
        return "D"
    else:
        return "F"
    
    
print(grade(int(input("Hur många poäng fick du?"))))
