def invertdict(d):
    res = {}
    for key, value in d.items():
        res[value] = key
    return res

dic = {}
n = int(input("Enter number of pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic[key] = value

print(invertdict(dic))