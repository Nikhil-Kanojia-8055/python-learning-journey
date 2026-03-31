# WAP for print multiplication table of given number

def multiplication(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

multiplication(7)