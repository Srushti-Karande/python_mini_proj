# Grade Calculator for 5 Subjects
total = 0

for i in range(1, 6):
    subject = input("Enter subject name: ")
    marks = int(input("Enter marks out of 100: "))
    total = total + marks

percentage = total / 5

print("\nTotal Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 35:
    print("Grade: D")
else:
    print("Grade: F")
