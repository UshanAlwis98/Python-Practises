# Control Flow
# water_level = 90
#
# if water_level>80:
#     print("Water Level is high")
# else:
#     print("Water level is low")


# Nested If Statements
age = int(input("Enter your age\n"))

if age>5:
    if age<12:
        print("Your ticket price is $7")
    elif age<18:
        print("Your ticket price is $12")
    elif age<22:
        print("Your ticket price is $25")
    else:
        print("You are an adult")
else:
    print("You can not ride the RollerCoaster")