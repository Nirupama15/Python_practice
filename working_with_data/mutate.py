def mutate(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    
    for i in range(len(word) + 1):
        for c in letters:
            result.append(word[:i] + c + word[i:])
    
    for i in range(len(word)):
        result.append(word[:i] + word[i+1:])
    
    for i in range(len(word)):
        for c in letters:
            result.append(word[:i] + c + word[i+1:])
    
    for i in range(len(word) - 1):
        result.append(word[:i] + word[i+1] + word[i] + word[i+2:])
    
    return result
word = input("Enter a word: ")
words = mutate(word)
print("Total mutations:", len(words))
test = input("Enter a word to check if it's a mutation: ")
print(test in words)