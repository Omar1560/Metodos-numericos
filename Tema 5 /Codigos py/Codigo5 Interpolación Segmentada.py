def spline_lineal_manual(x):
    # Datos base: {(0, 2), (2, 6), (5, 15)}
    if 0 <= x <= 2:
        return 2 + ((6 - 2) / (2 - 0)) * (x - 0)
    elif 2 < x <= 5:
        return 6 + ((15 - 6) / (5 - 2)) * (x - 2)
    else:
        return None

print("=" * 45)
print(f"Spline Lineal - Valor en x = 1: {spline_lineal_manual(1):.2f}")
print(f"Spline Lineal - Valor en x = 4: {spline_lineal_manual(4):.2f}")
print("=" * 45)
