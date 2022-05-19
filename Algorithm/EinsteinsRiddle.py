from itertools import permutations

class Person():
    def __init__(self, beverage=None, cigar=None, pet=None, nationality=None):
        self.beverage=beverage
        self.cigar=cigar
        self.pet=pet
        self.nationality=nationality

    def getNation(self):
        return self.nationality

    def setBeverage(self,beverage):
        self.beverage=beverage

    def getBeverage(self):
        return self.beverage

    def setCigar(self,cigar):
        self.cigar=cigar

    def getCigar(self):
        return self.cigar

    def setPet(self,pet):
        self.pet=pet

    def getPet(self):
        return self.pet

class House():
    def __init__(self,person: Person):
        self.setPerson(person)
        self.color=None
        self.houseNumber=None
        self.lHouse=None
        self.rHouse=None

    def setPerson(self,person): # set the person who live in this house
        self.person=person

    def getPerson(self): # get the person who live in this house
        return self.person

    def setRightHouse(self,house=None): # set the person who live in right
        self.rHouse=house

    def getRightHouse(self): # get right house
        return self.rHouse

    def setLeftHouse(self,house=None): # set left house
        self.lHouse=house

    def getLeftHouse(self): # get left house
        return self.lHouse

    def setColor(self,color: str): # set color
        self.color=color

    def getColor(self) -> str: # get color
        return self.color

    def setNumber(self, number):
        self.houseNumber=number

    def getNumber(self) -> int:
        return self.houseNumber

