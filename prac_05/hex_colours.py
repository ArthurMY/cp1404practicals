COLOR_NAME = {"absolute zero": "#0048ba", "aliceblue": "#f0f8ff", "aqua": "#00ffff"}
print(COLOR_NAME)
get_color_name = input("Enter the color: ").lower()

while get_color_name != "":
    if get_color_name in COLOR_NAME:
        print(f"{COLOR_NAME[get_color_name]}")
    else:
        print("Invalid input")
    get_color_name = input("Enter the color: ").lower()
