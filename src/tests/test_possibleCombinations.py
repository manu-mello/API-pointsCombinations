import possibleCombinations


def test_isValid():
    assert possibleCombinations.isValid(0) == True
    assert possibleCombinations.isValid(1) == False
    assert possibleCombinations.isValid(2) == False
    assert possibleCombinations.isValid(3) == True
    assert possibleCombinations.isValid(4) == False
    assert possibleCombinations.isValid(5) == False
    assert possibleCombinations.isValid(6) == True
    assert possibleCombinations.isValid(7) == True
    assert possibleCombinations.isValid(8) == True
    assert possibleCombinations.isValid(20) == True
    assert possibleCombinations.isValid(-1) == False
    assert possibleCombinations.isValid(-15) == False

def test_hitStopCondition():
    assert possibleCombinations.hitStopCondition(0) == True
    assert possibleCombinations.hitStopCondition(1) == True
    assert possibleCombinations.hitStopCondition(2) == True
    assert possibleCombinations.hitStopCondition(3) == False
    assert possibleCombinations.hitStopCondition(4) == True
    assert possibleCombinations.hitStopCondition(5) == True
    assert possibleCombinations.hitStopCondition(6) == False
    assert possibleCombinations.hitStopCondition(7) == False 
    assert possibleCombinations.hitStopCondition(8) == False
    assert possibleCombinations.hitStopCondition(24) == False
    assert possibleCombinations.hitStopCondition(-1) == True
    assert possibleCombinations.hitStopCondition(-12) == True

def test_countValidPoint():
    assert possibleCombinations.countValidPoint([0, 0, 0, 0], 0) == [1, 0, 0, 0]
    assert possibleCombinations.countValidPoint([0, 0, 0, 0], 1) == [0, 1, 0, 0]
    assert possibleCombinations.countValidPoint([0, 0, 0, 0], 2) == [0, 0, 1, 0]
    assert possibleCombinations.countValidPoint([0, 0, 0, 0], 3) == [0, 0, 0, 1]
    assert possibleCombinations.countValidPoint([0, 0, 0, 1], 0) == [1, 0, 0, 1]
    assert possibleCombinations.countValidPoint([0, 0, 1, 0], 1) == [0, 1, 1, 0]
    assert possibleCombinations.countValidPoint([0, 1, 0, 0], 2) == [0, 1, 1, 0]
    assert possibleCombinations.countValidPoint([1, 0, 0, 0], 3) == [1, 0, 0, 1] 
    assert possibleCombinations.countValidPoint([1, 0, 0, 0], 0) == [2, 0, 0, 0]
    assert possibleCombinations.countValidPoint([0, 1, 0, 0], 1) == [0, 2, 0, 0]
    assert possibleCombinations.countValidPoint([0, 0, 1, 0], 2) == [0, 0, 2, 0]
    assert possibleCombinations.countValidPoint([0, 0, 0, 1], 3) == [0, 0, 0, 2]

def test_computeScorePossibilities():
    possibleCombinations.computeScorePossibilities(3)
    assert possibleCombinations.g_possiblePointsCombination == {(1, 0, 0, 0)}
    possibleCombinations.g_possiblePointsCombination.clear()
    possibleCombinations.computeScorePossibilities(6)
    assert possibleCombinations.g_possiblePointsCombination == {(0, 1, 0, 0), (2, 0, 0, 0)}
    possibleCombinations.g_possiblePointsCombination.clear()
    possibleCombinations.computeScorePossibilities(12)
    assert possibleCombinations.g_possiblePointsCombination == {(4, 0, 0, 0), (0, 2, 0, 0), (2, 1, 0, 0)}
    possibleCombinations.g_possiblePointsCombination.clear()
    possibleCombinations.computeScorePossibilities(3, [1, 0, 3, 3])
    assert possibleCombinations.g_possiblePointsCombination == {(2, 0, 3, 3)}
    possibleCombinations.g_possiblePointsCombination.clear()

def test_countScorePossibilities():
    assert possibleCombinations.countScorePossibilities(3) == 1
    assert possibleCombinations.countScorePossibilities(6) == 2
    assert possibleCombinations.countScorePossibilities(7) == 1
    assert possibleCombinations.countScorePossibilities(8) == 1
    assert possibleCombinations.countScorePossibilities(9) == 2
    assert possibleCombinations.countScorePossibilities(10) == 1
    assert possibleCombinations.countScorePossibilities(11) == 1
    assert possibleCombinations.countScorePossibilities(12) == 3
    assert possibleCombinations.countScorePossibilities(13) == 2
    assert possibleCombinations.countScorePossibilities(24) == 9
    assert possibleCombinations.countScorePossibilities(42) == 28
    # assert possibleCombinations.countScorePossibilities(70) == 90

def test_countPossibleCombinations():
    # assert possibleCombinations.countPossibleCombinations("0x0") == 0
    # assert possibleCombinations.countPossibleCombinations("3x6") == 2
    # assert possibleCombinations.countPossibleCombinations("7x11") == 1
    # assert possibleCombinations.countPossibleCombinations("8x13") == 2
    # assert possibleCombinations.countPossibleCombinations("12x12") == 9
    # assert possibleCombinations.countPossibleCombinations("14x15") == 12
    # assert possibleCombinations.countPossibleCombinations("18x24") == 45
    # assert possibleCombinations.countPossibleCombinations("25x30") == 98
    # assert possibleCombinations.countPossibleCombinations("24x42") == 252
    # assert possibleCombinations.countPossibleCombinations("13x44") == 56
    # # assert possibleCombinations.countPossibleCombinations("11x70") == 90
    assert possibleCombinations.countPossibleCombinations("60x60") == 4096