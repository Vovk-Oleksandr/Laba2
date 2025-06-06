n = int(input("Введіть n: "))
nums = input("Введіть числа через пробіл: ").split()
divisors = [int(x) for x in nums]

result = []
for i in range(1, n + 1):
    if all(i % d == 0 for d in divisors):
        result.append(i)

print("Числа, що підходять:")
print(result)
