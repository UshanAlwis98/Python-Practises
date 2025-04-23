# Control Flow
# water_level = 90
#
# if water_level>80:
#     print("Water Level is high")
# else:
#     print("Water level is low")


# Nested If Statements
# age = int(input("Enter your age\n"))
#
# if age>5:
#     if age<12:
#         print("Your ticket price is $7")
#     elif age<18:
#         print("Your ticket price is $12")
#     elif age<22:
#         print("Your ticket price is $25")
#     else:
#         print("You are an adult")
# else:
#     print("You can not ride the RollerCoaster")

# Control Flow Final Challange(Chat GPT Question)

# first_digit = input("Enter Digit 1\n")
#
# if first_digit == "4":
#     second_digit = input("Enter Digit 2\n")
#
#     if first_digit == "4" and second_digit == "8":
#         third_digit = input("Enter Digit 3\n")
#
#
#         if first_digit == "4" and second_digit == "8" and third_digit == "7":
#             fourth_digit = input("Enter Digit 4\n")
#
#             if first_digit == "4" and second_digit == "8" and third_digit == "7" and fourth_digit == "2":
#                 print("✅ Code cracked! Welcome, Agent.")
#
#             else:
#                 print("Wrong digit. Access denied!")
#
#         else:
#             print("Wrong digit. Access denied!")
#
#     else:
#         print("Wrong digit. Access denied!")
# else:
#     print("Wrong digit. Access denied!")


# Pizza Challange

# First Answer

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? S, M, or L
# add_pepperoni = input()  # Do you want pepperoni? Y or N
# extra_cheese = input()  # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# price_of_small_pizza = 15
# price_of_medium_pizza = 20
# price_of_large_pizza =25
#
# if size == "S":
#    if add_pepperoni == "Y":
#       if extra_cheese == "Y":
#         print(f"Your final bill is: ${price_of_small_pizza + 3}")
#       else:
#                 print(f"Your final bill is: ${price_of_small_pizza +2}")
#
#    elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
#        print(f"Your final bill is: ${price_of_small_pizza + 1}")
#
#    else:
#        print(f"Your final bill is: ${price_of_small_pizza}")
#
# elif size == "M":
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             print(f"Your final bill is: ${price_of_medium_pizza + 4}")
#         else:
#             print(f"Your final bill is: ${price_of_medium_pizza + 3}")
#
#     elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
#         print(f"Your final bill is: ${price_of_medium_pizza + 1}")
#
#     else:
#         print(f"Your final bill is: ${price_of_medium_pizza}")
#
# else:
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             print(f"Your final bill is: ${price_of_large_pizza + 4}")
#         else:
#             print(f"Your final bill is: ${price_of_large_pizza + 3}")
#
#     elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
#         print(f"Your final bill is: ${price_of_large_pizza + 1}")
#
#     else:
#         print(f"Your final bill is: ${price_of_large_pizza}")



# Second Answer
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? S, M, or L
# add_pepperoni = input()  # Do you want pepperoni? Y or N
# extra_cheese = input()  # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# Bill =0
# if size == "S":
#    Bill += 15
# elif size == "M":
#     Bill += 20
# else:
#     Bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         Bill += 2
#     else:
#         Bill += 3
#
# if extra_cheese == "Y" :
#     Bill +=1
#
# print(f"Your final bill is:{Bill}")

# Logical Operator Challange beginning
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# # Count letters for TRUE
# combined_names = (name1 + name2).lower()
# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# true_score = t + r + u + e
#
# # Count letters for LOVE
# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e2 = combined_names.count("e")
# love_score = l + o + v + e2
#
# # Combine scores as string and convert back to int
# final_score = int(str(true_score) + str(love_score))
#
# # Output based on score Condition
# if final_score < 10 or final_score > 90:
#     print(f"Your score is {final_score}, you go together like coke and mentos.")
# elif 40 <= final_score <= 50:
#     print(f"Your score is {final_score}, you are alright together.")
# else:
#     print(f"Your score is {final_score}.")


# Final Project of Day 03
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



direction = input("You're at a cross road.Where do u want to go ? Type left or right\n")



if direction == "left":
    swim_wait = input(
        "You come to a lake.There is an island in the middle of the lake. Type 'wait' to wait for a boat.Type 'swim' to swim across \n")
    if swim_wait == "wait":
        door = input(
            "You arrived at the island unharmed. There is a house with 3 doors.one red , one yellow and one blue. Which color do you choose ?\n")
        if door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "Red":
            print("Burned by fire.Game Over.")
        elif door == "yellow":
            print("You Win")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")










