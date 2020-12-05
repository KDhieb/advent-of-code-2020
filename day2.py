
f = open("data/day2.txt", "r")
save = f.read()
array = save.split("\n")
passwordArray = []

def passwordParse():
    for entry in array:
        store = entry.split()
        pDict = {}
        pDict["code"] = store[0]
        pDict["letter"] = store[1][0]
        pDict["password"] = store[2]
        passwordArray.append(pDict)
    

#valid = 0

# REQUIREMENTS: selectPart either 1 or 2
# EFFECTS: answers part 1 by default, or part 2 if 2 is inputted
def validPasswordCount(selectPart=1):
    valid = 0
    passwordParse()
    for entry in passwordArray:
        minmax = entry["code"].split("-")
        minval = int(minmax[0])
        maxval = int(minmax[1])
        letter = entry["letter"]
        password = entry["password"]
        if selectPart == 1:
            valid += count(minval, maxval, letter, password)
        if selectPart == 2:
            valid += countNew(minval, maxval, letter, password)
    print(f"Part {selectPart}: Number of valid passwords is " + str(valid))


def countNew(pos1, pos2, letter, password):
    if password[pos1-1] == letter and password[pos2-1] != letter:
        return 1
    elif password[pos1-1] != letter and password[pos2-1] == letter:
        return 1
    else:
        return 0


def count(minimum, maximum, letter, password):
    counter = 0
    for char in password:
        if char == letter:
            counter += 1
    if counter >= minimum and counter <= maximum:
        return 1
    else:
        return 0

if __name__ == '__main__':
    passwordParse()
    validPasswordCount(1) # Part 1 answer
    validPasswordCount(2) # Part 2 answer


    


    
        

