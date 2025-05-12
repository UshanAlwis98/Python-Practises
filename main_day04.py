# Random Numbers
import random
import  my_Module_day04
# print(random.randint(100 ,200)) #randint will return integer between 100 and 200 , 100 and 200 will also come
# print(my_Module_day04.pi_value)

random_float = random.random()  #random.random() will give floating point number between 0.0 and 1.0 not including 1

# print(random_float * 5)
#
# # Head and Tail Challenge
# # Write your code below this line 👇
# import random
#
# random_num = random.randint(0,1)
# print(random_num)
#
# if random_num == 1:
#   print("Heads")
# else:
#   print("Tails")
# # Hint: Remember to import the random module first. 🎲

# Python list data structure

# states_of_america = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
#     "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
#     "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
#     "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
#     "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
#     "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
#     "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
#     "Wisconsin", "Wyoming"
# ]
#
#
# print(states_of_america[-50])

# Python Names Challenge with List,Randomization

# import  random
# my_names_list = input("Enter names\n")
# names_seperated = my_names_list.split(", ")
# names_count = len(names_seperated)
#
# name_random_index = random.randint(0,names_count-1)
#
# pick_a_name = names_seperated[name_random_index]
# print(f"Your randomely picked name is {pick_a_name}")


# List Index out of range error
# states_of_america = [ "Arizona", "California", "Indiana", "Montana", "Nevada", "Washington"  ]
#
# print(states_of_america[6])

# states_of_america = [ "Arizona", "California", "Indiana", "Montana", "Nevada", "Washington"  ]
# total_states = len(states_of_america)
#
# print(states_of_america[total_states-1])
#
#
# fruits = ["Apple", "Papaya", "Pineapple", "Orange", "Banana", "Water Melon"]
# vegetables = ["Brinjal", "Beans", "Leaks", "Union", "Potetos"]
#
# dry_drozen = [fruits,vegetables]
# print(dry_drozen)


# Treasure Map Challenge
# line1 = ["⬜️","️⬜️","️⬜️"]
# # line2 = ["⬜️","⬜️","️⬜️"]
# # line3 = ["⬜️️","⬜️️","⬜️️"]
# # map = [line1, line2, line3]
# # print("Hiding your treasure! X marks the spot.")
# # position = input() # Where do you want to put the treasure?
# # # 🚨 Don't change the code above 👆
# #
# # # Write your code below this row 👇
# # letter = ["A", "B", "C"]
# # Letter_index = letter.index(position[0].upper())
# # Number_index = int(position[1]) -1
# # map[Number_index][Letter_index] = "X"
# # # Write your code above this row 👆
# #
# # # 🚨 Don't change the code below 👇
# # print(f"{line1}\n{line2}\n{line3}")



# ChatGPT Python list challenge 01
# from itertools import chain
# data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flattened = list(chain(*data))
#
#
# def is_odd(x):
#     return x % 2 != 0
#
# odd_numbers = filter(is_odd, flattened)
#
# for x in odd_numbers:
#   print(x*x)

# ChatGPT Challenge 2 accepted.
data = [5, 12, 7, 3, 9, 15, 4]

# data.append(10)
# print(data)
# data.remove(data[0]) #Remove first element
# print(data)
# data.insert(1,20) # Put 20 as second element
# print(data)
# data[2] = 100  # Replace third element
# new_list = data[-3:]  # Last 3 elements
# print(data)
# print(new_list)

# Rock paper scissors challenge
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Display prompt
print("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.")

# User input
user_input = input()

# Validate and convert input
if user_input not in ["1", "2", "3"]:
    print("Invalid input. Please enter 1, 2, or 3.")
else:
    user_choice = int(user_input) - 1  # Convert to 0-based index
    elements_ascii = [rock, paper, scissors]
    elements_name = ["rock", "paper", "scissors"]

    print("You chose:")
    print(elements_ascii[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(elements_ascii[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie.")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You won!")
    else:
        print("You lost!")
