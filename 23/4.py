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

from collections import deque

def is_valid_move(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    visited = set()
    queue = deque([(start, 0)])  # Queue elements: ((row, col), distance)
    visited.add(start)
    
    while queue:
        (row, col), distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, new_row, new_col) and (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), distance + 1))
                visited.add((new_row, new_col))
    
    return -1


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

path = shortest_path(b, start, end)

print(path)     

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