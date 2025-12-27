print("Student Marks Management System")

name = input("Enter student name: ")

math = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = math + science + english
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
