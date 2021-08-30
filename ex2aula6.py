def verifica(n):
    if n == 0:
        return("0 é um numero Neutro")
    if n > 0:
        return("P")
    else:
        return("N")
n = float(input("\ndigite um valor numérico: "))
res = verifica(n)
print(res)