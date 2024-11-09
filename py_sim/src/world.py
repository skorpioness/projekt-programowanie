import organism

# class World:
#     def __init__(self):
#         self.liveList: list[src.organism.Organism] = []
#         self.iterator: int = 0
#         self.orgList: dict[str, int] = {}

#     def addOrganism(self, organism: 'src.organism.Organism'):
#         organism.setID(self.iterator)
#         self.liveList.append(organism)
#         self.iterator += 1
#         if self.orgList[organism.getName()] == None:
#             self.orgList[organism.getName()] = 0
#         self.orgList[organism.getName()] += 1

#     def checkForOrganism(self, pos: list[int]) -> 'src.organism.Organism':
#         for o in self.liveList:
#             orgPos = o.getPos()
#             if orgPos[0] == pos[0] and orgPos[1] == pos[1] and o.isDead() == False:
#                 return o
#         return None

#     def playTurn(self):
#         for o in self.liveList:
#             o.makeTurn()

class World:
    def __init__(self):
        self._organismList: list[organism.Organism] = []
        self._next_id: int = 0

    def getOrganismList(self):
        return self._organismList

    def newOrganism(self, type: str, x: int, y: int) -> None:
        o = None
        match type:
            case 'Wolf':     o = organism.Wolf(x, y, self, self._next_id)
            case 'Sheep':    o = organism.Sheep(x, y, self, self._next_id)
            case 'Turtle':   o = organism.Turtle(x, y, self, self._next_id)
            case 'Lion':     o = organism.Lion(x, y, self, self._next_id)
            case 'Scorpion': o = organism.Scorpion(x, y, self, self._next_id)
            case 'Grass':    o = organism.Grass(x, y, self, self._next_id)
            case 'Guarana':  o = organism.Guarana(x, y, self, self._next_id)
            case 'Milkweed': o = organism.Milkweed(x, y, self, self._next_id)
            case _: raise Exception("Unknown organism type")

        self._organismList[str(self._next_id)] = o
        self._next_id += 1

    def delOrganism(self, id: int) -> None:
        for o in self._organismList:
            if o.getID() == id:
                self._organismList.remove(o)

    def checkCoord(self, x, y) -> None|organism.Organism:
        for o in self._organismList:
            if o.getPosX() == x and o.getPosY() == y:
                return o
        return None

    def playTurn(self):
        tempList = sorted(sorted(self._organismList, key = lambda x: x.getID()), key = lambda x: x.getInitiative())
        for o in tempList:
            if o in self._organismList:
                o.takeTurn()

