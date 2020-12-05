f = open("data/day1.txt", "r")
text = f.read()
array = text.split()


def twoNum2020():
    for number in array:
        for  nextNum in array:
            if (int(number) + int(nextNum)  == 2020):
                return (str(number) +" and " + str(nextNum))
    return "none were found"

def threeNum2020():
    for number in array:
        for  nextNum in array:
            for  nextNextNum in array:
                if (int(number) + int(nextNum) + int(nextNextNum) == 2020):
                    return (str(number) +" and " + str(nextNum) + " and " + str(nextNextNum))
    return "none were found"

if __name__ == '__main__':
    print("Part 1: " + twoNum2020())
    print("Part 2: " + threeNum2020())

