def unique(l, key=None):
    elements = []
    uni = []
    for item in l:
        k = key(item) if key else item
        if k not in uni:
            elements.append(item)
            uni.append(k)
    return elements

strings = input("Enter strings: ")
strings = strings.split(",")
print("Unique items:", unique(strings, key=lambda s: s.lower()))

