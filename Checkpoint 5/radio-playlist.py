weekly_playlist = ["Blinding Lights","Levitating","As It Was","Heat Waves","Good 4 u"]
weekly_playlist.append("Drivers License")
weekly_playlist.insert(0,"Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")

print(weekly_playlist.index("Levitating"))
print(weekly_playlist.count("As it was"))

print("Throwback Thursday")
weekly_playlist.reverse()
print(weekly_playlist)

weekly_playlist.sort()
print(weekly_playlist)