n = int(input("Vnesi število. >"))

if n < 1:
    print("Neveljaven vnos")
    exit()

fib = [1, 1]

for i in range(n - 1):
    fib.append(fib[-1] + fib[-2])

print(f"Tvoje število: {fib[-1]}")
