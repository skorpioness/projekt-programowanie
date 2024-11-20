from typing import Self
import random

import pygame


class Organism:
    def __init__(self, pos_x: int, pos_y: int, strength: int, initiative: int, world: 'world.World', id: int):
        self.id = id
        self.name = None
        self.world = world
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.strength = strength
        self.initiative = initiative
        self.type = None


    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getName(self):
        return self.name

    def getPosX(self):
        return self.pos_x

    def setPosX(self, pos_x):
        self.pos_x = pos_x

    def getPosY(self):
        return self.pos_y

    def setPosY(self, pos_y):
        self.pos_y = pos_y

    def getStrength(self):
        return self.strength

    def setStrength(self, strength):
        self.strength = strength

    def getInitiative(self):
        return self.initiative

    def getType(self):
        return self.type

    def action(self):
        pass

    def collision(self, target: Self):
        pass

    def takeTurn(self):
        pass

    def draw(self, screen):
        if hasattr(self, 'image') and self.image:
            screen.blit(self.image, (self.pos_x, self.pos_y))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (self.pos_x, self.pos_y, 20, 20))

class Animal(Organism):
    def __init__(self, pos_x, pos_y, strength, initiative, world: 'world.World', id):
        super().__init__(pos_x, pos_y, strength, initiative, world, id)
        self.dead = False
        self.next_x = pos_x
        self.next_y = pos_y
        self.type = 'animal'

    def getNextPosX(self):
        return self.next_x

    def getNextPosY(self):
        return self.next_y

    def setNextPosX(self, pos_x):
        self.next_x = pos_x

    def setNextPosY(self, pos_y):
        self.next_y = pos_y

    def action(self):
        pass

    def collision(self, opponent: Self):
        pass

    def takeTurn(self):
        self.planMove()
        self.action()
        self.move()

    def planMove(self):
        move = 20 if random.randint(0, 1) == 1 else -20

        if random.randint(0, 1) == 1:
            pos = self.getPosX()
            if pos + move < 0 or pos + move > 380:
                move *= -1
            self.setNextPosX(pos + move)
        else:
            pos = self.getPosY()
            if pos + move < 0 or pos + move > 380:
                move *= -1
            self.setNextPosY(pos + move)

    def move(self):
        pos_x = self.getNextPosX()
        pos_y = self.getNextPosY()
        target = self.world.checkCoord(pos_x, pos_y)

        if target is not None:
            if target.getName() == self.getName():
                return
            else:
                target.collision(self)

                if target.type == 'animal':
                    self.attack(target)
                elif target.type == 'plant':
                    target.collision(self)
                    target.kill()

        if self in self.world.getOrganismList():
            self.setPosX(self.getNextPosX())
            self.setPosY(self.getNextPosY())


    def attack(self, target: Self):
        if (
                self.getStrength() == target.getStrength() and self.getID() < target.getID()) or self.getStrength() < target.getStrength():
            self.kill()
        else:
            target.kill()

    def kill(self):
        self.world.removeOrganism(self)
        self.dead = True


class Plant(Organism):
    def __init__(self, pos_x, pos_y, strength, world: 'world.World', id):
        super().__init__(pos_x, pos_y, strength, 0, world, id)

    def kill(self):
        self.dead = True
        self.world.removeOrganism(self)

    def collision(self, opponent: Animal):
        print(
            f"{self.getName()} with ID {self.getID()} has been eaten by {opponent.getName()} with ID {opponent.getID()}.")
        self.kill()

class Wolf(Animal):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 9, 5, world, id)
        self.name = 'Wolf'
        self.image = pygame.image.load('assets/wolf.png')
        self.image = pygame.transform.scale(self.image, (20, 20))


class Sheep(Animal):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 4, 4, world, id)
        self.name = 'Sheep'
        self.image = pygame.image.load('assets/sheep.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

class Turtle(Animal):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 2, 1, world, id)
        self.name = 'Turtle'
        self.image = pygame.image.load('assets/turtle.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
    def action(self):
        if random.randint(0, 3) != 0:
            print(f"{self.getName()} with ID {self.getID()} didn't move this turn")
            self.setNextPosX(self.getPosX())
            self.setNextPosY(self.getPosY())

    def collision(self, opponent: Animal):
        if opponent.strength < 5:
            print(
                f"{self.getName()} with ID {self.getID()} pushed back {opponent.getName()} with ID {opponent.getID()}")
            opponent.setNextPosX(opponent.getPosX())
            opponent.setNextPosY(opponent.getPosY())
            opponent.move()


class Lion(Animal):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 11, 7, world, id)
        self.name = 'Lion'
        self.image = pygame.image.load('assets/lion.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
    def collision(self, opponent: Animal):
        if opponent.strength < 5:
            print(
                f"{self.getName()} with ID {self.getID()} pushed back {opponent.getName()} with ID {opponent.getID()}")
            opponent.setNextPosX(opponent.getPosX())
            opponent.setNextPosY(opponent.getPosY())
            opponent.move()


class Scorpion(Animal):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 2, 4, world, id)
        self.name = 'Scorpion'
        self.image = pygame.image.load('assets/scorpion.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
    def collision(self, opponent: Animal):
        print(
            f"{self.getName()} with ID {self.getID()} poisoned and killed {opponent.getName()} with ID {opponent.getID()}")
        opponent.kill()


class Grass(Plant):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 0, world, id)
        self.name = 'Grass'
        self.image = pygame.image.load('assets/grass.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

class Guarana(Plant):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 0, world, id)
        self.image = pygame.image.load('assets/guarana.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

    def collision(self, target: Animal):
        print(
            f"{self.getName()} with ID {self.getID()} upgraded {target.getName()} with ID {target.getID()} strength by 3")
        target.setStrength(target.getStrength() + 3)


class Milkweed(Plant):
    def __init__(self, pos_x, pos_y, world: 'world.World', id: int):
        super().__init__(pos_x, pos_y, 0, world, id)
        self.image = pygame.image.load('assets/milkweed.png')
        self.image = pygame.transform.scale(self.image, (20, 20))