# Random Numbers
import random
import  my_Module_day04
# print(random.randint(100 ,200)) #randint will return integer between 100 and 102
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
states_of_america = [ "Arizona", "California", "Indiana", "Montana", "Nevada", "Washington"  ]

print(states_of_america[6])