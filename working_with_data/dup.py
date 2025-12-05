def dups(l):
    elements = []
    dup = []
    for item in l:
        if item in elements and item not in dup:
            dup.append(item)
        else:
            elements.append(item)
    return dup
numbers = input("Enter numbers: ")
num_list = [x for x in numbers.split(",")]
print("Duplicate elements:", dups(num_list))
