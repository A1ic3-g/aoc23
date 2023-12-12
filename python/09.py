from inputs import Input09

def getNextValue(sequence: list[int]) -> int:
    diffSequences = [sequence]
    while isNotZeroSequence(diffSequences[-1]):
        diffSequences.append(getDifferenceSequence(diffSequences[-1]))
    print(sequence)
    for i in range(len(diffSequences)-1, -1, -1):
        toAdd = diffSequences[i][-1]
        #print(diffSequences[i])
        #input()
        #print(diffSequences[i-1])
        diffSequences[i-1].append(getNewLastElement(diffSequences[i-1], toAdd))
        #print(diffSequences[i-1])
        #print()

    print(diffSequences[0])
    print()
    #print(diffSequences[0][-1])
    return diffSequences[0][-1]

def getNewLastElement(sequence: list[int], toAdd: int) -> int:
    return sequence[-1] + toAdd

def getDifferenceSequence(sequence: list[int]) -> list[int]:
    newSequence = []
    for i in range(len(sequence)-1):
        newSequence.append(sequence[i+1]-sequence[i])
    return newSequence

def isNotZeroSequence(sequence: list[int]) -> bool:
    #print(sequence)
    return all(sequence)

def part1(sequences: list[list[int]]):
    return sum([getNextValue(sequence) for sequence in sequences])

if __name__ == "__main__":
    Input09 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
    sequences = [[int(value) for value in line.split()] for line in Input09.splitlines()]
    print(part1(sequences))