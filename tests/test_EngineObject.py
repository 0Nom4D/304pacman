##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## test_Main
##

from sources.EngineObjects.EngineObject import EngineObj
from sources.EngineObjects.Phantom import Phantom
from sources.EngineObjects.Pacman import Pacman
from sys import argv
from pytest import *

class TestEngineObjects:

    basic_map = ["1111111111", "0000000000", "0000000000", "0000000000",
                "00000F0000", "0000000000", "00000P0000", "0000000000",
                "0000000000", "1111111111"]

    empty_map = ["1111111111", "1111111111"]

    def test_fetching_with_basic_map(self):
        newObj_1 = EngineObj(self.basic_map, '1', 'P')
        newObj_2 = EngineObj(self.basic_map, '1', 'F')
        assert newObj_1.getPosition() == (6, 5)
        assert newObj_2.getPosition() == (4, 5)

    def test_fetching_with_empty_map(self):
        newObj_1 = EngineObj(self.empty_map, '1', 'P')
        newObj_2 = EngineObj(self.empty_map, '1', 'F')
        assert newObj_1.getPosition() == (-1, -1)
        assert newObj_2.getPosition() == (-1, -1)

    def test_create_pacman(self):
        newPacman = Pacman(self.basic_map, '1', 'P')
        assert newPacman.getPosition() == (6, 5)

    def test_create_phantom(self):
        newPhantom = Phantom(self.basic_map, '1', 'F')
        assert newPhantom.getPosition() == (4, 5)