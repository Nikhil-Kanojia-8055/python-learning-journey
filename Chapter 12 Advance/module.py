def myFunc():
    print("Hello World!")

if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running the code")
    myFunc()
    print(__name__) # In __name__ it will print the file name (main)