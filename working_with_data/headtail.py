def head(fname, n=10):
    lines = open(fname).readlines()
    for l in lines[:n]:
        print(l, end='')

def tail(fname, n=10):
    lines = open(fname).readlines()
    for l in lines[-n:]:
        print(l, end='')
fname = input("Enter filename: ")
ch = input("Enter 'head' or 'tail': ")

if ch == 'head':
    head(fname)
else:
    tail(fname)
    