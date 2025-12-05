def product(numbers):
    re = 1
    for n in numbers:
        re = re * n
    return re

n = int(input("Enter a number: "))
numbers = list(range(1, n + 1))
print("Factorial =", product(numbers))
