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

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
price_of_small_pizza = 15
price_of_medium_pizza = 20
price_of_large_pizza =25

if size == "S":
   if add_pepperoni == "Y":
      if extra_cheese == "Y":
        print(f"Your final bill is: ${price_of_small_pizza + 3}")
      else:
                print(f"Your final bill is: ${price_of_small_pizza +2}")

   elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
       print(f"Your final bill is: ${price_of_small_pizza + 1}")

   else:
       print(f"Your final bill is: ${price_of_small_pizza}")

elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${price_of_medium_pizza + 4}")
        else:
            print(f"Your final bill is: ${price_of_medium_pizza + 3}")

    elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
        print(f"Your final bill is: ${price_of_medium_pizza + 1}")

    else:
        print(f"Your final bill is: ${price_of_medium_pizza}")

else:
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${price_of_large_pizza + 4}")
        else:
            print(f"Your final bill is: ${price_of_large_pizza + 3}")

    elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
        print(f"Your final bill is: ${price_of_large_pizza + 1}")

    else:
        print(f"Your final bill is: ${price_of_large_pizza}")

