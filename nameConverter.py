nameList = []
tgtfile = open("names.txt", "r")
data = tgtfile.readlines()
name = ""
for text in data:
    for letter in text:
        name += letter
        if letter == "-":
            name = name[:-2]
            break
    nameList.append(name)
    name = ""
tgtfile.close()

for name in nameList:
    if "\t" in name:
        nameList[nameList.index(name)] = name[:-2]

for name in nameList:
    nameList[nameList.index(name)] = name.title()

print nameList
