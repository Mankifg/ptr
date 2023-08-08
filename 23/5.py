"""5. naloga - Hranjenje Blåhaja
Naš predragi morski pes Blåhaj je lačen in rabi tvojo pomoč! V njegovi soseski je malo morje hrane, vendar jo mora zaradi časovne stiske pojesti med potovanjem. Pomagaj mu najti pot, da bo pojedel največ hrane!

Kot vhod v program boš dobil 2D sliko morja v katerem se nahaja Blåhaj (predstavljen s črko B), hrana (H) in prazen prostor v morju (.). Blåhaj se vedno premika en korak v desno lahko pa se medtem premakne tudi en korak gor ali dol (torej v vsak naslednji stolpec lahko gre diagonalno gor, diagonalno dol ali naravnost). S temi premiki mu pomagaj pojesti največ hrane.

Najprej kot vhodne podatke dobimo dve števili, ki sta višina in širina morja. Nato sledi še slika, ki je sestavljena iz zgoraj omenjenih znakov.
"""

def update(t):
    t[-1] = t[-1] + 1
    for i in range(len(t)-1,0,-1):
        if t[i] == 3:
            t[i] = 0
            t[i-1] = t[i-1] + 1
        
    return t

def with_toggle_go(toggle):
    curr_v = visina_b
    curr_s = sirina_b
    food = 0
    for elem in toggle:
        # elem = 0,1,2
        elem =  elem - 1
        curr_v = curr_v + elem
        curr_s = curr_s + 1
        try:
            if b[curr_v][curr_s] == "H":
                food = food + 1
        except IndexError:
            curr_v = curr_v - elem
    return food
                    
visina = int(input())
sirina = int(input())

b = []
for i in range(visina):
    b.append(list(input()))
    


for i in range(len(b)):
    if "B" in b[i]:
        visina_b = i
        sirina_b = b[i].index("B")

for i in range(len(b)):
    c = b[i]
    take_off = sirina_b - len(b[i])
    c = c[take_off::]
    b[i] = c

sirina_b = b[visina_b].index("B")
toggle = [0]*len(b[0])

m_food = 0

for _ in range(3**len(toggle)):
    toggle = update(toggle)
    #? print(toggle)
    food  = with_toggle_go(toggle)
    m_food = max(m_food,food)
    
print(m_food)    