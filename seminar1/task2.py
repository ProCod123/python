print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')


def assertionСhecking(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    if left == right:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')


assertionСhecking(0, 0, 0)
assertionСhecking(0, 0, 1)
assertionСhecking(0, 1, 0)
assertionСhecking(0, 1, 1)
assertionСhecking(1, 0, 0)
assertionСhecking(1, 0, 1)
assertionСhecking(1, 1, 0)
assertionСhecking(1, 1, 1)
