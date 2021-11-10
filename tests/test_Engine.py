##
## EPITECH PROJECT, 2021
## 304pacman [WSL: Ubuntu-20.04]
## File description:
## test_Engine
##

from sources.Engine import Engine
from pytest import raises

class TestEngine:

    basic_map_str = "++++++++++\n          \n          \n          \n     F    \n          \n     P    \n          \n          \n++++++++++\n"

    basic_map = ["++++++++++", "          ", "          ", "          ",
                "     F    ", "          ", "     P    ", "          ",
                "          ", "++++++++++"]

    result_cells_map3 = ["+++++++", "+F123P+", "+++++++"]

    cells_map3 = ["1111111", "1F000P1", "1111111"]

    too_tiny_map = ["++++++++++++", "++++++++++++"]

    too_tiny_map_str = "++++++++++++\n++++++++++++\n"

    def test_basic_map_engine(self):
        args = ["maps/map01", "+", " "]
        myEngine = Engine(args)

        assert myEngine.map == self.basic_map
        assert myEngine.map_size == 10
        assert myEngine.phantom.getPosition() == (4, 5)
        assert myEngine.pacman.getPosition() == (6, 5)

    def test_too_tiny_map(self):
        args = ["maps/too_tiny_map", "+", " "]
        myEngine = Engine(args)

        assert myEngine.map == self.too_tiny_map
        assert myEngine.map_size == 2
        assert myEngine.phantom.getPosition() == (-1, -1)
        assert myEngine.pacman.getPosition() == (-1, -1)

    def test_extract_basic_map(self):
        args = ["maps/map01", "+", " "]
        myEngine = Engine(args)

        assert myEngine.extractMap("maps/map01") == self.basic_map
        assert myEngine.map_size == 10

    def test_extract_eof_map(self):
        args = ["maps/eof_map", "+", " "]
        myEngine = Engine(args)

        assert myEngine.extractMap("maps/eof_map") == self.basic_map
        assert myEngine.map_size == 10

    def test_extract_empty_map(self):
        args = ["maps/empty_map", "+", " "]

        with raises(SystemExit) as pytest_exit:
            Engine(args)
        assert pytest_exit.type == SystemExit
        assert pytest_exit.value.code == 84

    def test_basic_map_display(self, capsys):
        args = ["maps/map01", "+", " "]
        myEngine = Engine(args)

        myEngine.displayMap()
        captured = capsys.readouterr()
        assert captured[0] == self.basic_map_str

    def test_map_display(self, capsys):
        args = ["maps/too_tiny_map", "+", " "]
        myEngine = Engine(args)

        myEngine.displayMap()
        captured = capsys.readouterr()
        assert captured[0] == self.too_tiny_map_str

    def test_valid_djikstra(self):
        args = ["maps/3_cells_map", "+", " "]
        myEngine = Engine(args)

        myEngine.runDijkstra()
        assert myEngine.map == self.result_cells_map3

    def test_already_solved(self):
        args = ["maps/close_char_map", "+", " "]
        myEngine = Engine(args)

        myEngine.runDijkstra()
        assert myEngine.map == ["++++", "+FP+", "++++"]

    def test_run_shortest_path(self, capsys):
        args = ["maps/3_cells_map", "+", " "]
        myEngine = Engine(args)

        myEngine.runShortestPath()
        captured = capsys.readouterr()
        assert myEngine.map == self.result_cells_map3
        assert captured[0] == "+++++++\n+F123P+\n+++++++\n"

    def test_run_shortest_path_on_already_solved(self, capsys):
        args = ["maps/close_char_map", "+", " "]
        myEngine = Engine(args)

        myEngine.runShortestPath()
        captured = capsys.readouterr()
        assert myEngine.map == ["++++", "+FP+", "++++"]
        assert captured[0] == "++++\n+FP+\n++++\n"