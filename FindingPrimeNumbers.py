def generate_prime():
    prime_numbers = []
    for number in range(2, 20 + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime_numbers.append(number)

    print("Prime numbers between 1 to 20 are:", prime_numbers)

generate_prime()
