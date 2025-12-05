fname = input("Enter the filename: ")
with open(fname) as f:
    words = f.read().split()

fr = {}
for w in words:
    fr[w] = fr.get(w, 0) + 1

sorted_items = sorted(fr.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_items:
    print(word, count)
