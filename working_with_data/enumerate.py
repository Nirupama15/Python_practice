def enumerate(l):
    return [(i, l[i]) for i in range(len(l))]

items = input("Enter items: ")
item_list = items.split(",")
print(enumerate(item_list))