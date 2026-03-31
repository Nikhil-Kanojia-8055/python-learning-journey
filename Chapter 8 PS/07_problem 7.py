# WAP convert inches to cms
def inches_to_cms( inches ):
    return inches *2.54

n  = int(input("Enter the number in inches : "))
print(f"The corresponding value in cms is{inches_to_cms(n)}")