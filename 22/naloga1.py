inp = input("Vnesi kovance! (loči jih s presledkom) >")
inp = inp.split(" ")

if inp[-1] == "":
    inp.pop(-1)

for i in range(len(inp)):
    inp[i] = int(inp[i])

diff = []

for i in range(len(inp)):
    if not inp[i] in diff:
        diff.append(inp[i])

count = []

for i in range(len(diff)):
    count.append(inp.count(diff[i]))

product = 0
for i in range(len(diff)):
    product = product + diff[i] * count[i]


diff, count = zip(*sorted(zip(diff, count)))


for i in range(len(diff)):
    print(f"{diff[i]}€: {count[i]}x")


print(f"Skupaj: {product}€")
