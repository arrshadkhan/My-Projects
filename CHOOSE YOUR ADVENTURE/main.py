name = input("Enter your name: ")
print("Welcome,", name, "to this adventure ")
answer = input("Do you wanna play game? (yes/no) ").lower()
if answer == "yes":
    question = input(
        "you are on a dirt road, it has come to an end you can go left or right. Which way do you like to go? "
    ).lower()
    if question == "left":
        question = input(
            "You come to river. you can walk around it or swim across? Type walk to walk around and swim to swim across: "
        ).lower()
        if question == "walk":
            print("you walked for many miles, ran out of water and lost the game")
        elif question == "swim":
            print("you swam acrross and were eaten by an alligator.")
        else:
            print("Not a valid input, You lose!")
    elif question == "right":
        question = input(
            "You come to bridge it looks wobbly do you want cross it or head back (cross/back)? "
        ).lower()
        if question == "cross":
            question = input(
                "You cross the bridge and meet the stranger do you wanna talk to them (yes/no)"
            ).lower()
            if question == "yes":
                print(" You talked to stranger and they gave you gold, YOU WIN!")
            elif question == "no":
                print("You ignore the stranger they offend , You loose!")
            else:
                print("Not a valid input, You lose!")
        elif question == "back":
            print("You go back and loose.")
        else:
            print("Not a valid input, You lose!")
    else:
        print("Not a  valid input.")
elif answer == "no":
    print("Okay", name, "have a great day !")
else:
    print("Not a valid input..")
