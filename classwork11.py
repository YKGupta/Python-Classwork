# 1. After 10 years what will be the age of all the students, print them
# 2. Before 4 years, what would be the age of all the students
# 3. Assume that the every year the age of students increase by 3, 
#    so what should be the age of students after 3 years

ageOfStudents = [10, 11, 12, 14, 15]
#1
print("Age of students after 10 years:-")
for i in ageOfStudents:
    print(i + 10)
#2
print("Age of students before 4 years:-")
for i in ageOfStudents:
    print(i-4)
#3
print("Age of students after 3 years for increment of 3 years to age per year:-")
for i in ageOfStudents:
    print(i + (3*3))