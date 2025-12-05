def filter(f, lis):
    return [l for l in lis if f(l)]

def even(n):
    return n % 2 == 0

numbers = input("Enter numbers: ")
number_list = [int(x) for x in numbers.split(",")]
print(filter(even, number_list))