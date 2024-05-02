grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
def calculate_avarage(sublist):
    return sum(sublist) / len(sublist)
averages = [calculate_avarage(sublist) for sublist in grades]
print(averages)

students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
sorted_students = sorted(students)
print(sorted_students)
student_grades = {student: average for student, average in zip(sorted_students, averages)}
print(student_grades)

