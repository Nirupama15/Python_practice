import os
import time
dir = input("Enter folder path: ").strip()
for name in os.listdir(dir):
    path = dir + name
    info = os.stat(path)
    print(name, info.st_size, time.asctime(time.localtime(info.st_mtime)), sep="\t")
