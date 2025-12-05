def center_align(fname):
    lines = open(fname).readlines()
    max_len = 0
    for l in lines:
        if len(l.strip()) > max_len:
            max_len = len(l.strip())
    
    for l in lines:
        l = l.strip()
        space = (max_len - len(l)) // 2
        print(' ' * space + l)

fname = input("Enter filename: ")
center_align(fname)