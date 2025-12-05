def valuesort(d):
    return sorted(d.values())

dic = {}
n = int(input("Enter the number of pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic[key] = value

print(valuesort(dic))
