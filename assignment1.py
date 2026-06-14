# This program takes a student's score as input and outputs the corresponding letter grade based on standard grading scale.

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
print(f"The grade for a student score of {score} is : {grade}")