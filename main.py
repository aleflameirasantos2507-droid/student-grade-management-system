students = []
student = []

while True:
    student.append(input('Name: ').capitalize())
    student.append(float(input('Grade 1: ')))
    student.append(float(input('Grade 2: ')))

    students.append(student[:])
    student.clear()

    option = input('Would you like to continue? ').strip().upper()

    if option == 'N':
        break

print('No      NAME               AVERAGE')
print('=' * 30)

for index, record in enumerate(students):
    average = (record[1] + record[2]) / 2
    print(f'{index:<3} {record[0]:<18} {average:.2f}')

print('=' * 30)

while True:
    student_index = int(input('Show grades for which student? (999 to exit): '))

    if student_index == 999:
        break

    if 0 <= student_index < len(students):
        print(f"{students[student_index][0]}'s grades are [{students[student_index][1]}, {students[student_index][2]}]")
    else:
        print('Invalid student number.')

    print()
