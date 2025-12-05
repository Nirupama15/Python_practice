def parse_csv(fname):
    lines = open(fname).readlines()
    return [l.strip().split(',') for l in lines]

fname = input("Enter CSV file: ")
print(parse_csv(fname))