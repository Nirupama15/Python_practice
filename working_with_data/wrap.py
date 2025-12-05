def wrap(fname, w):
    lines = open(fname).readlines()
    for l in lines:
        l = l.strip()
        while len(l) > w:
            print(l[:w])
            l = l[w:]
        print(l)
fname = input("Enter filename: ")
w = int(input("Enter width: "))
wrap(fname, w)