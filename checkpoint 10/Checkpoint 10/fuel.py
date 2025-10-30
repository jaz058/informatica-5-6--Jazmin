def main():
    fuel = input("Enter your fuel as fraction:").split("/")
    num =  int(fuel[0])
    den = int([1])
    percentage = round ((num/den) * 100)
    if percentage <= 1:
        percentage = "E"
    elif percentage >= 99:
        percentage="F"
    elif percentage > 100 :
        print("Inavlid Input")
    print(percentage)

    print(fuel)
    
main
    