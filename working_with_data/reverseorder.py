def reverse_line(fname):
    lines = open(fname).readlines()
    for l in lines:
        print(l[::-1])
fname = input("Enter filename: ")
reverse_line(fname)