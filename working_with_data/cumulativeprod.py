elements = input("Enter numbers: ")
numbers = [int(n) for n in elements.split(",")]
c = []
prod = 1
for num in numbers:
    prod *= num
    c.append(prod)
print("Cumulative product:", c)


