from itertools import permutations
from time import time
# import pandas as pd

class Person():
    def __init__(self, beverage: str=None, cigar: str=None, pet: str=None, nationality: str=None):
        self.beverage=beverage
        self.cigar=cigar
        self.pet=pet
        self.nationality=nationality

    def getNation(self) -> str:
        return self.nationality

    def setBeverage(self, beverage: str):
        self.beverage=beverage

    def getBeverage(self) -> str:
        return self.beverage

    def setCigar(self, cigar: str):
        self.cigar=cigar

    def getCigar(self) -> str:
        return self.cigar

    def setPet(self, pet: str):
        self.pet=pet

    def getPet(self) -> str:
        return self.pet

class House():
    def __init__(self, person: Person):
        self.setPerson(person)
        self.color=None
        self.houseNumber=None
        self.lHouse=None
        self.rHouse=None

    def setPerson(self, person: Person): # set the person who live in this house
        self.person=person

    def getPerson(self) -> Person: # get the person who live in this house
        return self.person

    def setRightHouse(self, house=None): # set the person who live in right
        self.rHouse=house

    def getRightHouse(self): # get right house
        return self.rHouse

    def setLeftHouse(self, house=None): # set left house
        self.lHouse=house

    def getLeftHouse(self): # get left house
        return self.lHouse

    def setColor(self, color: str): # set color
        self.color=color

    def getColor(self) -> str: # get color
        return self.color

    def setNumber(self, number: int):
        self.houseNumber=number

    def getNumber(self) -> int:
        return self.houseNumber

