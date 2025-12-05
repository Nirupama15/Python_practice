def zip(l1, l2):
    return [(l1[i], l2[i]) for i in range(len(l1))]
l1 = input("Enter first list: ")
l1 = l1.split(",")
l2 = input("Enter second list: ")
l2 = l2.split(",")
print(zip(l1, l2))