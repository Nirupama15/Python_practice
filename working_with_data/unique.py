def unique(l):
    uni = []
    for item in l:
        if item not in uni:
            uni.append(item)
    return uni

numbers = input("Enter numbers: ")
num_list = [x for x in numbers.split(",")]
print("Unique elements:", unique(num_list))
   