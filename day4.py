import re

class PassportScanner:
    passportArray = []
    checkList = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def parseFile(self, filename):
        readFile = open(filename, 'r').read()
        stringArray = readFile.split("\n\n")
        for p in stringArray:
            dObj = {}
            passport = re.split(r"\n|\s+", p)
            for field in passport:
                fieldArray = field.split(":")
                dObj[fieldArray[0]] = fieldArray[1]
            self.passportArray.append(dObj)

    def countValidPassports(self):
        count = 0
        for passport in self.passportArray:
            currentPassportFields = passport.keys()
            valid = True
            for field in self.checkList:
                if field not in currentPassportFields:
                    valid = False
            if valid == True:
                count += 1
        print(f"Number of Valid Passports: {count}")

    def countValidPassportsAndFields(self):
        count = 0
        for passport in self.passportArray:
            currentPassportFields = passport.keys()
            valid = True
            for field in self.checkList:
                if field in currentPassportFields:
                    isValueValid = self.checkFields(field, passport[field])
                    if isValueValid == False:
                        valid = False
                else:
                    valid = False
            if valid == True:
                count += 1
        print(f"Number of Valid Passports: {count}")

    def checkFields(self, field, value):
        if field == 'byr':
            return self.checkBirthYear(value)
        elif field == 'iyr':
            return self.checkIssueYear(value)
        elif field == 'eyr':
            return self.checkExpirationYear(value)
        elif field == 'hgt':
            return self.checkHeight(value)
        elif field == 'hcl':
            return self.checkHairColour(value)
        elif field == 'ecl':
            return self.checkEyeColour(value)
        elif field == 'pid':
            return self.checkPassportID(value)

    def checkBirthYear(self, value):
        byr = int(value)
        return len(value) == 4 and 1920 <= byr <= 2002

    def checkIssueYear(self, value):
        iyr = int(value)
        return len(value) == 4 and 2010 <= iyr <= 2020

    def checkExpirationYear(self, value):
        eyr = int(value)
        return len(value) == 4 and 2020 <= eyr <= 2030

    def checkHeight(self, value):
        reString = "1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in"
        reObj = re.fullmatch(reString, value)
        return bool(reObj)

    def checkHairColour(self, value):
        reString = "#([0-9]|[a-f]){6}"
        reObj = re.fullmatch(reString, value)
        return bool(reObj)

    def checkEyeColour(self, value):
        acceptable = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return value in acceptable

    def checkPassportID(self, value):
        reString = "[0-9]{9}"
        reObj = re.fullmatch(reString, value)
        return bool(reObj)


if __name__ == "__main__":
    ps = PassportScanner()
    ps.parseFile("data/day4.txt")
    print("Part 1:")
    ps.countValidPassports()
    print("\nPart 2:")
    ps.countValidPassportsAndFields()
