#Studant name
student_name = input("Enter the student's name: ")

#Take the five grades and store them in a list
grades = []
grades.append(float(input("Enter grade 1: ")))
grades.append(float(input("Enter grade 2: ")))
grades.append(float(input("Enter grade 3: ")))
grades.append(float(input("Enter grade 4: ")))
grades.append(float(input("Enter grade 5: ")))

#Calculate the average
average = sum(grades) / len(grades)

#Determine the letter grade bassed on the average
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

#Print the results
print(f"\n{student_name}")
print(f"average: {average:.1f}")
print(f"letter grade: {letter_grade}")
