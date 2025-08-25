import random
print("Welcome to the Goblin Game")
print("The best game ever")
player_name= input("Write your name")
print(player_name,"Can you find the Goblin")
print("|_|" *5)
goblin_position = random.randint(1,5)
keep_trying = True
while keep_trying:
    guessed_position =int(input ("Can you guess where the goblin is? "))
    if guessed_position==goblin_position:
        print("Good luck you find the Goblin")
        keep_trying = False
    else: print("No")
