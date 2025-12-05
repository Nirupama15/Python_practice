def extsort(fi):
    return sorted(fi, key=lambda f: f.split('.')[-1])
files = input("Enter filenames: ")
files_list = files.split(",")
print(extsort(files_list))