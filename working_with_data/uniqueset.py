def unique(l):
    return list(set(l))
numbers = input("Enter the numbers: ")
num_list = [int(x) for x in numbers.split(",")]
print("Unique Elements: ", unique(num_list))