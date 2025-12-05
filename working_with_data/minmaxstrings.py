strings = input("Enter strings: ")
words = [w for w in strings.split(",")]
print("Min:", min(words))
print("Max:", max(words))
