# i = 0
# while i < 10:
#     print("i is now {0}".format(i))
#     i+=1


# exits = ["north" , "south" , "east" , "west"]
#
# choosen_exit = ""
#
# while choosen_exit not in exits:
#     choosen_exit = input("enter your direction")
#     if choosen_exit.casefold() == "quit":
#         print("game over")
#         break
# print("you are returned back")

# for i in range(0,12):
#     if i > 0 and i % 11 ==0:
#         break
#     print(i)

# for i in range(0,21):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)

# for i in range(21):
#     if i%3!=0 or i%5!=0:
#         print(x)


i=1
while i<=20:
    if i%3!=0 and i%5!=0:
        print(i)
    i=i+1



