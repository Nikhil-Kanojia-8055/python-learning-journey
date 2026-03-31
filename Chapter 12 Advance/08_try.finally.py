def main():
    try:
        a = int(input("Hey! ,Enter a number :"))
        print(a) # If we will write this much code only and if user give the input as string so the code will crash
        return

    except Exception as e:
        print(e)
        return
    
    # Even if the functions returns the finally will run
    finally: 
# Here if finally keyword is not defined & simply written print so in every case the print statement will not execute and if finally keyword is there so in every case it will execute always either there is return or not
        print("I am inside finally")

main()