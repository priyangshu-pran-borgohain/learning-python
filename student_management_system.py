students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added successfully!\n")

def show_students():
    if not students:
        print("No students found.\n")
        return
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']} | Marks: {student['marks']}")
    print()

def show_result():
    name = input("Enter student name to check result: ")
    for student in students:
        if student["name"].lower() == name.lower():
            percentage = student["marks"]
            print("Name:", student["name"])
            print("Percentage:", percentage)
            print("Result:", "PASS" if percentage >= 40 else "FAIL")
            print()
            return
    print("Student not found.\n")

while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        show_result()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
