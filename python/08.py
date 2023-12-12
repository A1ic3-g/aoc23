from inputs import Input08
from pprint import pprint
import math


def getNodes(nodesString: str) -> dict[str, tuple[str, str]]:
    return {
        (node := line.split(" ", 2))[0]: tuple((node[2][1:-1]).split(", "))
        for line in nodesString.splitlines()
    }


def getNumStepsPart1(steps: str, nodes: dict[str, tuple[str, str]]) -> int:
    numSteps = 0
    currentNode = ("AAA", nodes["AAA"])
    while currentNode[0] != "ZZZ":
        for step in steps:
            numSteps += 1
            if step == "L":
                name = currentNode[1][0]
                currentNode = (name, nodes[name])
            elif step == "R":
                name = currentNode[1][1]
                currentNode = (name, nodes[name])
            if currentNode[0] == "ZZZ":
                return numSteps


def getStartNodes(
    nodes: dict[str, tuple[str, str]]
) -> list[tuple[str, tuple[str, str]]]:
    startNodes = []
    for key, node in nodes.items():
        if key.endswith("A"):
            startNodes.append((key, node))
    return startNodes


def getNumStepsPart2(steps: str, nodes: dict[str, list[str]]) -> int:
    
    currentNodes = getStartNodes(nodes)
    nodeSteps = {}
    for node in currentNodes:
        nodeSteps[node[0]] = getNumStepsInduvidualPart2(steps, node)
    return math.lcm(* nodeSteps.values())

def getNumStepsInduvidualPart2(steps, node):
    numSteps = 0
    while True:
        for step in steps:
            numSteps += 1
            if step == "L":
                name = node[1][0]
                node  = (name, nodes[name])
            elif step == "R":
                name = node[1][1]
                node = (name, nodes[name])
            if node[0].endswith("Z"):
                return numSteps

if __name__ == "__main__":
    nodes = getNodes(Input08["nodes"])
    pprint(getNumStepsPart1(Input08["steps"], nodes))
    pprint(getNumStepsPart2(Input08["steps"], nodes))
