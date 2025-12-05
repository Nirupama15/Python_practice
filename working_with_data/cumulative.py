elements = input("Enter numbers: ")
numbers = [int(n) for n in elements.split(",")]
c = []
total = 0
for num in numbers:
    total += num
    c.append(total)
print("Cumulative sum:", c)
