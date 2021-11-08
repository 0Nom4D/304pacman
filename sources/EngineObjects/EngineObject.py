##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## EngineObject
##

class EngineObj:
    def __init__(self, mapContent: list, wallChar: str, checkedChar: str) -> None:
        self.positionX, self.positionY = self.getPositionFromMap(mapContent, wallChar, checkedChar)
        pass

    def getPositionFromMap(self, fileContent: list, wallChar: str, checkedChar: str):
        for absc in range(len(fileContent)):
            for ordn in range(len(fileContent[absc])):
                if fileContent[absc][ordn] == checkedChar:
                    return absc, ordn
        return -1, -1

    def isInWalls(self, content: list, x: int, y: int, wallChar: str) -> bool:
        if content[x + 1][y] == wallChar and content[x - 1][y] == wallChar and content[x][y + 1] == wallChar and content[x][y - 1] == wallChar:
            return True
        return False

    def getPosition(self) -> int:
        return (self.positionX, self.positionY)