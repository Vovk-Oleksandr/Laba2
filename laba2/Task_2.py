import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Катет 1 трикутника 1: "))
b1 = float(input("Катет 2 трикутника 1: "))
a2 = float(input("Катет 1 трикутника 2: "))
b2 = float(input("Катет 2 трикутника 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза 1: {h1}")
print(f"Гіпотенуза 2: {h2}")

if h1 > h2:
    print("Гіпотенуза 1 більша")
elif h2 > h1:
    print("Гіпотенуза 2 більша")
else:
    print("Гіпотенузи рівні")
