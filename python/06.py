from inputs import Input06
from timeit import timeit


def doesWin(heldTime: int, totalTime: int, record: int) -> bool:
    return heldTime * (totalTime - heldTime) > record


def getWaysToWinNaive(time, record) -> int:
    waysToWin = 0
    for heldTime in range(1, time - 1):
        if doesWin(heldTime, time, record):
            waysToWin += 1
    return waysToWin

def getWaysToWinOptimised(time: int, record: int) -> int:
    waysToWin = 0
    midpoint = time // 2
    left = midpoint
    right = midpoint + 1

    waysToWin += waysToWinTopHalf(right, time, record)
    waysToWin += waysToWinBottomHalf(left, time, record)

    return waysToWin

def getWaysToWinOptimised2(time: int, record: int) -> int:
    waysToWin = 0
    midpoint = time // 2
    left = midpoint
    right = midpoint + 1

    waysToWin += waysToWinTopHalf(right, time, record)*2

    return waysToWin

def waysToWinTopHalf(start: int, time: int, record: int) -> bool:
    ways = 0
    for pos in range(start, time -1):
        if doesWin(pos, time, record):
            ways += 1
        else:
            return ways
    return ways

def waysToWinBottomHalf(start, time, record) -> bool:
    ways = 0
    for pos in range(start, 0, -1):
        if doesWin(pos, time, record):
            ways += 1
        else:
            return ways
    return ways

def combineInts(nums: list[int]) -> int:
    newInt = ""
    for num in nums:
        newInt += str(num)
    return int(newInt)

if __name__ == "__main__":
    waysProduct1 = 1
    times = Input06["Time"]
    records = Input06["Distance"]
    for time, record in zip(times, records):
        waysProduct1 *= getWaysToWinOptimised(time, record)
        if waysProduct1 == getWaysToWinOptimised2(time, record):
            print(time, " ", record)
    print(waysProduct1)
    newTime = combineInts(times)
    newRecord = combineInts(records)
    print(newTime, " ", newRecord)
    print(getWaysToWinOptimised2(newTime, newRecord))
    print(getWaysToWinOptimised(newTime, newRecord))
    print(getWaysToWinNaive(newTime, newRecord))


    

    
    