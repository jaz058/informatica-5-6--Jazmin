# #Syntax error 
# #print("Hello world")

# try:
#     x=int(input("What´s x?"))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number")

def spam(divided_by):
    return 42 / divided_by

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
