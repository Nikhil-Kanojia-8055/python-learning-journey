# Store a multiplication table generated in problem 3 in file named table.txt

n = int(input("enter a number :"))
table = [n*i for i in range (1,11)]
with open("table.txt" , "a") as f:
    f.write(str(table) + "\n")
