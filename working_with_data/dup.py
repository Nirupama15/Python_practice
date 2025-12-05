def dups(l):
    ele = []
    dup = []
    for i in l:
        if i in ele and i not in dup:
            dup.append(i)
        else:
            ele.append(i)
    return dup
numbers = input("Enter numbers: ")
num_list = [x for x in numbers.split(",")]
print("Duplicate elements:", dups(num_list))
