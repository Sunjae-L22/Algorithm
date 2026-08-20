from solution import init, addTower, runSimulation

test_map = [[0, 2, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 1, 3, 0, 0, 0]]


init(6, test_map)
addTower(1, 4, 2)
addTower(3, 1, 3)