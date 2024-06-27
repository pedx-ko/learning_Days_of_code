'give to studens a grade'


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Neville": 62
}

students_Grades = {}
for studen in student_scores:
    score = student_scores[studen]
    if score > 90:
        students_Grades[studen] = "Outstanding"
    elif score > 80:
        students_Grades[studen] = "Exceeds Expectations"
    elif score > 70:
        students_Grades[studen] = "Acceptable"
    else:
        students_Grades[studen] = "Fail"

print(student_scores)
print()
print(students_Grades)
