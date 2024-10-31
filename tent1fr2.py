def divisible_by_3(string):
    
    divby3 = []
    totalnumber = 0
    
    for ch in string:
        divby3.append(ch)
        totalnumber += int(ch)
        
    
    print(totalnumber)
        
    if totalnumber % 3 == 0:
        return True

    
# def divisible_by_3(string):
#   totalnumber = sum(int(ch) for ch in string)
# return totalnumber % 3 == 0



def divisible_by_4(string):
    
    divby4 = []
    totalnumber = 0
    
    for ch in string:
        divby4.append(ch)
        totalnumber += int(ch)
    
    print(totalnumber)
        
    if totalnumber % 4 == 0:
        return True

    




def divisible_by_11(string):
    divby11 = []
    totalnumber = 0
    
    for ch in string:
        divby11.append(ch)
        totalnumber += int(ch)
        
    print(totalnumber)
    if totalnumber % 11 == 0:
        return True



is_div_by_3 = divisible_by_3("2453623462346")
is_div_by_4 = divisible_by_4("234623462346234664632")
is_div_by_11 = divisible_by_11("646223462346234623")

print(f"Is divisible by 3: {is_div_by_3}")
print(f"Is divisible by 4: {is_div_by_4}")
print(f"Is divisible by 11: {is_div_by_11}")
