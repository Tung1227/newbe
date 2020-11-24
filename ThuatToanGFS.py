import heapq
from _collections import defaultdict

data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']

weight = {}
weight['A'] = 6
weight['B'] = 3
weight['C'] = 4
weight['D'] = 8
weight['E'] = 3
weight['F'] = 1
weight['G'] = 6
weight['H'] = 2
weight['I'] = 5
weight['J'] = 4
weight['K'] = 2
weight['L'] = 0
weight['M'] = 4
weight['N'] = 0
weight['O'] = 4



class Node:
    def __init__(self, label, h=0):
        self.label = label
        self.h = h

    def __lt__(self, other):
        return self.h < other.h

    def __eq__(self, other):
        return self.h == self.other

    def __str__(self):
        return f"({self.label}, {self.h})"

def Print_Frontier(frontier):
    for i in frontier:
        print(i,end=" ; ")
    print()



def GBFS(start, end):
    frontier = [start]
    explored = [start.label]
    heapq.heapify(frontier)
    while len(frontier) > 0:
        Print_Frontier(frontier)
        currentNode = heapq.heappop(frontier)
        if currentNode.label == end.label:
            print("Found")
            return
        for neighbor in data[currentNode.label]:
            if neighbor not in explored:
                explored.append(neighbor)
                heapq.heappush(frontier, Node(neighbor,weight[neighbor]))
    print("NotFound")


if __name__ == '__main__':
    GBFS(Node('A',weight['A']), Node('L',weight['L']))
