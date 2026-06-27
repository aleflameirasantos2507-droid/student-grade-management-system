# Student Grade Management System

A beginner-friendly Python project that manages student records by storing names and grades, calculating averages, and displaying individual scores on demand.

## Features

- Stores multiple students and their grades
- Calculates each student's average grade
- Displays a formatted grade report
- Allows users to view individual student grades
- Uses nested lists to organize data

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/student-grade-management-system.git
```

2. Navigate to the project folder:

```bash
cd student-grade-management-system
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
Name: Alice
Grade 1: 8.5
Grade 2: 9.0
Would you like to continue? Y

Name: Bob
Grade 1: 7.0
Grade 2: 6.5
Would you like to continue? N
```

### Output

```text
No      NAME               AVERAGE
==============================
0       Alice               8.75
1       Bob                 6.75
==============================

Show grades for which student? 0

Alice's grades are [8.5, 9.0]
```

## Learning Objectives

This project demonstrates:

- Nested lists
- List copying (`[:]`)
- Loops (`while` and `for`)
- The `enumerate()` function
- Data storage and retrieval
- Average calculation
- User interaction

## Data Structure

Each student is stored as:

```python
[
    "Student Name",
    grade1,
    grade2
]
```

The complete database is a list of these records:

```python
students = [
    ["Alice", 8.5, 9.0],
    ["Bob", 7.0, 6.5]
]
```
