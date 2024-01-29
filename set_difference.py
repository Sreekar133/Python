plane_mode = {"1":"car", "2" : "plane"}

items = {"bag",
         "shoe",
         "dress",
         "cap",
         "knife",
         "scissors"}

restricted_items = {"knife","scissors"}

print("please type the mode of travel")
for key,value in plane_mode.items():
    print(f"{key}:{value}")

mode = "-"

while mode not in plane_mode:
    mode = input("<")

if mode == "2":
    # for restricted_item in restricted_items:
        items.difference_update(restricted_items)


for item in sorted(items):
    print(item)

