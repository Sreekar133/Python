# file = open("Python wiki.txt", "r")
#
# for line in file:
#     (print(line.rstrip()))
#
# file.close()

# with open("Python wiki.txt","r") as file:
#     for line in file:
#         print(line.rstrip())

# with open("Python wiki.txt","r") as file:
#     lines=file.readlines()
# print(lines)
#

with open("Python wiki.txt","r") as file:
    while True:

        line=file.readline().rstrip()
        print(line)
        if "Python" in line.casefold():
            break