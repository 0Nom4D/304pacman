##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## EngineObject
##

class EngineObj:
    def __init__(self, mapContent: list, checkedChar: str) -> None:
        self.positionX, self.positionY = self.getPositionFromMap(mapContent, checkedChar)
        pass

    def getPositionFromMap(self, fileContent: list, checkedChar: str):
        for absc in range(len(fileContent)):
            for ordn in range(len(fileContent[absc])):
                if fileContent[absc][ordn] == checkedChar:
                    return absc, ordn
        return -1, -1

    def getPosition(self) -> int:
        return (self.positionX, self.positionY)