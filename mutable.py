# shopping_list = ["milk", "eggs", "rice" , "spam" , "bread"]
#
# another_list = shopping_list
# print(id(shopping_list))
# print(id(another_list))
#
# shopping_list.append("cookies")
# print(shopping_list)
# print(id(shopping_list))
# print(another_list)
#
# a=b=c=d=f=another_list
#
# print(a)
# b.append("cream")
# print(shopping_list)

current_choice = "_"
computer_parts=[]

while current choice != '0':
    if current_choice in "12345":
        print("adding {0}".format(current_choice)
    else:
        print("please add options from list below:")
        print("1: computer")
        print("2:monitor")
        print("3:keyboard")
        print("4:mouse")
        print("5:mouse mat")
        Print("0:to finish")
    current_choice = input()