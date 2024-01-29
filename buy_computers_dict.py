availabe_parts = {"1":"computer",
                  "2":"monitor",
                  "3":"keyboard",
                  "4":"mouse",
                  "5":"hdmi cable",
                  "6":"dvd drive"}

current_choice = None
while current_choice !=0:
    if current_choice in availabe_parts:
        chosen_part = availabe_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        for key,values in availabe_parts.items():
            print(f"{key}:{values} in dictionary")
        print("0 to finish")

    current_choice = input("< ")