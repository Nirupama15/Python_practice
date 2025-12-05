def lensort(strs):
    return sorted(strs, key=lambda s: len(s))

strings = input("Enter words separated by spaces: ")
words = [w for w in strings.split(",")]
sorted_words = lensort(words)
print("Words sorted by length:", sorted_words)
