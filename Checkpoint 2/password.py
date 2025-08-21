import getpass

def check_password(p):
   guess = input("Enter password: ")
   if p == guess:
     print("Correct password")
    print("The program has ended")

def main():
   password = getpass.getpass("Set password: ")
   input("Press enter to log in.")
   check_password(password)
main()

