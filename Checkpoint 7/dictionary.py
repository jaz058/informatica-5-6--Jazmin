capitals = {
    "Mexico": "Mexico City",
    "Canada": "Ottawa",
    "Brazil": "Brasilia"
}

capitals["Italy"] = "Rome" #Add a new key and value
del capitals["Brazil"] #Deletes key and value
capitals.pop("Canada")
capitals.clear()

print(capitals)


# students={
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# for key in students:
#     print(f"{key}:{students[key]}")
# 
students = [
    {"name":"Hermione","house":"Gryffindor","patrounus":"Otter"},
    {"name":"Harry","house":"Gryffindor", "patrounus": "Stag"},
    {"name":"Ron","house":"Gryffindor", "patrounus": "Jack Russell Terrier"},
    {"name":"Draco","house":"Slytherin", "patrounus": "..."}
]
for element in students:
    print(f"{element["name"]},{element["house"]},{element["patrounus"]}")