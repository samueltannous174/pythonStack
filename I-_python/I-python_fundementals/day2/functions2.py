
def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result



def print_and_return(lst):
    print(lst[0])
    return lst[1]



def first_plus_length(lst):
    return lst[0] + len(lst)




def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    
    second_value = lst[1]
    new_list = []
    
    for num in lst:
        if num > second_value:
            new_list.append(num)
    
    print(len(new_list))
    return new_list

def length_and_value(size, value):
    result = []
    for i in range(size):
        result.append(value)
    return result


print (length_and_value(4,7)) 

# values_greater_than_second([5,2,3,2,1,4])   



