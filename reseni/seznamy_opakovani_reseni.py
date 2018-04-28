
reky = [
    'Berounka',
    'Jizera',
    'Otava',
    'Labe',
    'Lužnice',
    'Ploučnice',
    'Sázava',
    'Vltava',
]

print('reky:', reky)

# vypiš druhou polovinu seznamu řek
polovina = len(reky)//2     # celočíselné dělení
print('druha polovina:', reky[polovina:])

# vytvoř (a vypiš) nový seznam obsahující pouze řeky začínající na L
nove_reky = []
for reka in reky:
    if reka.startswith('L'):    # nebo: if reka[0] == 'L':
        nove_reky.append(reka)

# přidej do svého nového seznamu Berounku a Otavu
nove_reky.extend(['Berounka', 'Otava'])
print('novy seznam:', nove_reky)


# vytvoř seznam řek, které v prvním seznamu jsou, ale v novém ne
jen_prvni = []
for reka in reky:
    if reka not in nove_reky:
        jen_prvni.append(reka)
print('jen v prvnim:', jen_prvni)


# vypiš jednu náhodně vybranou řeku z původního seznamu
import random
print('nahodna:', random.choice(reky))


# "zamíchej" seznam řek a postupně jej vyprázdni, odstraňovanou hodnotu
# vždy vypiš na obrazovku
random.shuffle(reky)
while reky:
    print(reky.pop())
