print("========== STUDENT GRADES ============")
grades = []

# Ask user to input five times (student grades)
for i in range(0, 5):
    num = float(input('Enter Grade : '))
    grades.append(num)

# Adding all grades of student to find the sum to be used later to calculate for the average
sum = 0
for num in grades:
    sum += num

# Calculating the average of the student's grade and finding the maximum and minimum of grades the student entered.
average = sum / len(grades)
print('======================================')
print('Average :', average)
print('Maximum :', max(grades))
print('Minimum :', min(grades))
