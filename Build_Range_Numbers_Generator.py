# Build a Range of Numbers Generator

def range_of_numbers(start_num, end_num):
    if end_num == start_num :
        return [start_num]
    return [start_num] + range_of_numbers(start_num + 1 , end_num)


print(range_of_numbers(1, 5))
print(range_of_numbers(6, 9))
print(range_of_numbers(4, 4))
print(range_of_numbers(10, 15))