class EinsteinsRiddle():
    def __init__(self, houseDict: dict, properties: dict):
        self.houseDict=houseDict
        self.setHouseDict(properties)

    def getHouse(self,person: str=None, color: str=None,
                 cigar: str=None, beverage: str=None,
                 pet: str=None, houseNumber: int=0) -> House:

        for house in self.houseDict.values():
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
                if beverage!=None:
                    if house.getPerson().getBeverage()==beverage:
                        return house
                if pet!=None:
                    if house.getPerson().getPet()==pet:
                        return house
                if houseNumber!=None:
                    if house.getNumber()==houseNumber:
                        return house

    def setHouseDict(self, properties: dict):
        self.houseDict["Norwegian"].setColor(properties["color"][0])
        self.houseDict["Norwegian"].setNumber(properties["number"][0])
        self.houseDict["Norwegian"].getPerson().setPet(properties["pet"][0])
        self.houseDict["Norwegian"].getPerson().setBeverage(properties["beverage"][0])
        self.houseDict["Norwegian"].getPerson().setCigar(properties["cigar"][0])

        self.houseDict["Dane"].setColor(properties["color"][1])
        self.houseDict["Dane"].setNumber(properties["number"][1])
        self.houseDict["Dane"].getPerson().setPet(properties["pet"][1])
        self.houseDict["Dane"].getPerson().setBeverage(properties["beverage"][1])
        self.houseDict["Dane"].getPerson().setCigar(properties["cigar"][1])

        self.houseDict["Brit"].setColor(properties["color"][2])
        self.houseDict["Brit"].setNumber(properties["number"][2])
        self.houseDict["Brit"].getPerson().setPet(properties["pet"][2])
        self.houseDict["Brit"].getPerson().setBeverage(properties["beverage"][2])
        self.houseDict["Brit"].getPerson().setCigar(properties["cigar"][2])

        self.houseDict["German"].setColor(properties["color"][3])
        self.houseDict["German"].setNumber(properties["number"][3])
        self.houseDict["German"].getPerson().setPet(properties["pet"][3])
        self.houseDict["German"].getPerson().setBeverage(properties["beverage"][3])
        self.houseDict["German"].getPerson().setCigar(properties["cigar"][3])

        self.houseDict["Swede"].setColor(properties["color"][4])
        self.houseDict["Swede"].setNumber(properties["number"][4])
        self.houseDict["Swede"].getPerson().setPet(properties["pet"][4])
        self.houseDict["Swede"].getPerson().setBeverage(properties["beverage"][4])
        self.houseDict["Swede"].getPerson().setCigar(properties["cigar"][4])

        # set neighborhood
        self.numberDict = {}
        self.numberDict[self.houseDict["Brit"].getNumber()] = self.houseDict["Brit"]
        self.numberDict[self.houseDict["Dane"].getNumber()] = self.houseDict["Dane"]
        self.numberDict[self.houseDict["Norwegian"].getNumber()] = self.houseDict["Norwegian"]
        self.numberDict[self.houseDict["German"].getNumber()] = self.houseDict["German"]
        self.numberDict[self.houseDict["Swede"].getNumber()] = self.houseDict["Swede"]

        self.numberDict[1].setLeftHouse(None)
        self.numberDict[1].setRightHouse(self.numberDict[2])
        self.numberDict[2].setLeftHouse(self.numberDict[1])
        self.numberDict[2].setRightHouse(self.numberDict[3])
        self.numberDict[3].setLeftHouse(self.numberDict[2])
        self.numberDict[3].setRightHouse(self.numberDict[4])
        self.numberDict[4].setLeftHouse(self.numberDict[3])
        self.numberDict[4].setRightHouse(self.numberDict[5])
        self.numberDict[5].setLeftHouse(self.numberDict[4])
        self.numberDict[5].setRightHouse(None)

    def promising(self):
        # # The Norwegian lives in the first(leftmost) house
        # if (self.getHouse(person="Norwegian")) != None:
        #     if self.getHouse(person="Norwegian").getNumber() != 1:
        #         # print("9 error", end=' ')
        #         return 9
        #     # The German smokes Prince
        # if (self.getHouse(person="German")) != None:
        #     if self.getHouse(person="German").getPerson().getCigar() != "Prince":
        #         # print("13 error", end=' ')
        #         return 13
        # # The Brit lives in a red house
        # if (self.getHouse(person="Brit")) != None:
        #     if self.getHouse(person="Brit").getColor() != "red":
        #         # print("1 error", end=' ')
        #         return 1
        # # The green House is on the left of the white house
        # if (self.getHouse(color="white")) != None:
        #     if self.getHouse(color="green") != self.getHouse(color="white").getLeftHouse():
        #         # print("4 error", end=' ')
        #         return 4
        # # The owner of the yellow house smokes Dunhill
        # if (self.getHouse(color="yellow")) != None:
        #     if self.getHouse(color="yellow").getPerson().getCigar() != "Dunhill":
        #         # print("7 error", end=' ')
        #         return 7
        # # The Norwegian lives next to the blue house
        # if self.getHouse(color="blue") != None:
        #     if self.getHouse(color="blue").getNumber() != 2:
        #         # print("14 error",end=' ')
        #         return 14
        # # The Swede keeps dogs as pets
        # if (self.getHouse(person="Swede")) != None:
        #     if self.getHouse(person="Swede").getPerson().pet != "dog":
        #         # print("2 error", end=' ')
        #         return 2
        # # The person who smokes Pall Mall rears birds
        # if (self.getHouse(cigar="Pall Mall")) != None:
        #     if self.getHouse(cigar="Pall Mall").getPerson().getPet() != "bird":
        #         # print("6 error", end=' ')
        #         return 6
        # # The man who smokes Blend lives next to the one who keeps cats
        # if (self.getHouse(cigar="Blend")) != None:
        #     if (self.getHouse(cigar="Blend").getNumber() - self.getHouse(pet="cat").getNumber()) not in (1,-1):
        #         # print("10 error", end=' ')
        #         return 10
        # # The man who keeps horses lives next to the man who smokes Dunhill
        # if (self.getHouse(pet="horse")) != None:
        #     if (self.getHouse(pet="horse").getNumber() - self.getHouse(cigar="Dunhill").getNumber()) not in (1,-1):
        #         # print("11 error", end=' ')
        #         return 11
        # # The Dane drinks tea
        # if (self.getHouse(person="Dane")) != None:
        #     if self.getHouse(person="Dane").getPerson().getBeverage() != "tea":
        #         # print("3 error", end=' ')
        #         return 3
        #
        # # The green house owner drinks coffee
        # if (self.getHouse(color="green")) != None:
        #     if self.getHouse(color="green").getPerson().getBeverage() != "coffee":
        #         # print("5 error", end=' ')
        #         return 5
        #
        # # The man living in the house right in the center drinks milk
        # if (self.getHouse(houseNumber=3)) != None:
        #     if self.getHouse(houseNumber=3).getPerson().getBeverage() != "milk":
        #         # print("8 error", end=' ')
        #         return 8
        #
        # # The owner who smokes Blue Master drinks beer
        # if (self.getHouse(cigar="Blue Master")) != None:
        #     if self.getHouse(cigar="Blue Master").getPerson().getBeverage() != "beer":
        #         # print("12 error", end=' ')
        #         return 12
        # # The man who smokes Blend has a neighbor who drinks water
        # if (self.getHouse(cigar="Blend")) != None:
        #     if (self.getHouse(cigar="Blend").getNumber() - self.getHouse(beverage="water").getNumber()) not in (1,-1):
        #         # print("15 error", end=' ')
        #         return 15

        # The Norwegian lives in the first(leftmost) house
        if (self.getHouse(person="Norwegian")) != None:
            if self.getHouse(person="Norwegian").getNumber() != 1:
                # print("9 error", end=' ')
                return 9
        # The Brit lives in a red house
        if (self.getHouse(person="Brit")) != None:
            if self.getHouse(person="Brit").getColor() != "red":
                # print("1 error", end=' ')
                return 1
        # The Norwegian lives next to the blue house
        if self.getHouse(color="blue") != None:
            if self.getHouse(color="blue").getNumber() != 2:
                # print("14 error",end=' ')
                return 14
        # The green House is on the left of the white house
        if (self.getHouse(color="white")) != None:
            if self.getHouse(color="green") != self.getHouse(color="white").getLeftHouse():
                # print("4 error", end=' ')
                return 4
        # The Dane drinks tea
        if (self.getHouse(person="Dane")) != None:
            if self.getHouse(person="Dane").getPerson().getBeverage() != "tea":
                # print("3 error", end=' ')
                return 3
        # The green house owner drinks coffee
        if (self.getHouse(color="green")) != None:
            if self.getHouse(color="green").getPerson().getBeverage() != "coffee":
                # print("5 error", end=' ')
                return 5
        # The man living in the house right in the center drinks milk
        if (self.getHouse(houseNumber=3)) != None:
            if self.getHouse(houseNumber=3).getPerson().getBeverage() != "milk":
                # print("8 error", end=' ')
                return 8
        # The German smokes Prince
        if (self.getHouse(person="German")) != None:
            if self.getHouse(person="German").getPerson().getCigar() != "Prince":
                # print("13 error", end=' ')
                return 13
        # The owner who smokes Blue Master drinks beer
        if (self.getHouse(cigar="Blue Master")) != None:
            if self.getHouse(cigar="Blue Master").getPerson().getBeverage() != "beer":
                # print("12 error", end=' ')
                return 12
        # The owner of the yellow house smokes Dunhill
        if (self.getHouse(color="yellow")) != None:
            if self.getHouse(color="yellow").getPerson().getCigar() != "Dunhill":
                # print("7 error", end=' ')
                return 7
        # The man who smokes Blend has a neighbor who drinks water
        if (self.getHouse(cigar="Blend")) != None:
            if (self.getHouse(cigar="Blend").getNumber() - self.getHouse(beverage="water").getNumber()) not in (1,-1):
                # print("15 error", end=' ')
                return 15
        # The Swede keeps dogs as pets
        if (self.getHouse(person="Swede")) != None:
            if self.getHouse(person="Swede").getPerson().getPet() != "dog":
                # print("2 error", end=' ')
                return 2
        # The person who smokes Pall Mall rears birds
        if (self.getHouse(cigar="Pall Mall")) != None:
            if self.getHouse(cigar="Pall Mall").getPerson().getPet() != "bird":
                # print("6 error", end=' ')
                return 6
        # The man who keeps horses lives next to the man who smokes Dunhill
        if (self.getHouse(pet="horse")) != None:
            if (self.getHouse(pet="horse").getNumber() - self.getHouse(cigar="Dunhill").getNumber()) not in (1,-1):
                # print("11 error", end=' ')
                return 11
        # The man who smokes Blend lives next to the one who keeps cats
        if (self.getHouse(cigar="Blend")) != None:
            if (self.getHouse(cigar="Blend").getNumber() - self.getHouse(pet="cat").getNumber()) not in (1,-1):
                # print("10 error", end=' ')
                return 10
        return 16


