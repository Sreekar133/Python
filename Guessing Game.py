# import random
# highest = 10
# answer = random.randint(0,highest)
# print(answer)
#
# guess = int(input("enter the number from 1 to highest: "))
#
# if guess == answer:
#     print("you have guessed it correctly")
# else:
#     if guess < answer:
#         print("please guess higher")
#     else:
#         print("please guess lower")


# import random
# highest = 10
# answer = random.randint(0,highest)
# print(answer)
# guess = 0
# print("enter the number from 1 to highest: ")
#
# while guess != answer:
#     guess = int(input())
#
#     if guess == answer:
#         print("you have guessed it correctly")
#     else:
#         if guess < answer:
#             print("please guess higher")
#         else:
#             print("please guess lower")

import random
highest = 10
answer = random.randint(0,highest)
print(answer)
guess = 0

print("enter the number from 1 to 10: ")

while guess != answer:
    guess=int(input("enter the digits"))

    if guess == answer:
        print("you have guesses it correctly")
        break
    else:
        if guess < answer:
            print("guess higher")
        else:
            print("guess lower")



