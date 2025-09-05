indipendence_stages = ["Inicio","Organizacion", "Resistencia", "Concumacion",]
print(indipendence_stages[:4])
print(len(indipendence_stages))

#List methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(indipendence_stages)//Mis lists together
leaders.insert(1,"Jose Maria Morelos")
#leaders.remove("Vicente Guerrero")//Delete first matchof specific items
leaders.append("Agustin de Iturbide")
#leaders.pop(1)
#leaders.clear//Para limpiar todo lo de la lista
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
#print(leaders.sort())
#leaders.reverse()
new_leaders = leaders.copy()

print(leaders)
print(new_leaders)