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
# student_count = 0
# for number_of_students in student_heights:
#     student_count += 1
# print(f"number of students {student_count}")

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height is {total_height}")