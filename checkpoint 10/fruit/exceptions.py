# #Syntax error 
# #print("Hello world")

# try:
#     x=int(input("What´s x?"))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number")

# def spam(divided_by):
#     return 42 / divided_by

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            number = int(input_str)
            if number < 100 and number >= 0:
                return number 
        except ValueError :
            pass
number = read_small_integer()
print(number, "to the power of three is", number**3)