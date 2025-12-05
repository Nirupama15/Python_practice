import os
def count_files(dir):
    count = 0
    for file in os.listdir(dir):
        if file.endswith(".py"):
            count += 1
    return count

path = input("Enter path: ")
print("Number of python files:", count_files(path))
