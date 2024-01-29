# import copy
# lion_list = ["scary", "big", "cat"]
# elephant_list = ["big", "grey", "wrinkled"]
# teddy_list = ["cuddly", "stuffed"]
# animals = {
#     "lion" : lion_list,
#     "elephant" :elephant_list,
#     "teddy" : teddy_list
# }
# #perform a shallow copy
# # things = animals.copy()
# things = copy.deepcopy(animals)
# things = {
#     "lion" : lion_list,
#     "elephant" : elephant_list,
#     "teddy" : teddy_list
#
# }
# print(things["teddy"])
# print(animals["teddy"])
# print()
# teddy_list.append("toy")
# # things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])

choice = "-"
while choice !="0":
    if choice in set("12345"):
        print(f"you have selected {choice}")
    else:
        print("please select from above")
        print("1:\t Learn Python")
        print("2 \t Learn Stats")
        print("3 \t Learn SQL")
        print("4 \t Learn Machine Learning")
        print("5 \t Learn Deep Learning")

    choice = input()