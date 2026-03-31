# wap for find out wheather a student is passes or fail if it require 40% and atleast 33%in each subject to pass
# assume 3 subject and take marks as input from the user
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))     
sub3 = int(input("Enter marks of subject 3: "))

# cheak for total percentage
total_percentage =100*(sub1 +sub2 +sub3)/300

if(total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You are passed",total_percentage)

else:
    print("you failed",total_percentage)