if __name__=="__main__":
    start=time()
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

    houseDict = {}
    houseDict["Brit"] = britHouse
    houseDict["Dane"] = daneHouse
    houseDict["German"] = germanHouse
    houseDict["Norwegian"] = norwegianHouse
    houseDict["Swede"] = swedeHouse

    # #중복되면 하위 loop 부터
    # neighborhoodErrorCode=[9]
    # cigarErrorCode = [13]
    # colorErrorCode=[1, 4, 7, 14]
    # petErrorCode=[2, 6, 10, 11]
    # beverageErrorCode = [3, 5, 8, 12, 15]
    # 조건이 중복되면 하위 loop 부터
    neighborhoodErrorCode = [9]
    colorErrorCode = [1, 4, 14]
    beverageErrorCode = [3, 5, 8]
    cigarErrorCode = [7, 12, 13, 15]
    petErrorCode = [2, 6, 10, 11]

    numberOfNodes=0     # 총 탐색 노드 수
    checkNumber=0       # solution에 합당한지
    solutionNumber=16   # solution number


    # for number in permutations(range(1,6),5):
    #     for cigar in permutations(cigars, 5):
    #         for color in permutations(colors,5):
    #             for pet in permutations(pets, 5):
    #                 for beverage in permutations(beverages, 5):
    #                     numberOfNodes+=1
    #
    #                     properties={}
    #                     properties["number"] = number
    #                     properties["cigar"] = cigar
    #                     properties["color"] = color
    #                     properties["pet"] = pet
    #                     properties["beverage"] = beverage
    #
    #                     einstein = EinsteinsRiddle(houseDict=houseDict, properties=properties)
    #                     checkNumber=einstein.promising()
    #                     # print()
    #                     # print(checkNumber)
    #                     #
    #                     # print()
    #                     # for key in range(1, 6):
    #                     #     print(einstein.numberDict[key].getNumber(),
    #                     #           einstein.numberDict[key].getPerson().getNation(),
    #                     #           einstein.numberDict[key].getColor(),
    #                     #           einstein.numberDict[key].getPerson().getPet(),
    #                     #           einstein.numberDict[key].getPerson().getBeverage(),
    #                     #           einstein.numberDict[key].getPerson().getCigar())
    #                     if checkNumber != solutionNumber:
    #                         if checkNumber in beverageErrorCode:
    #                             continue
    #                         else:
    #                             break
    #                     else:
    #                         break
    #                 if checkNumber != solutionNumber:
    #                     if checkNumber in petErrorCode or \
    #                             checkNumber in beverageErrorCode:
    #
    #                         continue
    #                     else:
    #                         break
    #                 else:
    #
    #                     break
    #             if checkNumber != solutionNumber:
    #                 if checkNumber in colorErrorCode or \
    #                         checkNumber in petErrorCode or \
    #                         checkNumber in beverageErrorCode:
    #                     continue
    #                 else:
    #                     break
    #             else:
    #                 break
    #         if checkNumber != solutionNumber:
    #             if checkNumber in cigarErrorCode or \
    #                     checkNumber in colorErrorCode or \
    #                     checkNumber in petErrorCode or \
    #                     checkNumber in beverageErrorCode:
    #                 continue
    #             else:
    #                 break
    #         else:
    #             break
    #     if checkNumber != solutionNumber:
    #         if checkNumber in neighborhoodErrorCode or \
    #                 checkNumber in cigarErrorCode or \
    #                 checkNumber in colorErrorCode or \
    #                 checkNumber in petErrorCode or \
    #                 checkNumber in beverageErrorCode:
    #             continue
    #     else:
    #         break
    # numberOfNodes = 0
    # checkNumber = 0
    for number in permutations(range(1, 6), 5):
        for color in permutations(colors, 5):
            for beverage in permutations(beverages, 5):
                for cigar in permutations(cigars, 5):
                    for pet in permutations(pets, 5):
                        numberOfNodes += 1

                        properties = {}
                        properties["number"] = number
                        properties["cigar"] = cigar
                        properties["color"] = color
                        properties["pet"] = pet
                        properties["beverage"] = beverage

                        einstein = EinsteinsRiddle(houseDict=houseDict, properties=properties)
                        checkNumber = einstein.promising()
                        print()
                        print("Hint number",checkNumber,"error")
                        #
                        #print()
                        for key in range(1, 6):
                            print(einstein.numberDict[key].getNumber(),
                                  einstein.numberDict[key].getPerson().getNation(),
                                  einstein.numberDict[key].getColor(),
                                  einstein.numberDict[key].getPerson().getPet(),
                                  einstein.numberDict[key].getPerson().getBeverage(),
                                  einstein.numberDict[key].getPerson().getCigar())
                        if checkNumber != solutionNumber:
                            if checkNumber in petErrorCode:
                                continue
                            else:
                                break
                        else:
                            break
                    if checkNumber != solutionNumber:
                        if checkNumber in cigarErrorCode or \
                                checkNumber in petErrorCode:
                            continue
                        else:
                            break
                    else:
                        break
                if checkNumber != solutionNumber:
                    if checkNumber in beverageErrorCode or \
                            checkNumber in cigarErrorCode or \
                            checkNumber in petErrorCode:
                        continue
                    else:
                        break
                else:
                    break
            if checkNumber != solutionNumber:
                if checkNumber in colorErrorCode or \
                        checkNumber in beverageErrorCode or \
                        checkNumber in cigarErrorCode or \
                        checkNumber in petErrorCode:
                    continue
                else:
                    break
            else:
                break
        if checkNumber != solutionNumber:
            if checkNumber in neighborhoodErrorCode or \
                    checkNumber in colorErrorCode or \
                    checkNumber in beverageErrorCode or \
                    checkNumber in cigarErrorCode or \
                    checkNumber in petErrorCode:
                continue
        else:
            break
    print()
    print("The Final Solution is")
    for key in range(1, 6):
        print(einstein.numberDict[key].getNumber(),
              einstein.numberDict[key].getPerson().getNation(),
              einstein.numberDict[key].getColor(),
              einstein.numberDict[key].getPerson().getPet(),
              einstein.numberDict[key].getPerson().getBeverage(),
              einstein.numberDict[key].getPerson().getCigar())

    # df=pd.DataFrame({key: [einstein.numberDict[key].getPerson().getNation(),
    #                        einstein.numberDict[key].getColor(),
    #                        einstein.numberDict[key].getPerson().getPet(),
    #                        einstein.numberDict[key].getPerson().getBeverage(),
    #                        einstein.numberDict[key].getPerson().getCigar()] for key in range(1,6)},
    #                 index=["Nationality", "Color", "Pet", "Beverage", "Cigar"])

    # print(df)
    print()
    print("Number of nodes: ", numberOfNodes)
    end=time()
    print("Time elapsed: ", end-start)









