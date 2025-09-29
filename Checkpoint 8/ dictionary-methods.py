dictionary = {
    "color": "black",
    "age" : 17
}

#values
print(dictionary.values())
for v in dictionary.values():
    print(v)

#Keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)

#Item
print(dictionary.items())
for i in dictionary.items():
    print(i)

#Print key and value using methods
#to do

picnic_items = {"apples":5, "cups":2}
print(f"I'm bringing{picnic_items.get("cups")} cups.")

print(f"I'm bringing{picnic_items.get("eggs",0)} eggs.")

#Setting Default Values
pet_info = {
    "name": "Puka"
    "age" : "5"
}
pet_info.setdefault("color","black")
pet_info["color"] = "black"
pet_info.setdefault
print(pet_info)