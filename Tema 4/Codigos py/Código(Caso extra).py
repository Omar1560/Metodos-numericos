import math
def x(t): return 0.05 * math.cos(10 * t + math.pi/6)
t0, h = 0.1, 0.005
vel = (x(t0 - 2*h) - 8*x(t0 - h) + 8*x(t0 + h) - x(t0 + 2*h)) / (12 * h)
print(f"Velocidad aprox: {vel:.10f} m/s")
