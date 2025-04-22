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
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
letter_T = name1.lower().count("t") + name2.lower().count("t")
letter_R = name1.lower().count("r") + name2.lower().count("r")
letter_U = name1.lower().count("u") + name2.lower().count("u")
letter_E = name1.lower().count("e") + name2.lower().count("e")
total_letters_in_true = print(letter_T + letter_R + letter_U + letter_E)

letter_L = name1.lower().count("l") + name2.lower().count("l")
letter_O = name1.lower().count("o") + name2.lower().count("o")
letter_V = name1.lower().count("v") + name2.lower().count("v")
letter_love_E = name1.lower().count("e") + name2.lower().count("e")
total_letters_in_love = print(letter_L + letter_O + letter_V + letter_love_E)

print(total_letters_in_true and total_letters_in_love)




















