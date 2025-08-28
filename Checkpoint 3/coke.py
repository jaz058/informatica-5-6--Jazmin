def main():

    name= input("Please type your name: ")
    amount=0
    while amount < 50:
        coin = int(input("Please insert your coin: "))
        if coin == 25 or coin == 10 or coin==5:
            amount = amount + coin
            print(amount)
        else:
            print("We recive $25 $10 $5:")

    change = amount - 50
    print('Here’s a Coke for', name)
    print('Here your change', change)

main()