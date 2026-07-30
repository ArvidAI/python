def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        last_line = ' '.join(str(j) for j in range(1, n + 1))
        return last_line


print(number_pattern(4))
print(number_pattern(12))