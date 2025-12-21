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

# Функция вычисления интеграла с подынтегральным выражением в квадрате
def integral2(array, beg, end):
    l = (end - beg)/100
    sum = 0

    for i in range(99):
        sum = sum + l * array[i] ** 2
    return sum

# Функция вычисления массива данных для интеграла
def arrayInt(h1,ph1,h2,ph2):
    l = T/100
    x = 0
    array = np.zeros(100)

    for i in range(100):
        x = l * i
        array[i] = h1*math.sin(wh1*x + ph1) + h2*math.sin(wh2*x + ph2) 
    return array

uAD = arrayInt(Umh1AD, ph1UAD, Umh2AD, ph2UAD)
uCD = arrayInt(Umh1CD, ph1UCD, Umh2CD, ph2UCD)
uAB = arrayInt(Umh1AB, ph1UAB, Umh2AB, ph2UAB)
uBE = arrayInt(Umh1BE, ph1UBE, Umh2BE, ph2UBE)
uEC = arrayInt(Umh1EC, ph1UEC, Umh2EC, ph2UEC)
uL2 = arrayInt(Umh1L2, ph1UL2, Umh2L2, ph2UL2)
uC11 = arrayInt(Umh1C11, ph1UC11, Umh2C11, ph2UC11)
uC12 = arrayInt(Umh1C12, ph1UC12, Umh2C12, ph2UC12)

iB1 = arrayInt(Imh1B1, ph1IB1, Imh2B1, ph2IB1)
iB2 = arrayInt(Imh1B2, ph1IB2, Imh2B2, ph2IB2)
iB3 = arrayInt(Imh1B3, ph1IB3, Imh2B3, ph2IB3)
iB4 = arrayInt(Imh1B4, ph1IB4, Imh2B4, ph2IB4)
iB5 = arrayInt(Imh1B5, ph1IB5, Imh2B5, ph2IB5)
iB6 = arrayInt(Imh1B6, ph1IB6, Imh2B6, ph2IB6)
iB7 = arrayInt(Imh1B7, ph1IB7, Imh2B7, ph2IB7)

# Вычисление действующих значений
U_AD_RMS = math.sqrt(1./T * integral2(uAD, 0., T))
U_CD_RMS = math.sqrt(1./T * integral2(uCD, 0., T))
U_AB_RMS = math.sqrt(1./T * integral2(uAB, 0., T))
U_BE_RMS = math.sqrt(1./T * integral2(uBE, 0., T))
U_EC_RMS = math.sqrt(1./T * integral2(uEC, 0., T))
U_L2_RMS = math.sqrt(1./T * integral2(uL2, 0., T))
U_C11_RMS = math.sqrt(1./T * integral2(uC11, 0., T))
U_C12_RMS = math.sqrt(1./T * integral2(uC12, 0., T))
        
IB1_RMS = math.sqrt(1./T * integral2(iB1, 0., T))
IB2_RMS = math.sqrt(1./T * integral2(iB2, 0., T))
IB3_RMS = math.sqrt(1./T * integral2(iB3, 0., T))
IB4_RMS = math.sqrt(1./T * integral2(iB4, 0., T))
IB5_RMS = math.sqrt(1./T * integral2(iB5, 0., T))
IB6_RMS = math.sqrt(1./T * integral2(iB6, 0., T))
IB7_RMS = math.sqrt(1./T * integral2(iB7, 0., T))

# Вычисление максимальных значений
UmAD = max(uAD)
UmCD = max(uCD)
UmAB = max(uAB)
UmBE = max(uBE)
UmEC = max(uEC)
UmL2 = max(uL2)
UmC11 = max(uC11)
UmC12 = max(uC12)

ImB1 = max(iB1)
ImB2 = max(iB2)
ImB3 = max(iB3)
ImB4 = max(iB4)
ImB5 = max(iB5)
ImB6 = max(iB6)
ImB7 = max(iB7)

# Вычисление методом наложения
UcplxAD = Uh1cplx + Uh2cplx
UcplxCD = Uh1cplxCD + Uh2cplxCD
UcplxAB = Uh1cplxAB + Uh2cplxAB
UcplxBE = Uh1cplxBE + Uh2cplxBE
UcplxEC = Uh1cplxEC + Uh2cplxEC
UcplxL2 = Uh1cplxL2 + Uh2cplxL2
UcplxC11 = Uh1cplxC11 + Uh2cplxC11
UcplxC12 = Uh1cplxC12 + Uh2cplxC12
        
