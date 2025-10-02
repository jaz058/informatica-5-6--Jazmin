def character_count (message , dictionary):
    for charecter in message:
        dictionary.setdefault(charecter,0)
        dictionary[charecter] += 1
    print(dictionary)

    print(sum(dictionary.values()))


# #Alternative 1
# dictionary = {}
# values_list = list(dictionary.values())
# print(values_list)
# largest_number_index = values_list.index(max(values_list))
# repeted_character = list(dictionary.keys())[largest_number_index]
# print(f"The most repeted character is: {repeted_character}, repeating{dictionary}[repeted_character],times")

# #Alternative 2
# largest_number2 = max(dictionary,key=dictionary.get)
# print(f"The most repeted character is: {largest_number2}, repeating{dictionary}[largest_number2],times")
# message = input ("Write a message")

# character_count(message, dictionary)
