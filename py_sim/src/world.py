class World:

    def __init__(self):
        self._organismList = []
        self._next_id = 0

    def addOrganism(self, organism):
        organism.setID(self._next_id)
        self._organismList.append(organism)
        self._next_id += 1

    def getOrganismList(self):
        return self._organismList

    def checkCoord(self, x, y):
        for o in self._organismList:
            if o.getPosX() == x and o.getPosY() == y:
                return o
        return None

    def playTurn(self):
        tempList = sorted(sorted(self._organismList, key=lambda x: x.getID()), key=lambda x: x.getInitiative())
        for o in tempList:
            if o in self._organismList:
                o.takeTurn()