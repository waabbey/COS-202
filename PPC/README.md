# Personal Pocket CGPA Calculator (PPC)

## Project Title

Personal Pocket CGPA Calculator (PPC)

## Aim

The aim of this project is to develop a Python program that calculates a student's Cumulative Grade Point Average (CGPA) on a 5.0 grading scale using Python's selection control statements ("if", "elif", and "else").

## Objectives

- To accept course information from the user.
- To determine the grade and grade point based on the score entered.
- To calculate the quality points for each course.
- To compute the total CGPA.
- To display the student's degree classification (remark).

## Program Description

The Personal Pocket CGPA Calculator is a console-based application developed in Python. The program prompts the user to enter the number of courses taken, the course title, course unit, and score for each course. Using selection control statements, the program determines the appropriate letter grade and grade point for each score.

The program then calculates the quality points by multiplying the course unit by the corresponding grade point. After processing all courses, it computes the CGPA by dividing the total quality points by the total course units. Finally, it displays the student's CGPA and the corresponding degree classification.

## Grading System

| Score | Grade | Grade Point |
|-------|-------|-------------|
| 70 – 100 | A | 5 |
| 60 – 69 | B | 4 |
| 50 – 59 | C | 3 |
| 45 – 49 | D | 2 |
| 40 – 44 | E | 1 |
| 0 – 39 | F | 0 |

## Degree Classification

| CGPA | Remark |
|------|--------|
| 4.50 – 5.00 | First Class |
| 3.50 – 4.49 | Second Class Upper |
| 2.40 – 3.49 | Second Class Lower |
| 1.50 – 2.39 | Third Class |
| 1.00 – 1.49 | Pass |
| Below 1.00 | Fail |

## Algorithm

1. Start the program.

2. Ask the user to enter the number of courses.

3. Repeat the following for each course:
   - Enter the course title.
   - Enter the course unit.
   - Enter the course score.
   - Use "if", "elif", and "else" statements to determine the grade and grade point.
   - Calculate the quality point.
   - Add the quality point to the total grade points.
   - Add the course unit to the total units.

4. Calculate the CGPA using:
   ```
   CGPA = Total Grade Points ÷ Total Course Units
   ```

5. Display the total units, total grade points, CGPA, and remark.

6. End the program.

## Software Requirements

- Python 3.x
- Any Python IDE (IDLE, PyCharm, VS Code, Spyder) or a command-line terminal.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/waabbey/COS-202.git
   cd COS-202/PPC
   ```

2. Ensure Python 3.x is installed on your system.

3. Run the calculator:
   ```bash
   python cgpa_calculator.py
   ```

## Usage

### How to Use

1. **Start the Program**: Run the script using Python.

2. **Enter Number of Courses**: Input the total number of courses you want to calculate CGPA for.

3. **For Each Course, Enter**:
   - **Course Title**: Name of the course (e.g., "Data Structures")
   - **Course Unit**: Credit hours/units for the course (e.g., 3)
   - **Course Score**: Your score in the course out of 100 (e.g., 85)

4. **View Results**: The program will display:
   - Grade for each course (A, B, C, D, E, or F)
   - Grade point for each course
   - Quality point for each course
   - Total units
   - Total grade points
   - Final CGPA (out of 5.0)
   - Degree classification (remark)

### Example Session

```
=============================================
      PERSONAL POCKET CGPA CALCULATOR
=============================================
Enter the number of courses: 3

Course 1
Course Title: Data Structures
Course Unit: 3
Course Score (0 - 100): 85
Grade: A
Grade Point: 5
Quality Point: 15

Course 2
Course Title: Web Development
Course Unit: 4
Course Score (0 - 100): 72
Grade: A
Grade Point: 5
Quality Point: 20

Course 3
Course Title: Database Design
Course Unit: 3
Course Score (0 - 100): 65
Grade: B
Grade Point: 4
Quality Point: 12

=============================================
TOTAL UNITS: 10
TOTAL GRADE POINTS: 47
CGPA = 4.70 / 5.00
REMARK: FIRST CLASS
=============================================
```

## Code Structure

### Main Components

1. **Input Section**: Collects the number of courses
2. **Loop Section**: Iterates through each course:
   - Accepts course information
   - Determines grade and grade point using selection statements
   - Calculates quality points
   - Accumulates totals
3. **Calculation Section**: Computes the final CGPA
4. **Output Section**: Displays results and degree classification

### Key Variables

- `num_courses`: Number of courses to process
- `total_grade_points`: Accumulation of quality points
- `total_units`: Accumulation of course units
- `score`: Student's score in a course
- `grade`: Letter grade (A-F)
- `gp`: Grade point value (0-5)
- `quality_point`: Grade point × course unit
- `cgpa`: Final CGPA calculation

## Learning Outcomes

This project demonstrates practical knowledge of:
- **Selection Control Statements**: Using if, elif, and else statements for decision-making
- **Loops**: Using for loops to process multiple courses
- **Arithmetic Operations**: Calculating grade points and CGPA
- **User Input/Output**: Handling console input and formatted output
- **String Formatting**: Using `.format()` for displaying results with specific decimal places
- **Variable Management**: Accumulating and managing total values

## Conclusion

The Personal Pocket CGPA Calculator successfully automates the computation of a student's CGPA on a 5.0 scale. It demonstrates the practical use of Python's selection control statements, loops, arithmetic operations, and user input handling, making it a useful academic tool for students.

## License

This project is part of the COS-202 coursework.

## Author

Created by: waabbey

## Support

For issues, suggestions, or questions, please open an issue in the repository.
