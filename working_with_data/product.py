def product(numbers):
    re = 1
    for n in numbers:
        re = re * n
    return re

nums = input("Enter numbers: ").split(",")
numbers = [int(n) for n in nums]
print("Product =", product(numbers))
