# # s = "malayalam"
# # v = ""
# #
# # for i in s:
# #     v = i+v
# # if s==v:
# #     print("palindrome")
# # else:
# #     print("not palindrome")
#
#
# s ="eye"
#
#
# s1 = s[::-1]
# if s==s1:
#     print("it is palindrome")
# else:
#     print("not palindrome")


d={"ineuron":{"a":14,"b":10,"c":4},"course":{"d":45,"e":34,"f":1},
     "g" : 354 , "h" :[45,6,7,8,9,3] , 'i' :(45,34,2) , 'k' :"sudh"}

lst =[]

# for i in d.values():
#     if type(i) == dict:
#         lst.append(max(i.values()))
#     elif type(i) == list:
#         lst.append(max(i))
#     elif type(i) == tuple:
#         lst.append(max(i))
#     elif type(i) == str:
#         pass
#     else:
#         lst.append(i)
# print(max(lst))


l = []

for i in d.values():
    if type(i) == dict:
        l.append(max(i.values()))
    elif type(i) == list:
        l.append(max(i))
    elif type(i) == tuple:
        l.append(max(i))
    elif type(i) == str:
        pass
    else:
        l.append(i)
print(max(l))



