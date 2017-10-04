class SpaceStation:
    def __init__(self):
        self.crew = []

    def addCrewMember(self, crew_member):
        # if self.getCrewSize() >= 3:
        #     return False
        # self.crew.append(crew_member)
        # return True

        if self.getCrewSize() < 3:
            self.crew.append(crew_member)
            return True
        return False

    def getCrewSize(self):
        #return len(self.crew)
        size = 0
        for member in self.crew:
            size += 1
        return size

if __name__ == '__main__':
    starkiller = SpaceStation()
    print(starkiller.addCrewMember('Hux'))
    print(starkiller.addCrewMember('Ren'))
    print(starkiller.addCrewMember('Phasma'))
    print(starkiller.addCrewMember('Finn'))
    print(starkiller.getCrewSize())