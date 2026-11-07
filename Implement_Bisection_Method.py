def square_root_bisection(number, tolerance =1e-7, max_iterations= 50):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    elif number in (0, 1):
        print(f'The square root of {number} is {number}')
        return number

    low= 0
    high= max(1, number)

    for _ in range(max_iterations):
        root = (low + high) / 2

        if root * root < number:
            low = root

        else:
            high = root

        if high - low <= tolerance:
            root = (low + high) / 2
            print(f"The square root of {number} is approximately {root}")
            return root
        
        
    
    print(f"Failed to converge within {max_iterations} iterations")
    return None

print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(1))