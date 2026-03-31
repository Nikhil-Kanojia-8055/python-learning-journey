# using of spam comment is defined as atext containing following keywords
# "make a lot of money","buy now","suscribe this","click this" wap for detecting it

p1 = "make a lot of money"
p2= "buy now"
p3 = "suscribe this"
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is spam comment")

else:
    print("this comment is not a spam")



    