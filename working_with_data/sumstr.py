x = input("Enter strings: ")
words = [w for w in x.split(",")]
result = ""
for w in words:
    result += w
print(result)
