def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

print(biggie_size([-1, 3, 5, -5]))


def count_positives(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    lst[-1] = count
    return lst

print(count_positives([-1,1,1,1]))


def sum_total(lst):
    total = 0
    for num in lst:
        total += num
    return total


print(sum_total([1,2,3,4]))




def average(lst):
    if len(lst) == 0:
        return 0
    return sum_total(lst) / len(lst)

print(average([1,2,3,4]))





def length(lst):
    return len(lst)

print(length([1,2,3,4]))





def maximum(lst):
    if len(lst) == 0:
        return False
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(maximum([1,2,3,4]))



def minimum(lst):
    if len(lst) == 0:
        return False
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

print(minimum([1,2,3,4]))



def ultimate_analysis(lst):
    if len(lst) == 0:
        return {
            'sumTotal': 0,
            'average': 0,
            'minimum': False,
            'maximum': False,
            'length': 0
        }
    
    return {
        'sumTotal': sum_total(lst),
        'average': average(lst),
        'minimum': minimum(lst),
        'maximum': maximum(lst),
        'length': length(lst)
    }

print(ultimate_analysis([1,2,3,4]))


def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst

print(reverse_list([1,2,3,4]))