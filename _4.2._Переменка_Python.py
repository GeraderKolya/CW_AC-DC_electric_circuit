# Импорт необходимых модулей
import numpy as np
import cmath
import math

# Исходные данные
R = np.array([60., 5., 10., 0., 300.])
C = np.array([3000.e-6, 800.e-6, 2400.e-6])
L = np.array([0.e-3, 26.e-3, 12.e-3])
f = 40.
Um = 160.
T = 0.025
pi = math.pi

# Перевод сопротивлений в комплексный вид для первой гармоники
wh1 = 2 * pi * f
Uh1m = Um

ZR = R + 0j
ZL = L * wh1 * 1j
ZC = 1j * (-1.) / (wh1 * C)

# Метод эквивалентных преобразований для первой гармоники
Z1 = ZR[4] + ZC[2]
Z2 = ZL[1] + ZC[1]
Z3 = ZC[0] + ZR[0]
Z4 = ZR[2] + ZC[0]
Z5 = ZR[1] + ZC[1]
Z6 = ZR[2] + ZC[2]

Z7 = (Z1 * Z2)/(Z1 + Z2)
Z8 = (Z4 * Z5)/(Z4 + Z5)
Z9 = (ZL[2] * Z3)/(ZL[2] + Z3)

Z10 = Z7 + Z8
Z11 = (Z10 * Z9)/(Z10 + Z9)
Zeq = ZL[2] + Z11 + Z6

# Расчёт для первой гармоники
Uh1cplx = complex(Uh1m, 0)
Uh1cplxAD = Uh1cplx
Ih1cplx = Uh1cplx/Zeq
Uh1cplxCD = Ih1cplx * Z6
Uh1cplxAB = Ih1cplx * ZL[2]
Uh1cplxZ11 = Ih1cplx * Z11
Ih1cplxZ10 = Uh1cplxZ11/Z10
Uh1cplxZ7 = Ih1cplxZ10 * Z7
Uh1cplxBE = Uh1cplxZ7
Uh1cplxZ8 = Ih1cplxZ10 * Z8
Uh1cplxEC = Uh1cplxZ8
Ih1cplxZ2 = Uh1cplxZ7/Z2
Uh1cplxL2 = Ih1cplxZ2 * ZL[1]
Ih1cplxZ4 = Uh1cplxZ8/Z4
Uh1cplxC11 = Ih1cplxZ4 * ZC[0]
Ih1cplxZ3 = Uh1cplxZ11/Z3
Uh1cplxC12 = Ih1cplxZ3 * ZC[0]
Ih1cplxBE = Uh1cplxBE/Z1
Ih1cplxR2C2 = Uh1cplxEC/Z5
Ih1cplxL3 = Uh1cplxZ11/ZL[2]

# Перевод сопротивлений в комплексный вид для второй гармоники
wh2 = 2 * 2 * pi * f
Uh2m = .5 * Um

ZR = R + 0j
ZL = L * wh2 * 1j
ZC = 1j * (-1.) / (wh2 * C)

# Метод эквивалентных преобразований для второй гармоники
Z1 = ZR[4] + ZC[2]
Z2 = ZL[1] + ZC[1]
Z3 = ZC[0] + ZR[0]
Z4 = ZR[2] + ZC[0]
Z5 = ZR[1] + ZC[1]
Z6 = ZR[2] + ZC[2]

Z7 = (Z1 * Z2)/(Z1 + Z2)
Z8 = (Z4 * Z5)/(Z4 + Z5)
Z9 = (ZL[2] * Z3)/(ZL[2] + Z3)

Z10 = Z7 + Z8
Z11 = (Z10 * Z9)/(Z10 + Z9)
Zeq = ZL[2] + Z11 + Z6

# Расчёт для второй гармоники
Uh2cplx = complex(Uh2m, 0)
Uh2cplxAD = Uh2cplx
Ih2cplx = Uh2cplx/Zeq
Uh2cplxCD = Ih2cplx * Z6
Uh2cplxAB = Ih2cplx * ZL[2]
Uh2cplxZ11 = Ih2cplx * Z11
Ih2cplxZ10 = Uh2cplxZ11/Z10
Uh2cplxZ7 = Ih2cplxZ10 * Z7
Uh2cplxBE = Uh2cplxZ7
Uh2cplxZ8 = Ih2cplxZ10 * Z8
Uh2cplxEC = Uh2cplxZ8
Ih2cplxZ2 = Uh2cplxZ7/Z2
Uh2cplxL2 = Ih2cplxZ2 * ZL[1]
Ih2cplxZ4 = Uh2cplxZ8/Z4
Uh2cplxC11 = Ih2cplxZ4 * ZC[0]
Ih2cplxZ3 = Uh2cplxZ11/Z3
Uh2cplxC12 = Ih2cplxZ3 * ZC[0]
Ih2cplxBE = Uh2cplxBE/Z1
Ih2cplxR2C2 = Uh2cplxEC/Z5
Ih2cplxL3 = Uh2cplxZ11/ZL[2]

