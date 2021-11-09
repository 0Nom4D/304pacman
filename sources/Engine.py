##
## EPITECH PROJECT, 2021
## Tmp304pacman
## File description:
## Pacman
##

from sources.EngineObjects.Phantom import Phantom
from sources.EngineObjects.Pacman import Pacman

class Engine:
    def __init__(self, args: list) -> None:
        # Chars Properties
        self.wallChar = args[1]
        self.emptySpace = args[2]

        # Map Properties
        self.map = self.extractMap(args[0])
        self.map_size = len(self.map)
        self.phantom = Phantom(self.map, self.wallChar, 'F')
        self.pacman = Pacman(self.map, self.wallChar, 'P')
        pass

    def extractMap(self, mapFile: str) -> list:
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
        for line in self.map:
            print(line)

    def runDijkstra(self) -> None:
        checkedPositions = list()
        directionsOffsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fX, fY = self.phantom.getPosition()

        def computeDijkstra(lastIdx: int, x: int, y: int, x_offset: int, y_offset: int) -> bool:

            def isPositionValid(x: int, y: int) -> bool:
                if x < 0 or x >= self.map_size or y < 0 or y >= len(self.map[0]):
                    return False
                return True

            def isEmptyChar(char: str) -> bool:
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
        self.runDijkstra()
        self.displayMap()