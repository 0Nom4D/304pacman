##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## Phantom
##

class Phantom:
    def __init__(self, mapFile: list) -> None:
        self.positionX, self.positionY = self.getPositionFromMap(mapFile)
        pass

    def getPositionFromMap(self, fileContent: list):
        for absc in range(len(fileContent)):
            for ordn in range(len(fileContent[absc])):
                if fileContent[absc][ordn] == 'F':
                    return absc, ordn
        return -1, -1

    def getPosition(self):
        return self.positionX, self.positionY