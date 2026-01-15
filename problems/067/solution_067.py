
from typing import List
class Node:
    id: int
    value: int
    parentIds: List[int] | None 
    childIds: List[int] | None 

    def __init__(self, value: int,  id: int, parents: List[int] | None = [], children: List[int] | None = []):
        self.value = value
        self.id = id
        self.parentIds = parents
        self.childIds = children

    def addChild(self, child: int):
        if self.childIds is None: self.childIds = []
        self.childIds.append(child)

    def __str__(self) -> str:
        sAcc = f"Node: {self.id}\n\
\tvalue: {self.value}\n\
\tparentIds: {self.parentIds}\n\
\tchildIds: {self.childIds}\n\
        "
        return sAcc


def memorise(f):
    known = {}

    def wrapper(*args, **kwargs):
        if (args, str(kwargs)) not in known:
            known[(args, str(kwargs))] = f(*args, **kwargs)
        return known[(args, str(kwargs))]

    return wrapper
    
@memorise
def getCostTo(id: int | None):
    if id is None: return 0

    parentIds = elements[id].parentIds
    myValue = elements[id].value

    if parentIds is None or parentIds == []:
        return myValue
    return max([getCostTo(parentId) + myValue for parentId in [pid for pid in parentIds]])

def initaliseTree(simple_representation: List[int]) -> List[Node]:
        elements: List[Node] = []

        finalElement:Node = Node(0,-1,[],[])

        node_index = 0
        rowHead = 0
        prevRowHead = 0

        elements: List[Node] = []

        for rowIndex, row in enumerate(simple_representation):
            prevRowHead = rowHead
            rowHead = node_index

            has_next_row = rowIndex < len(simple_representation)-1

            for indexInRow, element in enumerate(row):
                isFirstElement = indexInRow == 0
                isLastElement = indexInRow == len(row)-1

                value = element
                id = node_index

                parentIds: List[int] = []

                if not isLastElement:
                    parentIds.append(prevRowHead + indexInRow)
                if not isFirstElement:
                    parentIds.append(prevRowHead + indexInRow - 1)

                childrenIds = []
                if not has_next_row: 
                    childrenIds = [finalElement.id]
                    finalElement.parentIds.append(id)


                elements.append(Node(value, id, parentIds,childrenIds))

                for parentId in parentIds:
                    elements[parentId].childIds.append(id)
                
                node_index += 1
        
        elements.append(finalElement)

        return elements

if __name__ == "__main__":
    fileName= "0067_triangle.txt"
    
    triangle: List[List[int]] = [[]]
    triangle.pop()

    with open(fileName,'r') as fp:
        for line in fp:
            line= line.strip('\n')
            elements = line.split(' ')
            elements = [int(element) for element in elements]
            triangle.append(elements)

    elements:List[Node]= initaliseTree(triangle)

    print(getCostTo(elements[-1].id))

