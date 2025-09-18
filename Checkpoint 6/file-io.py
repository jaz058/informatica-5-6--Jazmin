# names = []

# for i in range(3):
#     name = input("What´s is your name?")
#     #print(f"{i}. Hello{name}")
#     names.append(name)
#     print(names)

# for name in sorted(names):
#     print(f" Hello {name}")

name=input("What´s your name?")
file= open("name.txt","a")
file.write(f"{name}\n")
file.close()