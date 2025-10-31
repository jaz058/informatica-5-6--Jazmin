# def divide(a,b):
#     if b==0:
#         raise ValueError("Hey! You cannot divide by zero.")
#     return a / b

# print(divide(1,2))
# print(divide(2,0))
def main():
    factorial()

def factorial(n):
    if n <= 0:
        raise ValueError(f"The input was negative or zero: {n}")
    else:
        new_n = 1
        print(list(range(2, n + 1)))
        for 1 in range(2, n + 1):
            new_n = new_n*1
        return new_n 
main()   