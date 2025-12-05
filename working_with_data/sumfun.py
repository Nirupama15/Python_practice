def strings_add(words):
    re = ""
    for w in words:
        re += w
    return re

words_list = input("Enter strings: ").split(",")
print("Concatenated string:", strings_add(words_list))

