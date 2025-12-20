# Импорт необходимых модулей
import numpy as np
import cmath
import math

# Исходные данные
R12 = 27
R23 = 22
R34 = 14
R41 = 23
R15 = 81
R45 = 50
R49 = 55
R56 = 14
R67 = 42
R69 = 60
R97 = 43
R72 = 12
R82 = 22
R83 = 30
E1  = 150
E2  = 105

# Вычисление собственных сопротивлений контуров
r = np.zeros((6, 6))
r[0][0] = R41 + R15 + R45
r[1][1] = R12 + R15 + R56 + R67 + R72
r[2][2] = R45 + R56 + R69 + R49
r[3][3] = R69 + R67 + R97
r[4][4] = R34 + R49 + R97 + R72 + R82 + R83
r[5][5] = R83 + R82 + R23

# Вычисление взаимных сопротивлений контуров
r[0][1] = -R15
r[0][2] = -R45
r[1][2] = -R56

r[1][0] = r[0][1]
r[1][3] = -R67
r[1][4] = -R72

r[2][0] = r[0][2]
r[2][1] = r[1][2]
r[2][3] = -R69

r[2][4] = -R49
r[3][1] = r[1][3]
r[3][2] = r[2][3]

r[3][4] = -R97
r[4][1] = r[1][4]
r[4][2] = r[2][4]

r[4][3] = r[3][4]
r[4][5] = -R82 - R83

r[5][4] = r[4][5]

# Расчёт контурных ЭДС
Ek = np.zeros(6)
Ek[1] = E1
Ek[2] = E2
Ek[4] = -E2
Ek[3] = -E1
Ek[5] = 0

# Метод Зейделя
def sysEqSolver(A, b, x0=None, eps=1e-6, max_iter=10000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = A.shape[0]
    if x0 is None:
        x = np.zeros(n, dtype=float)
    else:
        x = np.array(x0, dtype=float)

    # Проверка диагональных элементов
    if np.any(np.isclose(np.diag(A), 0.0)):
        raise ValueError("На диагонали есть нули — метод неприменим без перестановок.")

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])          # уже обновлённые значения
            s2 = np.dot(A[i, i+1:], x_old[i+1:])  # старые значения
            x[i] = (b[i] - s1 - s2) / A[i, i]
        # критерий остановки (макс. норма)
        if np.max(np.abs(x - x_old)) < eps:
            return x
    raise RuntimeError("Не сошлось за max_iter итераций")

x = sysEqSolver(r, Ek)

print(x)