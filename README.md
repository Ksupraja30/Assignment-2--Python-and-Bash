# Assignment-2--Python-and-Bash
**1. Grade Checker
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"
here we used a basic if else statement to carry out marks and all.**

score = int(input("Enter student score: \n "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"    
print(f"The grade for a student score of {score} is : ", grade)


**2 Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.**

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

**Used dictionary and basic operations. Using if else:
3.Write to a File
Write a program to create a text file and write some content to it.**

# Write file
f = open('data.txt', 'w')
f.write("Hi, I am Supraja Writing this file, "
        "This content was written using Python.\n Welcome to file handling!")
f.close()
print("Successfully created 'data.txt' and wrote content to it.")

**Using file functions like write and open.
4. Read from a File
We used open in read mode and file.read to read and print to display.**

# Read file
f = open('data.txt', 'r')
data = f.read()
print(data)
f.close()

***Output Screenshots and program files are attached : 
Assignment1.py and that Output1.png, 
Assignment2.py and that Output2.png, 
Assignment3.py and that Output3and4.png***

