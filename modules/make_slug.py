def make_slug(name):
    name = name.replace(' ', '-')
    while '--' in name:
        name = name.replace('--', '-')
    name = name.strip('-')
    return name

text = input("Enter text: ")
s = make_slug(text)
print("Result:", s)