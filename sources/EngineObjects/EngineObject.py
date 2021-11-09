##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## EngineObject
##

class EngineObj:
    """
    Class designating an object such as a Phantom or a Pacman Player

    Attributes
    -------
    positionX: int
        X position of the object within the file
    positionY: int
        Y position of the object within the file
    """
    def __init__(self, mapContent: list, wallChar: str, checkedChar: str) -> None:
        self.positionX, self.positionY = self.getPositionFromMap(mapContent, wallChar, checkedChar)
        pass

    def getPositionFromMap(self, fileContent: list, wallChar: str, checkedChar: str):
        """
        Gets the position of the asked object within the map file

        Parameters
        -------
        fileContent: list
            Map passed as a list of strings
        wallChar: str
            Character designating a wall
        checkedChar: str
            Character to seek in the map

        Returns
        -------
        Tuple of the position X and Y of the asked object
        -1, -1 if the asked object isn't found in the map
        """
        for absc in range(len(fileContent)):
            for ordn in range(len(fileContent[absc])):
                if fileContent[absc][ordn] == checkedChar:
                    return absc, ordn
        return -1, -1

    def getPosition(self) -> int:
        """
        Gets the position of the object

        Returns
        -------
        Position of the object
        """
        return (self.positionX, self.positionY)
