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
        self.map = self.extractMap(args[0], args[1], args[2])
        self.phantom = Phantom(self.map)
        self.pacman = Pacman(self.map)
        if self.phantom.getPosition() == (-1, -1) or self.pacman.getPosition() == (-1, -1):
            exit(84)
        pass

    def extractMap(self, mapFile: str, wallChar: str, emptyChar: str) -> list:
        map = list()

        with open(mapFile) as fd:
            for line in fd:
                line = line.replace('\n', '')
                if len(line) != 0:
                    line = line.replace('0', emptyChar).replace('1', wallChar)
                    map.append(line)
            while '' in map:
                map.remove('')
            if not len(map):
                exit(84)
        fd.close()
        return (map)

    def displayMap(self):
        for line in self.map:
            print(line)