import copy

g_invalidScores = [1, 2, 4, 5]
g_possiblePointsCombination = set()


def isValid(score):
    if score in g_invalidScores or score < 0:
        return False
    return True


def hitStopCondition(score):
    return score == 0 or not isValid(score)


def countValidPoint(history, pointIndex):
    historyCopy = copy.copy(history)
    historyCopy[pointIndex] += 1
    return historyCopy


def computeScorePossibilities(score, history=[0, 0, 0, 0]):
    # Next score for each type of point
    #                field goal, touchdown, touchdownX1, touchdownX2
    nextPointScores = [score - 3, score - 6, score - 7, score - 8]

    for pointIndex in range(0, len(nextPointScores)):
        nextPointScore = nextPointScores[pointIndex]
        if hitStopCondition(nextPointScore):
            if isValid(nextPointScore):
                # Hit an stop condition with a valid value
                # Count the point and add current history as a possible points combination
                g_possiblePointsCombination.add(tuple(countValidPoint(history, pointIndex)))
                return
        else:
            # Count point as valid and then compute next valid points
            computeScorePossibilities(nextPointScore, countValidPoint(history, pointIndex))


# Define number of possibilities for each team score
def countScorePossibilities(score):
    g_possiblePointsCombination.clear()
    computeScorePossibilities(score)
    # This next line was used in tests and it returns a set with the possibilities for a given individual score
    # print(g_possiblePointsCombination)
    return len(g_possiblePointsCombination)


# Calculate combination of possibilites for a final game score
def countPossibleCombinations(strScore):
    scores = strScore.split("x")

    homeScore = int(scores[0])
    visitorScore = int(scores[1])

    homeScorePossibilities = countScorePossibilities(homeScore)
    visitorScorePossibilities = countScorePossibilities(visitorScore)

    possibleCombinations = homeScorePossibilities*visitorScorePossibilities
    return possibleCombinations

# The next code lines were used in tests and they return the result of possible combinations for a given final game score
# strScore = input("Placar do jogo (eg. 0x0): ")
# possibleCombinations = countPossibleCombinations(strScore)
# print(possibleCombinations)