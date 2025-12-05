import os
dir = input("Enter folder path: ")
for name in os.listdir(dir):
    print(name)
