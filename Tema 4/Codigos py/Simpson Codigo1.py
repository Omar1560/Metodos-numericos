def simpson_error(n):
    if n % 2 != 0:
        return "ERROR: El método de Simpson 1/3 requiere obligatoriamente un número PAR de subintervalos (n)."
    return "Cálculo procediendo..."

print(simpson_error(15))