class EinsteinsRiddle():
    houseList=[]
    def __init__(self,houseList):
        self.houseList=houseList

    def getHouse(self,person=None, color=None, cigar=None, pet=None, houseNumber=None):
        for house in self.houseList:
            if house !=None:
                if person!=None:
                    if house.getPerson().getNation()==person:
                        return house
                if color!=None:
                    if house.getColor()==color:
                        return house
                if cigar!=None:
                    if house.getPerson().getCigar()==cigar:
                        return house
                if pet!=None:
                    if house.getPerson().getPet()==pet:
                        return house
                if houseNumber!=None:
                    if house.getNumber()==houseNumber:
                        return house

    def promising(self) -> int:
        # The Brit lives in a red house
        if (self.getHouse(person="Brit")) != None:
            if self.getHouse(person="Brit").getColor() != "red":
                print("1 error", end=' ')
                return 1
        # The Swede keeps dogs as pets
        if (self.getHouse(person="Swede")) != None:
            if self.getHouse(person="Swede").getPerson().pet != "dog":
                print("2 error", end=' ')
                return 2
        # The Dane drinks tea
        if (self.getHouse(person="Dane")) != None:
            if self.getHouse(person="Dane").getPerson().getBeverage() != "tea":
                print("3 error", end=' ')
                return 3
        # The green House is on the left of the white house
        if (self.getHouse(color="white")) != None:
            if self.getHouse(color="green") != self.getHouse(color="white").getLeftHouse():
                print("4 error", end=' ')
                return 4
        # The green house owner drinks coffee
        if (self.getHouse(color="green")) != None:
            if self.getHouse(color="green").getPerson().getBeverage() != "coffee":
                print("5 error", end=' ')
                return 5
        # The person who smokes Pall Mall rears birds
        if (self.getHouse(cigar="Pall Mall")) != None:
            if self.getHouse(cigar="Pall Mall").getPerson().getPet() != "bird":
                print("6 error", end=' ')
                return 6
        # The owner of the yellow house smokes Dunhill
        if (self.getHouse(color="yellow")) != None:
            if self.getHouse(color="yellow").getPerson().getCigar() != "Dunhill":
                print("7 error", end=' ')
                return 7
        # The man living in the house right in the center drinks milk
        if (self.getHouse(houseNumber=3)) != None:
            if self.getHouse(houseNumber=3).getPerson().getBeverage() != "milk":
                print("8 error", end=' ')
                return 8
        # The Norwegian lives in the first(leftmost) house
        if (self.getHouse(person="Norwegian")) != None:
            if self.getHouse(person="Norwegian").getNumber() != 1:
                print("9 error", end=' ')
                return 9
        # The man who smokes Blend lives next to the one who keeps cats
        if (self.getHouse(cigar="Blend")) != None:
            # left 이웃이 있을 경우
            if (self.getHouse(cigar="Blend").getLeftHouse() != None):
                # right 이웃이 있을 경우
                if self.getHouse(cigar="Blend").getRightHouse() != None:
                    if self.getHouse(cigar="Blend").getLeftHouse().getPerson().getPet() != "cat" and \
                            self.getHouse(cigar="Blend").getRightHouse().getPerson().getPet() != "cat":
                        print("10 error", end=' ')
                        return 10
                # right 이웃이 없을 경우
                if self.getHouse(cigar="Blend").getRightHouse() == None:
                    if self.getHouse(cigar="Blend").getLeftHouse().getPerson().getPet() != "cat":
                        print("10 error", end=' ')
                        return 10
            # left 이웃이 없을 경우
            if (self.getHouse(cigar="Blend").getLeftHouse() == None):
                if self.getHouse(cigar="Blend").getRightHouse() != None:
                    if self.getHouse(cigar="Blend").getRightHouse().getPerson().getPet() != "cat":
                        print("10 error", end=' ')
                        return 10
        # The man who keeps horses lives next to the man who smokes Dunhill
        if (self.getHouse(pet="horse")) != None:
            # left 이웃이 있을 경우
            if (self.getHouse(pet="horse").getLeftHouse() != None):
                # right 이웃이 있을 경우
                if self.getHouse(pet="horse").getRightHouse() != None:
                    if self.getHouse(pet="horse").getLeftHouse().getPerson().getCigar() != "Dunhill" and \
                            self.getHouse(pet="horse").getRightHouse().getPerson().getCigar() != "Dunhill":
                        print("11 error", end=' ')
                        return 11
                # right 이웃이 없을 경우
                elif self.getHouse(pet="horse").getRightHouse() == None:
                    if self.getHouse(pet="horse").getLeftHouse().getPerson().getCigar() != "Dunhill":
                        print("11 error", end=' ')
                        return 11
            # left 이웃이 없을 경우
            else:
                if self.getHouse(pet="horse").getRightHouse() != None:
                    if self.getHouse(pet="horse").getRightHouse().getPerson().getCigar() != "Dunhill":
                        print("11 error", end=' ')
                        return 11
        # The owner who smokes Blue Master drinks beer
        if (self.getHouse(cigar="Blue Master")) != None:
            if self.getHouse(cigar="Blue Master").getPerson().getBeverage() != "beer":
                print("12 error", end=' ')
                return 12
        # The German smokes Prince
        if (self.getHouse(person="German")) != None:
            if self.getHouse(person="German").getPerson().getCigar() != "Prince":
                print("13 error", end=' ')
                return 13
        # The Norwegian lives next to the blue house:
        if (self.getHouse(person="Norwegian")) != None:
            # left 이웃이 있을 경우
            if (self.getHouse(person="Norwegian").getLeftHouse() != None):
                # right 이웃이 있을 경우
                if self.getHouse(person="Norwegian").getRightHouse() != None:
                    if self.getHouse(person="Norwegian").getLeftHouse().getColor() != "blue" and \
                            self.getHouse(person="Norwegian").getRightHouse().getColor() != "blue":
                        print("14 error", end=' ')
                        return 14
                # right 이웃이 없을 경우
                if self.getHouse(person="Norwegian").getRightHouse() == None:
                    if self.getHouse(person="Norwegian").getLeftHouse().getColor() != "blue":
                        print("14 error", end=' ')
                        return 14
            # left 이웃이 없을 경우
            if (self.getHouse(person="Norwegian").getLeftHouse() == None):
                if self.getHouse(person="Norwegian").getRightHouse() != None:
                    if self.getHouse(person="Norwegian").getRightHouse().getColor() != "blue":
                        print("14 error", end=' ')
                        return 14
        # The man who smokes Blend has a neighbor who drinks water
        if (self.getHouse(cigar="Blend")) != None:
            # left 이웃이 있을 경우
            if (self.getHouse(cigar="Blend").getLeftHouse() != None):
                # right 이웃이 있을 경우
                if self.getHouse(cigar="Blend").getRightHouse() != None:
                    if self.getHouse(cigar="Blend").getLeftHouse().getPerson().getBeverage() != "water" and \
                            self.getHouse(cigar="Blend").getRightHouse().getPerson().getBeverage() != "water":
                        print("15 error", end=' ')
                        return 15
                # right 이웃이 없을 경우
                if self.getHouse(cigar="Blend").getRightHouse() == None:
                    if self.getHouse(cigar="Blend").getLeftHouse().getPerson().getBeverage() != "water":
                        print("15 error", end=' ')
                        return 15
            # left 이웃이 없을 경우
            if self.getHouse(cigar="Blend").getLeftHouse() == None:
                if self.getHouse(cigar="Blend").getRightHouse().getPerson().getBeverage() != "water":
                    print("15 error", end=' ')
                    return 15
        return 16


