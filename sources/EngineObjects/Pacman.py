##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## Pacman
##

class Pacman:
    def __init__(self, mapContent: list) -> None:
        self.positionX, self.positionY = self.getPositionFromMap(mapContent)
        pass

    def getPositionFromMap(self, fileContent: list):
        for absc in range(len(fileContent)):
            for ordn in range(len(fileContent[absc])):
                if fileContent[absc][ordn] == 'P':
                    return absc, ordn
        return -1, -1

    def getPosition(self):
        return self.positionX, self.positionY