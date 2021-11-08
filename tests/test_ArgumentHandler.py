##
## EPITECH PROJECT, 2021
## 304pacman
## File description:
## ArgumentHandlerTests
##

from sources.ArgumentsHandling import ArgChecker
from pytest import *

class TestArgChecker:
    def test_unknown_file(self):
        Checker = ArgChecker(["file", "@", " "])
        assert Checker.analyseParams() == False

    def test_empty_file(self):
        Checker = ArgChecker(["maps/empty_map", "@", " "])
        assert Checker.analyseParams() == False

    def test_replacing_character_not_char(self):
        Checker = ArgChecker(["maps/map01", "free", "aled"])
        assert Checker.analyseParams() == False

    def test_replacing_with_already_known_char(self):
        Checker = ArgChecker(["maps/map01", "1", " "])
        assert Checker.analyseParams() == False

    def test_replacing_with_already_known_char_2(self):
        Checker = ArgChecker(["maps/map01", "@", "1"])
        assert Checker.analyseParams() == False

    def test_both_same_replacing_chars(self):
        Checker = ArgChecker(["maps/map01", "+", "+"])
        assert Checker.analyseParams() == False

    def test_too_tiny_map(self):
        Checker = ArgChecker(["maps/too_tiny_map", "+", " "])
        assert Checker.checkFileContent() == False

    def test_inconsistent_map(self):
        Checker = ArgChecker(["maps/inconsistent_map", "+", " "])
        assert Checker.checkFileContent() == False

    def test_map_with_not_map_char(self):
        Checker = ArgChecker(["maps/unknown_map_chars", "+", " "])
        assert Checker.checkFileContent() == False

    def test_map_with_multiple_characters(self):
        Checker = ArgChecker(["maps/multiple_characters", "+", " "])
        assert Checker.checkFileContent() == False

    def test_normal_map(self):
        Checker = ArgChecker(["maps/map01", "+", " "])
        assert Checker.checkFileContent() == True

    def test_wrong_map_argchecker(self):
        Checker = ArgChecker(["maps/multiple_characters", "+", " "])
        assert Checker.analyseParams() == False

    def test_normal_map_arg_checker(self):
        Checker = ArgChecker(["maps/map01", "+", " "])
        assert Checker.analyseParams() == True