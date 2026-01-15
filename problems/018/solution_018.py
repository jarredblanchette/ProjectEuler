# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#   _3_
#  _7_4
#  2_4_6
# 8 5_9_3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                     75
#                    95 64
#                   17 47 82
#                  18 35 87 10
#                 20 04 82 47 65
#                19 01 23 75 03 34
#               88 02 77 73 07 63 67
#             99 65 04 28 06 16 70 92
#            41 41 26 56 83 40 80 70 33
#           41 48 72 33 47 32 37 16 94 29
#          53 71 44 65 25 43 91 52 97 51 14
#         70 11 33 28 77 73 17 78 39 68 17 57
#        91 71 52 38 17 14 91 43 58 50 27 29 48
#       63 66 04 68 89 53 67 30 73 16 69 87 40 31
#      04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)

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

if __name__ == '__main__':
 
    simple_representation = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]
    example  = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]

    # simple_representation = example 

    elements = initaliseTree(simple_representation)

    print(getCostTo(elements[-1].id))



