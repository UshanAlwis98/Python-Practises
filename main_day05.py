# fruits = ["Apple", "Woodapple", "Pineapple", "Peach", "Pears"]
#
# # indentation is very important in this kind of for loops
# for fruitOneByOne in fruits:
#     print( fruitOneByOne)
#     print(fruitOneByOne + " Pie")
#     print(fruits)



# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# student_count = 0
# for number_of_students in student_heights:
#     student_count += 1
# print(f"number of students {student_count}")
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"Total height is {total_height}")
#
# average_height_of_students = total_height/student_count
# print(f"Average height of the students {average_height_of_students}")


# ChatGPT Python List and For Loop Challenge Find the Most Frequent Element in a List

elements = input("Enter numbers separated by space: ").split()
for i in range(len(elements)):
    elements[i] = int(elements[i])

max_count = 0
most_frequent = elements[0]
count = 0
for i in range(len(elements)):

    for j in range(len(elements)):
        if elements[i] == elements[j]:
            count += 1
    if count > max_count:
        max_count = count
        most_frequent = elements[i]

print(f"Most frequent element: {most_frequent} (appeared {max_count} times)")
