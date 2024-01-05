def reverse_string(string):
    str = ""
    for i in string:
        str = i + str
    return str
string = "I am learning Python"
print(reverse_string(string))
