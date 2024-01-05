def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    factorial = 1
    
    for i in range(2, n + 1):
        factorial *= i
    
    return factorial

n = int(input("Please enter a number to find the factorial: "))
result = factorial(n)

print(result)
