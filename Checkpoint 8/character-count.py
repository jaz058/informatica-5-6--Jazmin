def character_count (message , dictionary):
    for charecter in message:
     dictionary.setdefault(charecter,0)
    dictionary[charecter] += 1
    print(dictionary)

message = input ("Write a message")
dictionary = {}
character_count(message, dictionary)