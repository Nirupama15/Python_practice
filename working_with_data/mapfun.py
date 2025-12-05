def map(f, items):
    return [f(item) for item in items]

def square(x):
    return x * x

numbers = input("Enter numbers: ")
number_list = [int(x) for x in numbers.split(",")]
print(map(square, number_list))