IcplxB1 = Ih1cplx + Ih2cplx
IcplxB2 = Ih1cplxL3 + Ih2cplxL3
IcplxB3 = Ih1cplxBE + Ih2cplxBE
IcplxB4 = Ih1cplxZ4 + Ih2cplxZ4
IcplxB5 = Ih1cplxZ2 + Ih2cplxZ2
IcplxB6 = Ih1cplxR2C2 + Ih2cplxR2C2
IcplxB7 = Ih1cplxZ3 + Ih2cplxZ3

# Вычисление углов фаз
pUAD = math.degrees(cmath.phase(UcplxAD))
pUAB = math.degrees(cmath.phase(UcplxAB))
pUBE = math.degrees(cmath.phase(UcplxBE))
pUEC = math.degrees(cmath.phase(UcplxEC))
pUCD = math.degrees(cmath.phase(UcplxCD))
pUL2 = math.degrees(cmath.phase(UcplxL2))
pUC11 = math.degrees(cmath.phase(UcplxC11))
pUC12 = math.degrees(cmath.phase(UcplxC12))
        
pIB1 = math.degrees(cmath.phase(IcplxB1))
pIB2 = math.degrees(cmath.phase(IcplxB2))
pIB3 = math.degrees(cmath.phase(IcplxB3))
pIB4 = math.degrees(cmath.phase(IcplxB4))
pIB5 = math.degrees(cmath.phase(IcplxB5))
pIB6 = math.degrees(cmath.phase(IcplxB6))
pIB7 = math.degrees(cmath.phase(IcplxB7))

# Функции для вывода
def print_row():
    print("+------------+-------------------------+------------------------+-----------+")
    print("|","Параметр","|","Максимальное значение","|","Действующее значение","|", "Угол, °","|", sep='  ')
    print("+------------+-------------------------+------------------------+-----------+")
    return

def print_value(name, max_val, rms, ang):
    print("|",f"{name:^12}","|",f"{max_val:^25.6f}","|",f"{rms:^24.6f}","|",f"{ang:^11.2f}","|", sep='')
    print("+------------+-------------------------+------------------------+-----------+")
    return

# Вывод таблицы значений
print_row()
print_value('U_AD', UmAD, U_AD_RMS, pUAD)
print_value('U_AB', UmAB, U_AB_RMS, pUAB)
print_value('U_BE', UmBE, U_BE_RMS, pUBE)
print_value('U_EC', UmEC, U_EC_RMS, pUEC)
print_value('U_CD', UmCD, U_CD_RMS, pUCD)
print_value('U_L2', UmL2, U_L2_RMS, pUL2)
print_value('U_C11', UmC11, U_C11_RMS, pUC11)
print_value('U_C12', UmC12, U_C12_RMS, pUC12)
        
print_value('I_B1', ImB1, IB1_RMS, pIB1)
print_value('I_B2', ImB2, IB2_RMS, pIB2)
print_value('I_B3', ImB3, IB3_RMS, pIB3)
print_value('I_B4', ImB4, IB4_RMS, pIB4)
print_value('I_B5', ImB5, IB5_RMS, pIB5)
print_value('I_B6', ImB6, IB6_RMS, pIB6)
print_value('I_B7', ImB7, IB7_RMS, pIB7)

# Вывод данных для построения графика в Excel
# Вывод всех напряжений
with open("voltages_python.txt", "w", encoding="utf-8") as f:
    f.write("uAD uAB uBE uEC uCD uL2 uC11 uC12\n")

    for i in range(100):
        f.write(f"{uAD[i]:.6f} {uAB[i]:.6f} {uBE[i]:.6f} {uEC[i]:.6f} {uCD[i]:.6f} {uL2[i]:.6f} {uC11[i]:.6f} {uC12[i]:.6f}\n".replace(".", ","))

# Вывод всех токов
with open("currents_python.txt", "w", encoding="utf-8") as f:
    f.write("iB1 iB2 iB3 iB4 iB5 iB6 iB7\n")

    for i in range(100):
        f.write(f"{iB1[i]:.6f} {iB2[i]:.6f} {iB3[i]:.6f} {iB4[i]:.6f} {iB5[i]:.6f} {iB6[i]:.6f} {iB7[i]:.6f}\n".replace(".", ","))