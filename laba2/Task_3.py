def inside_circle(x, y, a, b, R):
    return (x - a) ** 2 + (y - b) ** 2 < R ** 2

a = float(input("Центр кола (a): "))
b = float(input("Центр кола (b): "))
R = float(input("Радіус кола (R): "))

p1 = float(input("Координата x точки P: "))
p2 = float(input("Координата y точки P: "))
f1 = float(input("Координата x точки F: "))
f2 = float(input("Координата y точки F: "))
l1 = float(input("Координата x точки L: "))
l2 = float(input("Координата y точки L: "))

count = 0
if inside_circle(p1, p2, a, b, R):
    count += 1
if inside_circle(f1, f2, a, b, R):
    count += 1
if inside_circle(l1, l2, a, b, R):
    count += 1

print(f"Кількість точок всередині кола: {count}")
