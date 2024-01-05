def find_max_element(test):
    
    
    maxelement = test[0]
    
    for x in test:
        if x > maxelement:
            maxelement = x
    
    return maxelement

# Example Usage:
list = [10, 5, 20, 3, 2, 8, 20, 2]
result = find_max_element(list)

print(f"Maximum element in the list: {result}")
