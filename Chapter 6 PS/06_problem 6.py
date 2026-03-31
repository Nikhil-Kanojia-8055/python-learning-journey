# WAP to calculate the grade of a student from his marks from following scheme
# # 90-100 A      
# # 80-90 B
# # 70-80 C
# # 60-70 D
# # 50-60 E
# # <50 F

marks = int(input("Enter your marks:"))

if(marks<=100 or marks>=90):
    print("your grade is excellent")
elif(marks<80 or marks>=70):
    print("your grade is B")
elif(marks<70 or marks>=60):
    print("your grade is C")
elif(marks<60 or marks>=50):
    print("your grade is D")
elif(marks<50 or marks>=50):
    print("your grade is E")
elif(marks<50 ):
    print("your grade is F")

print("your MARKS",marks)


