e = dict(
    nom= str,
    prenom = str,
    age = int,
    genre = str(),
    classe = str,
)

e["nom"] = "Ben Mohamed"
e["prenom"] = "Mohamed"
e["age"] = 17
e["genre"] = "G"
e["classe"] = "3 info 1"

print(e["nom"])
print(e["prenom"] )
print(e["age"] )
print(e["genre"] )
print(e["classe"] )