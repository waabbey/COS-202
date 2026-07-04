print("=" * 45)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 45)

num_courses = int(input("Enter the number of courses: "))

total_grade_points = 0
total_units = 0

for i in range(1, num_courses + 1):
    print(f"\nCourse {i}")

    course = input("Course Title: ")
    unit = int(input("Course Unit: "))
    score = float(input("Course Score (0 - 100): "))

    # Selection Control Statements
    if score >= 70:
        grade = "A"
        gp = 5
    elif score >= 60:
        grade = "B"
        gp = 4
    elif score >= 50:
        grade = "C"
        gp = 3
    elif score >= 45:
        grade = "D"
        gp = 2
    elif score >= 40:
        grade = "E"
        gp = 1
    else:
        grade = "F"
        gp = 0

    quality_point = gp * unit

    total_grade_points += quality_point
    total_units += unit

    print("Grade:", grade)
    print("Grade Point:", gp)
    print("Quality Point:", quality_point)

# Calculate CGPA
cgpa = total_grade_points / total_units

print("\n" + "=" * 45)
print("TOTAL UNITS:", total_units)
print("TOTAL GRADE POINTS:", total_grade_points)
print("CGPA = {:.2f} / 5.00".format(cgpa))

# CGPA Remark using Selection Statements
if cgpa >= 4.50:
    remark = "FIRST CLASS"
elif cgpa >= 3.50:
    remark = "SECOND CLASS UPPER"
elif cgpa >= 2.40:
    remark = "SECOND CLASS LOWER"
elif cgpa >= 1.50:
    remark = "THIRD CLASS"
elif cgpa >= 1.00:
    remark = "PASS"
else:
    remark = "FAIL"

print("REMARK:", remark)
print("=" * 45)
