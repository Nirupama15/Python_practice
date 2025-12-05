def group(l, num_groups):
    n = len(l)
    size = n // num_groups        
    rem = n % num_groups   
    grp = []
    start = 0
    for i in range(num_groups):
        end = start + size + (1 if i < rem else 0)
        grp.append(l[start:end])
        start = end
    return grp


list_in = input("Enter numbers: ")
numbers = [x for x in list_in.split(",")]


num_grp = int(input("Enter the number of groups: "))

print("Grouped list:", group(numbers, num_grp))
