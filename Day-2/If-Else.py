# Write a program to check student Grade
# If marks >= 90 then Grade A
# If marks >= 80 then Grade B
# If marks >= 70 then Grade C
# If marks >= 60 then Grade D
# If marks >= 50 then Grade E
# If marks < 50 then Grade F

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Grade F")

# Second way
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
elif marks >= 50 and marks < 60:
    print("Grade E")
elif marks >= 0 and marks < 50:
    print("Grade F")
else:
    print("Grade F")