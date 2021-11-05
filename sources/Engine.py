##
## EPITECH PROJECT, 2021
## Tmp304pacman
## File description:
## Pacman
##

from sources.EngineObjects.Phantom import Phantom
from sources.EngineObjects.Pacman import Pacman

class Engine:
    """
    304pacman Main engine class

    Attributes
    -------
    wallChar: str
        Character assigned to a wall
    emptySpace: str
        Character assigned to an empty space
    map: list
        Content of the file passed as parameter
    map_size: int
        Size of the map
    phantom: Phantom
        Class having the informations about the ghost
    pacman: Pacman
        Class having the informations about the pacman
    """
    def __init__(self, args: list) -> None:
        # Chars Properties
        self.wallChar = args[1]
        self.emptySpace = args[2]

        # Map Properties
        self.map = self.extractMap(args[0])
        self.map_size = len(self.map)
        self.phantom = Phantom(self.map, self.wallChar, 'F')
        self.pacman = Pacman(self.map, self.wallChar, 'P')
        if self.phantom.getPosition() == (-1, -1) or self.pacman.getPosition() == (-1, -1):
            exit(84)
        pass

    def extractMap(self, mapFile: str) -> list:
        """
        Exctracts the content of the file passed as parameter

        Parameters
        -------
        mapFile: str
            Path to the file containing the map

        Returns
        -------
        List containing the file content
        """
        map = list()

        with open(mapFile) as fd:
            for line in fd:
                line = line.replace('\n', '')
                if len(line) != 0:
                    line = line.replace('0', self.emptySpace).replace('1', self.wallChar)
                    map.append(line)
            while '' in map:
                map.remove('')
            if not len(map):
                exit(84)
        fd.close()
        return (map)

    def displayMap(self) -> None:
        """
        Displays the map

        Returns
        -------
        None
        """
        for line in self.map:
            print(line)

    def runDijkstra(self) -> None:
        """
        Run Dijkstra Shortest Path Algorithm

        Returns
        -------
        None
        """
        checkedPositions = list()
        directionsOffsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fX, fY = self.phantom.getPosition()

        def computeDijkstra(lastIdx: int, x: int, y: int, x_offset: int, y_offset: int) -> bool:
            """
            Computes a loop of the Dijkstra Algorithm

            Parameters
            -------
            lastIdx: int
                Integer label of the last computed position
            x: int
                Index of the line where Dijkstra's loop begins
            y: int
                Index of the character on a line where Dijkstra's loop begins
            x_offset: int
                Offset to apply to the x position defining the next position where we're going to apply Dijkstra algorithm
            y_offset: int
                Offset to apply to the y position defining the next position where we're going to apply Dijkstra algorithm
            """

            def isPositionValid(x: int, y: int) -> bool:
                """
                Checks if a position still is in the map

                Parameters
                -------
                x: int
                    X position to check
                y: int
                    Y position to check

                Returns
                -------
                True if the position is valid, otherwise False
                """
                if x < 0 or x >= self.map_size or y < 0 or y >= self.map_size:
                    return False
                return True

            def isEmptyChar(char: str) -> bool:
                """
                Checks if the character passed as parameter is an empty space

                Parameters
                -------
                char: str
                    Character to check


                Returns
                -------
                True if the character passed as parameter is an empty space, otherwise False
                """
                return (char == self.emptySpace)

            _x, _y = x + x_offset, y + y_offset
            if not isPositionValid(_x, _y):
                return False
            nextCharOnDirection = self.map[_x][_y]
            if isEmptyChar(nextCharOnDirection):
                copy = list(self.map[_x])
                copy[_y] = str((lastIdx + 1) % 10)
                self.map[_x] = ''.join(copy)
                checkedPositions.append([(_x, _y), int(self.map[_x][_y])])
                return False
            elif nextCharOnDirection == 'P':
                return True
            return False

        for offset in directionsOffsets:
            if computeDijkstra(0, fX, fY, offset[0], offset[1]):
                return
        for position in checkedPositions:
            for offset in directionsOffsets:
                if computeDijkstra(position[1], position[0][0], position[0][1], offset[0], offset[1]):
                    return

    def runShortestPath(self) -> None:
        """
        304pacman main loop

        Returns
        -------
        None
        """
        self.runDijkstra()
        self.displayMap()