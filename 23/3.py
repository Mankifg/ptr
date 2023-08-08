'''
3. naloga - Morski radar
Kot vsi vemo, so na različnih odsekih cest različne omejitve. Omejitve obstajajo tudi na morju. Na cesti se uporabljajo km/h, na morju pa morski vozli oziroma morska milja na uro. Ena morska milja je 1852 metra. Mi pa ne bomo komplicirali in uporabili kar kilometre :). Turisti bi se radi z ladjo bi pripeljali z ene lokacije na drugo. Natančno vemo kje vzdolž poti se nahajajo znaki za omejitev hitrosti in kakšne so te omejitve. Zanima nas, koliko časa bomo potrebovali, da pridemo na cilj.

Vhodni podatki
Preberite dolžino naše poti, začetno omejitev, število znakov in nato v vsaki vrstici par števil. Prvo v paru predstavlja koliko kilometrov od začetne lokacije se nahaja znak, drugo pa omejitev napisano na znaku.

vse razdalje so v kilometrih
vse hitrosti so v kilometrih na uro
znaki bodo podani glede na oddaljenost od začetka naše poti (najbližji najprej)
'''

import math

pot, z_omj, znaki = list(map(int,input().split(' ')))
razdalje, hitrosti = [],[]

for i in range(znaki):
    r,h = list(map(int,input().split(' ')))
    razdalje.append(r)
    hitrosti.append(h)

time = 0
z_r = 0
for i in range(znaki):
    if razdalje[i] > pot:
        break
    add_time = (razdalje[i] - z_r) / z_omj
    time = time + add_time
    z_omj = hitrosti[i]
    z_r = razdalje[i]
    #print(add_time)
    
add_time = (pot - z_r) / z_omj   

time = time + add_time

time = time*100
time = math.floor(time)
print(time/100)