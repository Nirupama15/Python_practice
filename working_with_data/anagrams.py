words = input("Enter the words: ").split(",")

dic = {}

for w in words:
    key = tuple(sorted(w)) 

    if key not in dic:
        dic[key] = []

    dic[key].append(w)

print(list(dic.values()))
