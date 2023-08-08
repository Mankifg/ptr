"""2. naloga - Pojedina čevapčičev
Letos Združenje Jedcev Čevapčičev (ZJČ) pripravlja svojo prvo organizirano pojedino čevapčičev! Odločili so se, da bojo naročili kar 10000 čevapčičev! Za pripravo sta se pa javila dva kuharja, vendar prvi pripravlja porcije po 5 in drugi porcije po 9 čevapčičev. Zveza zdaj ni prepričana kako bi razdelila delo med njiju in te prosi, da jim poveš na koliko različnih načinov lahko ta dva kuharja skupaj pripravita točno 10000 čevapčičev.

Primer
Za lažji primer lahko probamo pripraviti 100 čevapčičev. Z veliko računanja pridemo do možnosti:

2 porciji prvi kuhar in 10 porcij drugi kuhar (2⋅5+10⋅9=100
)
11 porciji prvi kuhar in 5 porcij drugi kuhar (11⋅5+5⋅9=100
)
20 porciji prvi kuhar in 0 porcij drugi kuhar (20⋅5+0⋅9=100
)
To so edine celoštevilske možnosti, da sestavimo porcije za 100 čevapčičev.

Prav tako je vredno omembe, da negativne porcije (npr. −7⋅5+15⋅9=100
 ) ne veljajo.

V tem primeru program vrne število 3, ker je toliko možnih rešitev."""

def find_possiblity(num):
    kuharji = [5,9]
    diff = 0
    
    a = int(num / kuharji[0])+1
    b = int(num / kuharji[1])+1
    
    for i in range(0,a):
        for j in range(0,b):
            if i * kuharji[0] + j * kuharji[1] == num:
                diff = diff+1
                #print(f"{i} * {kuharji[0]} + {j} * {kuharji[1]} = {num}, {diff}")
    
    return diff
    
    
find = find_possiblity(1000)
print(find)