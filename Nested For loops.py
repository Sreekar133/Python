# # for i in range(1,13):
# #     for j in range(1,13):
# #         print(j,"multipiled with", i , "is" ,i*j)
# #         print("--------------------------")
#
# # cricket_list=["bat","ball","pads","gloves","thigh pad"]
# # for i in cricket_list:
# #     if i == "pads":
# #             continue
# #     print(i)
#
# grocceries = ["oil", "rice", "sugar" , "water" , "dry fruits"]
#
# item_to_find = "sugar"
# found_at = None
#
# # for i in range(len(grocceries)):
# #     if grocceries[i] == item_to_find:
# #         found_at = i
# #         break
# # print("the position of item is found at" , found_at)
#
# if item_to_find in grocceries:
#     found_at = grocceries.index(item_to_find)
# if found_at is not None:
#     print("position is" , found_at)
# else:
#     print("none")


list = ["a","b","c","d","e"]

item_to_find = "b"

found = None

# for i in range(len(list)):
#     if list[i] == item_to_find:
#         found = i
# print("the position is" , found)

if item_to_find in list:
    found = list.index(item_to_find)
print("the position is" , found)


