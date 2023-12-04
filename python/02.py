from inputs import Input02
from pprint import pprint
import re


colours = {"red": 12, "green": 13, "blue": 14}

def getColourPairs(roundStrings) -> list[list[str]]:
    roundList = []
    for colour in roundStrings:
        pos = re.search("[a-z]", colour).start()
        roundList.append([colour[:pos], colour[pos:]])
    return roundList

def isValidRound(colourpairs):
    for pair in colourpairs:
        if colours[pair[1]] < int(pair[0]):
            return False
    return True

def isValidGame(game):
    rounds = [r.split(",") for r in game.split(";")]
    for r in rounds:
        if not isValidRound(getColourPairs(r)):
            return False
    return True

def getGamePower(game):
    coloursMin = {"red": 0, "green": 0, "blue": 0}
    rounds = [r.split(",") for r in game.split(";")]
    for r in rounds:
        pairs = getColourPairs(r)
        for pair in pairs:
            if coloursMin[pair[1]] < int(pair[0]):
                coloursMin[pair[1]] = int(pair[0])
    return coloursMin["red"] * coloursMin["green"] * coloursMin["blue"]

def part01():
    validGameSum = 0
    games = [g[g.find(":")+1:] for g in Input02.replace(" ", "").splitlines() if g != ""]
    for i, game in enumerate(games):
        if isValidGame(game):
            validGameSum += i+1
    
    return validGameSum

def part02():
    powerGameSum = 0
    games = [g[g.find(":")+1:] for g in Input02.replace(" ", "").splitlines() if g != ""]
    for game in games:
        powerGameSum += getGamePower(game)
    return powerGameSum

if __name__ == "__main__":
    print(part01())
    print(part02())






        
        
    