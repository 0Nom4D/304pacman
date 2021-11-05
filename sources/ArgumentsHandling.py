##
## EPITECH PROJECT, 2021
## Tmp304pacman
## File description:
## ArgumentsHandling
##

from genericpath import isfile
from os import stat

fileChars = ['0', '1', 'F', 'P']

class ArgChecker:
    def __init__(self, args: list) -> None:
        self.file = args[0]
        self.fst_char = args[1]
        self.snd_char = args[2]

    def analyseParams(self) -> bool:

        def isEmpty(filename: str) -> bool:
            if stat(filename).st_size == 0:
                return True
            return False

        if not isfile(self.file):
            return False
        elif isEmpty(self.file):
            return False
        if len(self.fst_char) != 1 or len(self.snd_char) != 1:
            return False
        if self.fst_char in fileChars or self.snd_char in fileChars or self.fst_char == self.snd_char:
            return False
        if not self.checkFileContent():
            return False
        return True

    def checkFileContent(self) -> bool:
        basic_size = 0
        total_size = 0
        line_size = 0

        with open(self.file) as fd:
            for line in fd:
                line = line.lstrip().rstrip().rstrip('\n')
                if basic_size == 0:
                    basic_size = len(line)
                else:
                    line_size = len(line)
                    if basic_size != line_size:
                        return False
                for idx in range(len(line)):
                    if line[idx] not in fileChars:
                        return False
                total_size += 1
        if total_size < 3:
            return False
        fd.close()
        return True