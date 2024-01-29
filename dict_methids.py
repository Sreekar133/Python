d = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"}

pantry_items = ["chicken","spam","egg","bread","lemon"]

v=d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)



#
# d2 = {
#     "7" : "lucky seven",
#     "10" : "ten",
#     "3":"this is the new three"
#
# }
# d.update(d2)
# # print(d)
#
# # # for key,values in d.items():
# # #     print(key,values)
# #
# # d.update(enumerate(pantry_items))
# # for key,values in d.items():
# #     print(key,values)
#
# #
# # # new_dict = dict.fromkeys(pantry_items,0)
# # # print(new_dict)
# #
# # keys = d.keys()
# # print(keys)

