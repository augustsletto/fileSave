def is_number_in_string(number, big_number):
    
    str_number = str(number)
    
    if str_number in big_number:
        return True
    else:
        return False
    


def frequence_of_0_to_9(big_number):
    
    
    
    frequency = [0] * 10
    
    for digit in big_number:
        frequency[int(digit)] += 1
    return frequency

#print(is_number_in_string(12, "093840981219433084"))


big_number = "111445"
print(frequence_of_0_to_9(big_number))