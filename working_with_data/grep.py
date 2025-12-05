def grep(fname, pattern):
    lines = open(fname).readlines()
    for l in lines:
        if pattern in l:
            print(l, end='')
fname = input("Enter filename: ")
pattern = input("Enter pattern: ")
grep(fname, pattern)