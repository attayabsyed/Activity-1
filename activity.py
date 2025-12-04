students = []

def add_student():
    name = input("Enter student name: ")
    while not name:
        print("Name cannot be empty!")
        name = input("Enter student name: ")
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                print("Age cannot be negative!")
            else:
                break
        except ValueError:
            print("Please enter a valid number!")
    while True:
        try:
            marks = float(input("Enter marks: "))
            if marks < 0:  
                print("Marks cannot be negative!")
            else:
                break
        except ValueError:
            print("Please enter a valid number!")
    students.append({"name": name, "age": age, "marks": marks})
    print("Student added successfully!\n")

def view_all_students():
    if not students:
        print("No student found \n")
        return
    print(".....All Students.....")
    i = 1
    for s in students:
        print(f"{i}. Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
        i += 1
    print()

def search_student():
    name = input("Enter name to search: ")
    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found → Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}\n")
            found = True
            break
    if not found:
        print("Student not found.\n")

def update_marks():
    name = input("Enter name of student to update marks: ")
    for s in students:
        if s["name"].lower() == name.lower():
            while True:
                try:
                    new_marks = float(input("Enter new marks: "))
                    if new_marks < 0:
                        print("Marks cannot be negative!")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number!")
            s["marks"] = new_marks
            print("Marks updated successfully!\n")
            return
    print("Student not found.\n")

while True:
    print("Student Management Console")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Update Student Marks")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        print("Have a nice day")
        break
    else:
        print("Invalid choice! Please select 1–5.\n")
