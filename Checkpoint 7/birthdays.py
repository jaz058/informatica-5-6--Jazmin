birthdays = {
    "Luna":"22/01/2008",
    "Luisa":"25/10/2007",
    "Jose":"19/05/2008"
}
print(birthdays)
while True:
    look = input("You are looking for: ")


    if look in birthdays:
        print((birthdays[look]), "is the birthday of", look)
        break

    else:
        print ("I do not have birthday information for", look)
        birthday = input("What is their birthday?")
        birthdays [look] = birthday
        print (birthdays)

    