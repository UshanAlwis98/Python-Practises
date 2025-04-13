# Subscripting Example 01
# print("Hello"[0])

# Subscripting Example 02
# my_First_Word = "Hello"
# my_Second_Word = "Vowel"
# my_Inputted_Word = input("Give me your idea\n")
# my_New_Word = print(my_First_Word[1]+my_Second_Word[2]+my_Inputted_Word[3])

# Type Casting Example 01
# num_Char_Name = len(input("What's Your Name?\n"))
# new_num_Char_Name = str(num_Char_Name)
# print("My name has " + new_num_Char_Name + " Characters.")

# Type Casting Example 02 - Add Integer and casted Float
# print(100 + float("70.5"))

# Type Casting Example 03 - Add Casted two Strings
# print(str(70)+str(3221))

# Mathematical Operators
# print(5+3)
# print(5-3)
# print(5 * 3)
# print(16/4)
# print(3 ** 2)


# Mathematical Operators Sequence

# PEMDAS
# Parentheses ()
# Exponenets **
# Multiplication *
# Division /
# Addition +
# Substraction -

# print(3 * 3 + 3 / 3 -3 )
# print(round(8/3,2))

# floor_division = (8 // 3)
# print(type(floor_division))

# F String

# score = 5
# isWinning = True
# height = 3.2
#
#
# print(f"Your Current Score is {score} and height is {height} the winning value is {isWinning}")


# Day 02 Final Task

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# print("Welcome to the tip calculator!")
# total_amount = input("What was the total bill?\n")
# tip_amount = input("How much tip would you like to give? 10, 12, or 15?\n")
# num_of_people = input("How many people to split the bill?\n")
#
# each_balance = ((float(total_amount)/100) * (100+float(tip_amount))) / int(num_of_people)
# print(round(each_balance,2))



# Python Day 02 Challange

first_input = input("Enter the first Number\n")
second_input = input("Enter the second Number\n")

# Addition Operation
addition_input = float(first_input)+float(second_input)
print(f"The addition of  {first_input} and {second_input} is {addition_input}")