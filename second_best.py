def second_smallest_and_largest(lst):
    
    
    lst.sort()
    new_lst = []
    
    new_lst.append(lst[1])
    new_lst.append(lst[-1])
    return new_lst

    
    

lista = [5, 99, 7, 33, 76, 8, 444, 2,999, 6, 45344, 33, 45, 5, 6,66, 7, -1, -434, 3, -555555]
    
print(second_smallest_and_largest(lista))