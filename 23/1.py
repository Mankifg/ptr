"""
1. naloga - Jesti travo je tudi težko delo!
Ovčka Mica svoje dni preživi na pašniku in žveči travo. Čeprav se to zdi kot preprosto opravilo, si je Mica zadala stroga pravila, da obdrži svoj brezhiben kožuh.

Mica vsak dan lahko poje samo določeno količino rastlin podano z n. Prav tako je samo v ravni črti in lahko naleti na naslednje rastline, ki jih predstavljajo različni simboli: travna bilka( | ), marjetica( M ), zemlja oz. ni rastline( / ) in regrat( R ). Mora se pa držati naslednjih pravil:

Ne sme pojesti zemlje
Lahko poje samo največ tri travne bilke zapored(naslednjo mora izpustiti, če ni vmes kakšne druge rastline ali zemlje)
Po regratu ne sme jesti marjetic
Mica po jedla dokler ne bo sita, tj. dokler ne poje n rastlin.

Kot vhod v prvi vrstici dobiš n, ki predstavlja koliko rastlin mora Mica pojesti. V naslednji vrstici dobiš dolžino zaporedje rastlin na katerega bo Mica naletela. V tretji vrstici dobiš zaporedje znakov, ki predstavlja rastline v takem vrstnem redu, kot na njih naleti Mica.

Izpiši na kateri zaporedni rastlini Mica neha jesti. Začnemo šteti z 1.

Če ti je ta naloga pretežka, upoštevaj samo, da Mica ne sme pojesti zemlje."""

trava = "|"
marjetica = "M"
dirt = "/"
regrat = "R"

n = int(input())
l = int(input())
seq = input()


eaten = 0

streak = 0

for ele in seq:
    if not ele == trava:
        ...
    
    if ele == dirt:
        continue

    eaten += 1

print(eaten)
