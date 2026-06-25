
student1 = ("Alice", 101, "A")
student2 = ("Bob", 102, "B")
student3 = ("Charlie", 103, "A+")

students = (student1, student2, student3)

print("Student Records:")
print(students)


print("\nFirst Student:", students[0])
print("Name of Second Student:", students[1][0])


print("\nLast Student:", students[-1])
print("Grade of Last Student:", students[-1][2])

print("\nAll Students:")
for student in students:
    print(f"Name: {student[0]}, Roll No: {student[1]}, Grade: {student[2]}")

reversed_students = students[::-1]
print("\nReversed Records:")
print(reversed_students)

top_two = students[:2]
print("\nFirst Two Students:")
print(top_two)

student4 = ("David", 104, "B+")
updated_students = students + (student4,)

print("\nAfter Adding New Student:")
print(updated_students)

try:
    students[0][1] = 999
except TypeError as e:
    print("\nTuple Immutability Test:")
    print("Error:", e)
