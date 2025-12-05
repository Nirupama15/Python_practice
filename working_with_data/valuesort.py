def valuesort(d):
    keys = sorted(d.keys())
    return [d[k] for k in keys]

dic = {}
n = int(input("Enter number of pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic[key] = value

print(valuesort(dic))