# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#  для всех значений предикат.

print('Программа для проверки истинности утверждения')
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z', end=' ')
print('для всех значений предикат.')
print()
print('  X', '  Y', '  Z' + '\t'*2+'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z', sep='\t')
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            print(x, y, z, end='\t'*3+'    ', sep='\t')
            p1 = not (x or y or z)
            p2 = not x and not y and not z
            print(p1 == p2)
