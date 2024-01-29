# for i in range(1,13):
#     print(i,i**2,i**3)
# print("*" * 80)

name = input("enter your name")
age =int(input("enter you age  {0}? ". format(name)))
if age < 18:
    print("He is not eligible")
elif age==18:
    print("he is just eligible")
else:
    print("he is eligible to vote")