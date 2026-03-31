# WAP to find out wheather a given post is talking about "Nikhil" or not

post = input("enter your post name:")

if("nikhil".lower() in post.lower() ):
# this is used to tell that if we have nikhil or Nikhil or NIKHIL in post it will consider all as same
    print("this post is talking about nikhil")


else:
    print("this post is not talking about nikhil")



# post2 = "Nikhil is  good boy, he is very intelligent"

# if("nikhil" in post2 or "Nikhil" in post2):
#     print("this post is talking about nikhil")

# else:
#     print("this post is not talking about nikhil")