# Вычисление максимальных значений для первой гармоники
Umh1AD = abs(Uh1cplxAD)
Umh1CD = abs(Uh1cplxCD)
Umh1AB = abs(Uh1cplxAB)
Umh1BE = abs(Uh1cplxBE)
Umh1EC = abs(Uh1cplxEC)
Umh1L2 = abs(Uh1cplxL2)
Umh1C11 = abs(Uh1cplxC11)
Umh1C12 = abs(Uh1cplxC12)

Imh1B1 = abs(Ih1cplx)
Imh1B2 = abs(Ih1cplxL3)
Imh1B3 = abs(Ih1cplxBE)
Imh1B4 = abs(Ih1cplxZ4)
Imh1B5 = abs(Ih1cplxZ2)
Imh1B6 = abs(Ih1cplxR2C2)
Imh1B7 = abs(Ih1cplxZ3)

# Вычисление максимальных значений для второй гармоники
Umh2AD = abs(Uh2cplxAD)
Umh2CD = abs(Uh2cplxCD)
Umh2AB = abs(Uh2cplxAB)
Umh2BE = abs(Uh2cplxBE)
Umh2EC = abs(Uh2cplxEC)
Umh2L2 = abs(Uh2cplxL2)
Umh2C11 = abs(Uh2cplxC11)
Umh2C12 = abs(Uh2cplxC12)

Imh2B1 = abs(Ih2cplx)
Imh2B2 = abs(Ih2cplxL3)
Imh2B3 = abs(Ih2cplxBE)
Imh2B4 = abs(Ih2cplxZ4)
Imh2B5 = abs(Ih2cplxZ2)
Imh2B6 = abs(Ih2cplxR2C2)
Imh2B7 = abs(Ih2cplxZ3)

# Вычисление углов сдвига фаз для первой гармоники (в радианах)
ph1UAD = cmath.phase(Uh1cplxAD)
ph1UCD = cmath.phase(Uh1cplxCD)
ph1UAB = cmath.phase(Uh1cplxAB)
ph1UBE = cmath.phase(Uh1cplxBE)
ph1UEC = cmath.phase(Uh1cplxEC)
ph1UL2 = cmath.phase(Uh1cplxL2)
ph1UC11 = cmath.phase(Uh1cplxC11)
ph1UC12 = cmath.phase(Uh1cplxC12)

ph1IB1 = cmath.phase(Ih1cplx)
ph1IB2 = cmath.phase(Ih1cplxL3)
ph1IB3 = cmath.phase(Ih1cplxBE)
ph1IB4 = cmath.phase(Ih1cplxZ4)
ph1IB5 = cmath.phase(Ih1cplxZ2)
ph1IB6 = cmath.phase(Ih1cplxR2C2)
ph1IB7 = cmath.phase(Ih1cplxZ3)

# Вычисление углов сдвига фаз для второй гармоники (в радианах)
ph2UAD = cmath.phase(Uh2cplxAD)
ph2UCD = cmath.phase(Uh2cplxCD)
ph2UAB = cmath.phase(Uh2cplxAB)
ph2UBE = cmath.phase(Uh2cplxBE)
ph2UEC = cmath.phase(Uh2cplxEC)
ph2UL2 = cmath.phase(Uh2cplxL2)
ph2UC11 = cmath.phase(Uh2cplxC11)
ph2UC12 = cmath.phase(Uh2cplxC12)
ph2IB1 = cmath.phase(Ih2cplx)
ph2IB2 = cmath.phase(Ih2cplxL3)
ph2IB3 = cmath.phase(Ih2cplxBE)
ph2IB4 = cmath.phase(Ih2cplxZ4)
ph2IB5 = cmath.phase(Ih2cplxZ2)
ph2IB6 = cmath.phase(Ih2cplxR2C2)
ph2IB7 = cmath.phase(Ih2cplxZ3)

print(ph2IB7)