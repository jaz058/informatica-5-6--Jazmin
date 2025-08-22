def main():
    n= int(input("Enter a integer number: "))
    integer_number(n)

def integer_number(n):
    negative= (n*(-1))
    positive=(n)

    if n > 0:
     print("The absolut value is: "(positive))
    else:
     print("The absolut value is: ", (negative))
      
main()