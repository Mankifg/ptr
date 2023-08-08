"""4. naloga - Mala ribiška ladja Umag 2
V nedeljo, 9. julija 2023 zgodaj zjutraj, je Slovenska tiskovna agencija sporočila, da je mala ribiška ladja Umag 2 s hrvaške ekonomsko ekološke cone zašla na sidrišče Luke Koper. Stekla je široka reševalna akcija pod vodstvom slovenske obalne straže. Reševalna ladja Luške kapitanije Koper je že na poti. Prebija se med ladjami, ki so zasidrane na sidrišču. Čas hitro teče in upamo, da bo pomoč prispela pravočasno in ladjo Umag 2 pospremila s sidrišča nazaj do hrvaške ekonomsko ekološke cone.

Slovenska obalna straža potrebuje pomoč programerjev, ki naj straži pošljejo rešitev, kako hitro lahko reševalna ladja Luške kapitanije Koper z vašo pomočjo prispe do izgubljene ladje Umag 2.

Na sidrišču velja sidrni red. Sidrišče je razdeljeno na M krat N sidrnih mest (v obliki kvadratov), kjer lahko ladje sidrajo. Ladje so lahko zelo dolge in zato daljše ladje zasedejo po dolžini več sidrnih mest. Nobena ladja pa ni tako široka, da bi po širini potrebovala več kot eno sidrno mesto. Veljajo še naslednja pravila:

Ladje so lahko sidrane zgolj v smeri sever – jug ali vzhod – zahod (ne glede na to kje je premec in kje krma). Prepovedane so ostale smeri sidranja, tako da lahko zasidrana ladja zasede vedno sosednja mesta le v smeri sever – jug ali vzhod – zahod, drugih pa ne.
Dve ladji ne smeta uporabiti istega sidrnega mesta.
Ladje lahko sidrajo tako, da različne ladje zasedejo katera koli sosednja sidrna mesta.
Plovba po sidrišču pravokotne oblike poteka izključno preko nezasedenih sidrnih mest in sicer obvezno v smereh sever – jug ali vzhod – zahod (in to v obeh smereh, podobno kot so sidrane ladje).
Po teh pravilih se po sidrišču gibljejo tudi reševalne ladje, vlačilci in druge kratke ladje (dolge največ eno sidrno mesto). Na spodnji sliki je narisan primer položajev zasedenih mest na sidrišču ter položaja ladje Umag 2 in reševalne ladje.

Primer

Naloga
Izračunaj, koliko sidrnih mest mora prečkati reševalna ladja, ki hiti na pomoč ladji Umag 2."""

# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        # for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            if maze[node_position[1]][node_position[0]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                (child.position[1] - end_node.position[1]) ** 2
            )
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)

# my code
 
def change(x, y):
    b[y][x] = 1


import numpy as np

m, n = list(map(int, input().split(" ")))

b = np.zeros((m, n))

se = list(map(int, input().split(" ")))
start = (se[0], se[1])
end = (se[2], se[3])

n = int(input())

for _ in range(n):
    data = list(map(int, input().split(" ")))

    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]

    if x1 == x2:
        key_x = x1

        for y in range(y1, y2 + 1):
            b[y][key_x] = 1

    elif y1 == y2:
        key_y = y1
        for x in range(x1, x2 + 1):
            b[key_y][x] = 1

path = astar(b, start, end)

for i in range(len(path)):
    b[path[i][1]][path[i][0]] = 9

b[start[1]][start[0]] = 3
b[end[1]][end[0]] = 3

print(len(path) - 1)

# print(path)
# print(b)

"""
10 10
2 2 6 6
5
1 3 1 7
1 3 6 3
5 3 5 6
8 5 8 7
3 8 8 8
"""