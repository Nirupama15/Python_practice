def reverse_lines(fname):
    lines = open(fname).readlines()
    for line in reversed(lines):
        print(line, end='')
fname = input("Enter filename: ")
reverse_lines(fname)