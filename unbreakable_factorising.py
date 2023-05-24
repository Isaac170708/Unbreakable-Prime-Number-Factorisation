import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_a(p):
    a = (p - 3) // 4
    return a


# Prompt the user to enter the unbreakable prime number
p = int(input("Enter the unbreakable prime number (p): "))

# Check if the entered number is a prime number
if not is_prime(p):
    print("The entered number is not a prime number.")
else:
    # Call the function to calculate the value of a
    a = find_a(p)
    # Print the value of a
    print(f"The value of a is: {a}")
