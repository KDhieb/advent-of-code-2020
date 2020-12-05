
class Toboggan:
    RIGHT = 3
    DOWN = 1
    treeCount = 0
    inRange = True
    mapArray = []

    def parseMap(self, file):
        f = open(str(file), 'r')
        text = f.read()
        self.mapArray = text.split("\n")
        lineIndex = 0
        for line in self.mapArray:
            self.mapArray[lineIndex] = line * 100
            lineIndex += 1

    def tobogganRightDown(self, right, down):
        widthIndex = 0
        heightIndex = 0
        self.treeCount = 0
        self.inRange = True

        while self.inRange:
            widthIndex += right
            heightIndex += down
            self.treeCount += self.checkIfTree(heightIndex, widthIndex)
        print(f"The number of trees encountered for slope Right {right}, Down {down} is {toboggan.treeCount}")
        return self.treeCount

    def checkIfTree(self, v, h):
        try:
            if self.mapArray[v][h] == "#":
                return 1
            else:
                return 0
        except:
            self.inRange = False
            return 0

if __name__ == '__main__':
    toboggan = Toboggan()
    toboggan.parseMap("data/day3.txt")

    print("Part 1:")
    s1 = toboggan.tobogganRightDown(3, 1)

    print("\nPart 2:")
    s2 = toboggan.tobogganRightDown(1, 1)
    s3 = toboggan.tobogganRightDown(5, 1)
    s4 = toboggan.tobogganRightDown(7, 1)
    s5 = toboggan.tobogganRightDown(1, 2)
    print(s1 * s2 * s3 * s4 * s5)