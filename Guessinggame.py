# answer =5
#
# guess=int(input("enter the number between 1 to 10:"))
#
# if guess < answer:
#     print("the number is lower")
#     guess=int(input("guess the number"))
#     if guess == answer:
#         print("well done")
#     else:
#         print("please guess the correct number")
# elif guess == answer:
#     print("the number is correct")
# elif guess > answer:
#     print("the number is higher")
#     guess = int(input("guess the number"))
#     if guess == answer:
#         print("well done")
#     else:
#         print("please guess the correct number")
# else:
#     print("error")

# x=7
# y=5
#
# if x>y:
#     print("x is greater")
# elif x==y:
#     print("x and y are equal")
# else:
#     print("y is greater")


answer =5

guess = int(input("guess the number from 1 to 10:"))

if guess!=answer:
    print("they are not equal")
    if guess > answer:
        print("guess lower number")
    else:
        print("guess high number")
elif guess==answer:
    print("they are equal")

