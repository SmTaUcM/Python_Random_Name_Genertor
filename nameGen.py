#   Version 3.1
#   02 Dec 2016
#   Stuart Macintosh


# ---------- Imports ----------
import random


# ---------- Global ----------
# Load the .dat files into the program.
with open("Male.dat") as f:
    maleFirstNames = f.readlines()

with open("Female.dat") as f:
    femaleFirstNames = f.readlines()

with open("Surnames.dat") as f:
    surnames = f.readlines()


# ---------- Definitions ----------
def stats():
    print """
Male First Names            = %s
Female First Names          = %s
Surnames                    = %s
Total possible combinations = %s""" %(len(maleFirstNames), len(femaleFirstNames), len(surnames), (group(str((len(maleFirstNames) + len(femaleFirstNames)) * len(surnames)))))

def randomMaleName():
    firstNameRange = len(maleFirstNames) - 1 # -1 due to len and index giving offset values.
    firstName = maleFirstNames[random.randint(0, firstNameRange)]
    name = firstName[:-1] + " " + randomSurname()
    return name



def randomFemaleName():
    firstNameRange = len(femaleFirstNames) - 1
    firstName = femaleFirstNames[random.randint(0, firstNameRange)]
    name = firstName[:-1] + " " + randomSurname()
    return name



def randomSurname():
    surnameRange = len(surnames) - 1
    surname = surnames[random.randint(0, surnameRange)]
    return surname[:-1]



def randomName():
    sex = random.randint(1,2)
    if sex == 1:
        name = randomMaleName()
        sex = "Male"
        return name, sex
    elif sex == 2:
        name= randomFemaleName()
        sex = "Female"
        return name, sex
    else:
        print "Error!"



def group(number):
    """Used to insert commas into large numbers e.g. 1,000,000."""
    output = ""
    finalNumber = ""
    count  = 0
    for num in number[::-1]:
        count += 1
        output += num
        if count == 3:
            output += ","
            count = 0
    if output[-1:] == ",":
        output = output[:-1]
    for i in output[::-1]:
        finalNumber += i
    return finalNumber



# ---------- Main ----------
if __name__ == '__main__':
    print "This script file is intended used as an imported module only.\n\n"
    print "This module can produce the following amount of random names for any application."
    stats()
    raw_input("\nPress 'Enter' to Exit.")
