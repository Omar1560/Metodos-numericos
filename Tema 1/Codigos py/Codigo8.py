

def secante_p1(f, x0, x1, tol, max_iter=20):
    print(f"{'Iter':<5}{'xi-1':<10}{'xi':<10}{'xi+1':<10}{'Ea (%)':<10}")
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("División por cero detectada.")
            return None
      
        x_sig = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        ea = abs((x_sig - x1) / x_sig) * 100 if x_sig != 0 else 0
        
        print(f"{i+1:<5}{x0:<10.4f}{x1:<10.4f}{x_sig:<10.4f}{ea:<10.4f}")
        
        if ea < tol:
            return x_sig
        
        x0 = x1
        x1 = x_sig
    return x1

f_s1 = lambda x: x**3 - 2*x**2 - 5
print(f"\nRaíz calculada: {secante_p1(f_s1, 2.0, 3.0, 0.01):.4f}")
