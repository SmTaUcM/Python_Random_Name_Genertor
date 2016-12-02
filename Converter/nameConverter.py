def nameConverter(nameFile):

    nameList = []

    # Open the source text file and load the data.
    tgtfile = open("Source Files\\%s" %nameFile, "r")
    data = tgtfile.readlines()
    tgtfile.close()

    # Gather each name, trim it after the " " and add it to the name list.
    name = ""
    for text in data:
        for letter in text:
            name += letter
            if letter == " ":
                name = name[:-1]
                break

        # Trim any \t tab spacings to the names on the list.
        if "\t" in name:
            name = name[ 0 : name.find("\t")]

        name = name.title()
        name += "\n"
        nameList.append(name)
        name = ""

    tgtfile = open("%s.dat" %nameFile[ 0 : nameFile.find(".")], "w")
    tgtfile.writelines(nameList)
    tgtfile.close()


# ------------------------------- MAIN PROGRAM. -------------------------------------

files = ["Surnames.txt", "Male.txt", "Female.txt"]

for fileName in files:
    nameConverter(fileName)
raw_input("Operation Complete.")
