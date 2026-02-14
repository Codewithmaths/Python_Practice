Name =  input("Enter your Name :")
subject1 = int(input("Enter first subject mark :"))
subject2 = int(input("Enter second subject mark :"))
subject3 = int(input("Enter third subject mark :"))

totalMarks = subject1 + subject2 + subject3
totalPercent = totalMarks*100/300

if subject1 >= 33 and subject2 >= 33 and subject3 >= 33 and totalPercent >= 40:
    print(f"{Name} pass with {totalPercent}%")
else:
    print(f"{Name} fail got {totalPercent}%")