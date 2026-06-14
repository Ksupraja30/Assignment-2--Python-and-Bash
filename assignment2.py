student_grades = {}
while True:
    print("\n--- Student Grades Manager ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        # 1. Add a new student and grade
        name = input("Enter the student's name: ").strip()
        if name in student_grades:
            print(f"'{name}' already exists! Use option 2 to update their grade.")
        else:
            grade = input(f"Enter the grade for {name}: ").strip()
            student_grades[name] = grade
            print(f"Added a new student : {name} with grade {grade}.")
            
    elif choice == '2':
        # 2. Update an existing student's grade
        name = input("Enter the name of the student to update: ").strip()
        if name in student_grades:
            new_grade = input(f"Enter the new grade for {name}: ").strip()
            student_grades[name] = new_grade
            print(f"Updated  an existing student: {name}'s grade to {new_grade}.")
        else:
            print(f"Student '{name}' not found in the records.")
            
    elif choice == '3':
        # 3. Print all student grades
        if not student_grades:
            print("No student records available yet.")
        else:
            print("\n--- All Current Student Records With name & grade ---")
            for name, grade in student_grades.items():
                print(f"Student: {name} | Grade: {grade}")
                
    elif choice == '4':
        # 4. Exit the program
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
