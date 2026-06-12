def log_bottles_recycled(player_turtle):
    print("---Welcome to the Beverage Return Scheme Tracker---")
    while True:
        user_input = input("How many plastic bottles did your family recycle today? ").strip()
        try:
            user_recycle = int(user_input)
            if user_recycle < 0:
                print("You can't have a negative amount of bottles! Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a Whole Number (e.g. 10, 20, 30).")
    money_saved = user_recycle * 0.1
    weight_gained = user_recycle // 5
    landfill_vol_saved = user_recycle * 25
    player_turtle.weight_grams += weight_gained

    print("---Your Real-World Impact---")
    print(f"You saved ${money_saved:.2f} & prevented {landfill_vol_saved}cm^3 of waste from entering the semakau landfill!")

    print("---IKEA Ice-Cream Tracker---")
    if money_saved >= 0.50:
        ice_cream = int(money_saved//0.5)
        print(f"Yay! You have earned enough for {ice_cream} IKEA ice-cream(s) :-) ")
    else:
        bottles_needed = 5 - user_recycle
        print(f"Tip: Recycle {bottles_needed} bottle(s) more to secure an IKEA ice-cream.")

    print("---Your Turtle's Status---")
    print(f"{player_turtle.name} gained {weight_gained}g from your recycling effort!")