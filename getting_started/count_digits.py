def count_digits(n):
    return len(str(abs(n)))

number = int(input("Enter a number: "))
print("Number of digits:", count_digits(number))