if __name__=="__main__":
    colors=["blue", "green", "red", "white", "yellow"]
    nationality=["Brit", "Dane", "German", "Norwegian", "Swede"]
    beverages=["beer", "coffee", "milk", "tea", "water"]
    cigars=["Blue Master", "Dunhill", "Pall Mall", "Prince", "Blend"]
    pets=["cat", "bird", "dog", "fish", "horse"]

    Brit=Person(nationality="Brit")
    Dane=Person(nationality="Dane")
    German=Person(nationality="German")
    Norwegian=Person(nationality="Norwegian")
    Swede=Person(nationality="Swede")

    britHouse=House(Brit)
    daneHouse=House(Dane)
    germanHouse=House(German)
    norwegianHouse=House(Norwegian)
    swedeHouse=House(Swede)

    # 중복되면 하위 loop 부터
    neighborhoodErrorCode=[9]
    colorErrorCode=[1,4,14]
    beverageErrorCode=[3,5,8,15]
    cigarErrorCode=[7,12,13]
    petErrorCode=[2,6,10,11]

    numberOfNodes=0

    for number in permutations([1,2,3,4,5],5):
        checkNumber=16
        for color in permutations(colors,5):
            for beverage in permutations(beverages,5):
                for cigar in permutations(cigars,5):
                    for pet in permutations(pets,5):
                        numberOfNodes+=1

                        norwegianHouse.setColor(color[0])
                        norwegianHouse.setNumber(number[0])
                        norwegianHouse.getPerson().setPet(pet[0])
                        norwegianHouse.getPerson().setBeverage(beverage[0])
                        norwegianHouse.getPerson().setCigar(cigar[0])

                        daneHouse.setColor(color[1])
                        daneHouse.setNumber(number[1])
                        daneHouse.getPerson().setPet(pet[1])
                        daneHouse.getPerson().setBeverage(beverage[1])
                        daneHouse.getPerson().setCigar(cigar[1])

                        britHouse.setColor(color[2])
                        britHouse.setNumber(number[2])
                        britHouse.getPerson().setPet(pet[2])
                        britHouse.getPerson().setBeverage(beverage[2])
                        britHouse.getPerson().setCigar(cigar[2])



                        germanHouse.setColor(color[3])
                        germanHouse.setNumber(number[3])
                        germanHouse.getPerson().setPet(pet[3])
                        germanHouse.getPerson().setBeverage(beverage[3])
                        germanHouse.getPerson().setCigar(cigar[3])


                        swedeHouse.setColor(color[4])
                        swedeHouse.setNumber(number[4])
                        swedeHouse.getPerson().setPet(pet[4])
                        swedeHouse.getPerson().setBeverage(beverage[4])
                        swedeHouse.getPerson().setCigar(cigar[4])

                        # set neighborhood
                        numberDict = {}
                        numberDict[britHouse.getNumber()]=britHouse
                        numberDict[daneHouse.getNumber()]=daneHouse
                        numberDict[norwegianHouse.getNumber()]=norwegianHouse
                        numberDict[germanHouse.getNumber()]=germanHouse
                        numberDict[swedeHouse.getNumber()]=swedeHouse\

                        numberDict[1].setLeftHouse(None)
                        numberDict[1].setRightHouse(numberDict[2])
                        numberDict[2].setLeftHouse(numberDict[1])
                        numberDict[2].setRightHouse(numberDict[3])
                        numberDict[3].setLeftHouse(numberDict[2])
                        numberDict[3].setRightHouse(numberDict[4])
                        numberDict[4].setLeftHouse(numberDict[3])
                        numberDict[4].setRightHouse(numberDict[5])
                        numberDict[5].setLeftHouse(numberDict[4])
                        numberDict[5].setRightHouse(None)

                        houseList = []
                        houseList.append(britHouse)
                        houseList.append(daneHouse)
                        houseList.append(germanHouse)
                        houseList.append(norwegianHouse)
                        houseList.append(swedeHouse)

                        # # 테스트용 답
                        # britHouse.setColor("red")
                        # britHouse.setNumber(3)
                        # britHouse.getPerson().setPet("bird")
                        # britHouse.getPerson().setBeverage("milk")
                        # britHouse.getPerson().setCigar("Pall Mall")
                        # britHouse.setLeftHouse(daneHouse)
                        # britHouse.setRightHouse(germanHouse)
                        #
                        # daneHouse.setColor("blue")
                        # daneHouse.setNumber(2)
                        # daneHouse.getPerson().setPet("horse")
                        # daneHouse.getPerson().setBeverage("tea")
                        # daneHouse.getPerson().setCigar("Blend")
                        # daneHouse.setLeftHouse(norwegianHouse)
                        # daneHouse.setRightHouse(britHouse)
                        #
                        # norwegianHouse.setColor("yellow")
                        # norwegianHouse.setNumber(1)
                        # norwegianHouse.getPerson().setPet("cat")
                        # norwegianHouse.getPerson().setBeverage("water")
                        # norwegianHouse.getPerson().setCigar("Dunhill")
                        # norwegianHouse.setLeftHouse()
                        # norwegianHouse.setRightHouse(daneHouse)
                        #
                        # germanHouse.setColor("green")
                        # germanHouse.setNumber(4)
                        # germanHouse.getPerson().setPet("fish")
                        # germanHouse.getPerson().setBeverage("coffee")
                        # germanHouse.getPerson().setCigar("Prince")
                        # germanHouse.setLeftHouse(britHouse)
                        # germanHouse.setRightHouse(swedeHouse)
                        #
                        # swedeHouse.setColor("white")
                        # swedeHouse.setNumber(5)
                        # swedeHouse.getPerson().setPet("dog")
                        # swedeHouse.getPerson().setBeverage("beer")
                        # swedeHouse.getPerson().setCigar("Blue Master")
                        # swedeHouse.setLeftHouse(germanHouse)
                        # swedeHouse.setRightHouse()
                        #
                        # houseList=[]
                        # houseList.append(britHouse)
                        # houseList.append(daneHouse)
                        # houseList.append(germanHouse)
                        # houseList.append(norwegianHouse)
                        # houseList.append(swedeHouse)

                        einstein = EinsteinsRiddle(houseList)
                        checkNumber=einstein.promising()
                        if checkNumber != 16:
                            if checkNumber in petErrorCode:
                                continue
                            else:
                                break
                        else:
                            print()
                            houseList.sort(key= lambda x : x.getNumber())
                            for house in houseList:
                                print(house.getNumber(), house.getPerson().getNation(), house.getColor(),
                                      house.getPerson().getPet(), house.getPerson().getBeverage(),
                                      house.getPerson().getCigar())
                            print("number of nodes: ", numberOfNodes)
                            break

                    if checkNumber!=16:
                        if checkNumber in cigarErrorCode:
                            continue
                    else:
                        break
                if checkNumber != 16:
                    if checkNumber in beverageErrorCode:
                        continue
                else:
                    break
            if checkNumber != 16:
                if checkNumber in colorErrorCode:
                    continue
            else:
                break
        if checkNumber != 16:
            if checkNumber in neighborhoodErrorCode:
                continue
        else:
            break

    # # 테스트용 답
    # britHouse.setColor("red")
    # britHouse.setNumber(3)
    # britHouse.getPerson().setPet("bird")
    # britHouse.getPerson().setBeverage("milk")
    # britHouse.getPerson().setCigar("Pall Mall")
    # britHouse.setLeftHouse(daneHouse)
    # britHouse.setRightHouse(germanHouse)
    #
    # daneHouse.setColor("blue")
    # daneHouse.setNumber(2)
    # daneHouse.getPerson().setPet("horse")
    # daneHouse.getPerson().setBeverage("tea")
    # daneHouse.getPerson().setCigar("Blend")
    # daneHouse.setLeftHouse(norwegianHouse)
    # daneHouse.setRightHouse(britHouse)
    #
    # norwegianHouse.setColor("yellow")
    # norwegianHouse.setNumber(1)
    # norwegianHouse.getPerson().setPet("cat")
    # norwegianHouse.getPerson().setBeverage("water")
    # norwegianHouse.getPerson().setCigar("Dunhill")
    # norwegianHouse.setLeftHouse()
    # norwegianHouse.setRightHouse(daneHouse)
    #
    # germanHouse.setColor("green")
    # germanHouse.setNumber(4)
    # germanHouse.getPerson().setPet("fish")
    # germanHouse.getPerson().setBeverage("coffee")
    # germanHouse.getPerson().setCigar("Prince")
    # germanHouse.setLeftHouse(britHouse)
    # germanHouse.setRightHouse(swedeHouse)
    #
    # swedeHouse.setColor("white")
    # swedeHouse.setNumber(5)
    # swedeHouse.getPerson().setPet("dog")
    # swedeHouse.getPerson().setBeverage("beer")
    # swedeHouse.getPerson().setCigar("Blue Master")
    # swedeHouse.setLeftHouse(germanHouse)
    # swedeHouse.setRightHouse()
    #
    # houseList=[]
    # houseList.append(britHouse)
    # houseList.append(daneHouse)
    # houseList.append(germanHouse)
    # houseList.append(norwegianHouse)
    # houseList.append(swedeHouse)






