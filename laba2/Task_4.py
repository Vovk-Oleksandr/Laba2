x = float(input("Сторона X: "))
y = float(input("Сторона Y: "))
z = float(input("Сторона Z: "))
t = float(input("Сторона T: "))

area1 = 0.5 * x * y
area2 = 0.5 * z * t

total_area = area1 + area2
print(f"Приблизна площа чотирикутника: {total_area}")
