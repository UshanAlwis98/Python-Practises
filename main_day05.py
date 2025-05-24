# fruits = ["Apple", "Woodapple", "Pineapple", "Peach", "Pears"]
#
# # indentation is very important in this kind of for loops
# for fruitOneByOne in fruits:
#     print( fruitOneByOne)
#     print(fruitOneByOne + " Pie")
#     print(fruits)



# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height


no_of_students = 0
for student in student_heights:
    no_of_students += 1

average_height = round(total_height / no_of_students)

print(f"total height = {total_height}")
print(f"number of students = {no_of_students}")
print(f"average height = {average_height}")