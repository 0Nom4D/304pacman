#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Tmp304pacman
## File description:
## main
##

from sources.ArgumentsHandling import ArgChecker
from sources.exitCode import exitCode
from sources.Engine import Engine
from sys import argv

def print_usage() -> int:
    print("USAGE")
    print("\t./304pacman file c1 c2")
    print("DESCRIPTION")
    print("\tfile\tfile describing the board, using the following characters:")
    print("\t\t\t'0' for an empty square")
    print("\t\t\t'1' for a wall")
    print("\t\t\t'F' for the ghost's position")
    print("\t\t\t'P' for Pacman's position")
    print("\tc1\tcharacter to display for a wall")
    print("\tc2\tcharacter to display for an empty space")
    return (exitCode.OK)

def main() -> int:
    if len(argv) == 2 and (argv[1] == '-h' or argv[1] == "--help"):
        return (print_usage())
    elif (len(argv)) != 4:
        return (exitCode.ERROR)
    Handler = ArgChecker(argv[1:])
    if not Handler.analyseParams():
        return (exitCode.ERROR)
    PacmanRunner = Engine(argv[1:]).runShortestPath()
    return (exitCode.OK)

if __name__ == "__main__":
    exit(main())
