import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

np.set_printoptions(suppress=True)

# Global Vars
cn1 = np.empty(18)
cn1 = cn1.astype('float64')
cn2 = np.empty(18)
cn2 = cn1.astype('float64')
cnx1 = np.empty(18)
cnx1 = cnx1.astype('float64')
cny1 = np.empty(18)
cny1 = cny1.astype('float64')
cnx2 = np.empty(18)
cnx2 = cnx2.astype('float64')
cny2 = np.empty(18)
cny2 = cny2.astype('float64')

xco = np.array(
    [0, .210, .526, .842, 1.158, 1.474,
     1.790, 2.106, 2.422, 2.738, 3.054, 3.370,
     3.686, 4.002, 4.318, 4.634, 4.950, 5.265,
     6.054]
)
xco1 = np.array(
    [0, .210, .526, .842, 1.158, 1.474,
     1.790, 2.106, 2.422, 2.738, 3.054, 3.370,
     3.686, 4.002, 4.318, 4.634, 4.950, 5.265]
)
xpco = np.array(
    [0, .035, .088, .14, .193, .246,
     .298, .351, .404, .456, .509, .562,
     .614, .667, .72, .772, .825, .878,
     1]
)
xpco1 = np.array(
    [0, .035, .088, .14, .193, .246,
     .298, .351, .404, .456, .509, .562,
     .614, .667, .72, .772, .825, .878]
)
xpco2 = np.array(
    [.035, .088, .14, .193, .246, .298,
     .351, .404, .456, .509, .562, .614,
     .667, .72, .772, .825, .878, 1]
)
xpco3 = np.array(
    [0, .035, .088, .14, .193, .246,
     .298, .351, .404, .456, .509, .562,
     .614, .667, .72, .772, .825, .878,
     .825, .772, .72,  .667, .614, .562,
     .509, .456, .404, .351, .298, .246,
     .193, .14,  .088, .035, 0, 0]
)
ypco1 = np.array(
    [0, .0305, .0446, .0524, .057, .0593,
     .06, .0595, .0579, .0555, .0524, .0487,
     .0444, .0398, .0347, .0292, .0234, .0172]
)
ypco3 = np.array(
    [0, .0305, .0446, .0524, .057, .0593,
     .06, .0595, .0579, .0555, .0524, .0487,
     .0444, .0398, .0347, .0292, .0234, .0172,
     -.0234, -.0292, -.0347, -.0398, -.0444, -.0487,
     -.0524, -.0555, -.0579, -.0595, -.06, -.0593,
     -.057,  -.0524, -.0446, -.0305, 0, 0]
)
ypco2 = np.array(
    [.0305, .0446, .0524, .057, .0593, .06,
     .0595, .0579, .0555, .0524, .0487, .0444,
     .0398, .0347, .0292, .0234, .0172, 0]
)
xco2 = np.array(
    [.210, .526, .842, 1.158, 1.474, 1.790,
     2.106, 2.422, 2.738, 3.054, 3.370, 3.686,
     4.002, 4.318, 4.634, 4.950, 5.265, 6.054]
)
yco1 = np.array(
    [0, .1826, .2676, .3145, .3417, .3558,
     .3601, .3568, .3473, .3329, .3142, .2919,
     .2666, .2386, .2082, .1755, .1405, .1035]
)
yco2 = np.array(
    [.1826, .2676, .3145, .3417, .3558, .3601,
     .3568, .3473, .3329, .3142, .2919, .2666,
     .2386, .2082, .1755, .1405, .1035, 0]
)
zco = np.zeros(18)
# Angle 1 is used for top half of graph, Angle 2 is used for bottom half of graph
angle1 = np.array(
    [3.14159265, 1.93944989, 1.76047655, 1.68268814, 1.63377077, 1.5986047,
     1.57165823, 1.55028219, 1.53296932, 1.518748, 1.50692872, 1.49698373,
     1.48848427, 1.48106533, 1.47440464, 1.46820969, 1.46220926, 1.45616746]
)
angle2 = np.array(
    [-1.93944989, -1.76047655, -1.68268814, -1.63377077, -1.5986047, -1.57165823,
     -1.55028219, -1.53296932, -1.518748, -1.50692872, -1.49698373, -1.48848427,
     -1.48106533, -1.47440464, -1.46820969, -1.46220926, -1.45616746, 3.14159265]
)
wing1 = 6 * (.12 / .20) * ((.2969 * ((xco / 6) ** .5)) - (.126 * (xco / 6)) - (.3516 * ((xco / 6) ** 2)) +
                           .2843 * ((xco / 6) ** 3) - (.1015 * ((xco / 6) ** 4)))
wing2 = -6 * (.12 / .20) * ((.2969 * ((xco / 6) ** .5)) - (.126 * (xco / 6)) - (.3516 * ((xco / 6) ** 2)) +
                            .2843 * ((xco / 6) ** 3) - (.1015 * ((xco / 6) ** 4)))
wingpco = (.12 / .20) * ((.2969 * (xpco ** .5)) - (.126 * xpco) - (.3516 * (xpco ** 2)) + (.2843 * (xpco ** 3)) - (.1015 * (xpco ** 4)))
angle_set = np.array(
    [0, 4, 6, 8, 10, 12, 14]
)


def angle_input():
    lst1 = ''
    lst2 = ''
    title = ''
    print('Data Available to Choose From:')
    print('0, 4, 6, 8, 10, 12, 14')
    while True:
        a = input('Angle of Attack: ')
        a = float(a)
        if a == 0:
            lst1 = 'Test01.dat'
            lst2 = 'Test01.dat'
        elif a == 4:
            lst1 = 'Test02.dat'
            lst2 = 'Test08.dat'
        elif a == 6:
            lst1 = 'Test03.dat'
            lst2 = 'Test09.dat'
        elif a == 8:
            lst1 = 'Test04.dat'
            lst2 = 'Test10.dat'
        elif a == 10:
            lst1 = 'Test05.dat'
            lst2 = 'Test11.dat'
        elif a == 12:
            lst1 = 'Test06.dat'
            lst2 = 'Test12.dat'
        elif a == 14:
            lst1 = 'Test07.dat'
            lst2 = 'Test13.dat'
        else:
            print('Invalid Input')
            continue
        angle_input.lst1 = lst1
        angle_input.lst2 = lst2
        angle_input.title = a
        return


angle_input()


# angle1 and angle2 values obtained from this code
# Point Location -> Slope -> Angle
def angles(lst):
    slope_calcs = np.empty(18)
    z = 0
    for r in lst:
        a = 3.6 * ((.0606 * (r ** (-.5))) - .021 - (.01953 * r) + (.00394 * (r ** 2)) - (.0003 * (r ** 3)))
        np.put(slope_calcs, z, a)
        z = z + 1
    z = 0
    slope_invert = np.empty(18)
    for r in slope_calcs:
        a = -1 / r
        np.put(slope_invert, z, a)
        z = z + 1
    z = 0
    slope_arctan = np.empty(18)
    for r in slope_invert:
        a = np.rad2deg(np.arctan(r))
        np.put(slope_arctan, z, a)
        z = z + 1
    z = 0
    slope_corrected = np.empty(18)
    for r in slope_arctan:
        if r <= 0:
            r = r + 180
        r = np.deg2rad(r)
        np.put(slope_corrected, z, r)
        z = z + 1


def coeff1(lst):
    data = np.loadtxt(lst, unpack=True)
    z = 1
    zk = 0
    for r in cn1:
        x = data[1][z]
        y = data[2][z]
        a = y / x
        np.put(cn1, zk, a)
        z = z + 1
        zk = zk + 1


def coeff2(lst):
    data = np.loadtxt(lst, unpack=True)
    z = 2
    zk = 0
    for r in cn2:
        if z <= 18:
            x = data[1][z]
            y = data[2][z]
            a = y / x
            np.put(cn2, zk, a)
            z = z + 1
            zk = zk + 1
        else:
            a = -.1
            np.put(cn2, zk, a)


def get_components(lst1, lst2):
    coeff1(lst1)
    z = 0
    for r in cn1:
        angle = angle1[z]
        a = -r * np.cos(angle)
        np.put(cnx1, z, a)
        a = -r * np.sin(angle)
        np.put(cny1, z, a)
        z = z + 1
    coeff2(lst2)
    z = 0
    for r in cn2:
        angle = angle2[z]
        a = -r * np.cos(angle)
        np.put(cnx2, z, a)
        a = -r * np.sin(angle)
        np.put(cny2, z, a)
        z = z + 1


def plot1():
    lst1 = angle_input.lst1
    lst2 = angle_input.lst2
    title = angle_input.title
    title = repr(title)
    get_components(lst1, lst2)
    plt.rcParams.update({'font.size': 26})
    plt.figure(dpi=200)
    plt.plot(xpco, wingpco, color='black')
    plt.plot(xpco, -wingpco, color='black')
    plt.quiver(xpco1, ypco1, cnx1, cny1, angles='xy', scale_units='xy', scale=1, color='blue')
    plt.quiver(xpco2, -1 * ypco2, cnx2, cny2, angles='xy', scale_units='xy', scale=1, color='red')
    plt.grid()
    plt.xlim(-1.15, 1.05)
    plt.ylim(-.125, 3)
    plt.title(title + ' Degree AOA Normal Pressure Coefficients')
    plt.show()


def plot2():
    lst1 = angle_input.lst1
    lst2 = angle_input.lst2
    title = angle_input.title
    title = repr(title)
    get_components(lst1, lst2)
    plt.plot(xco, wing1, color='black')
    plt.plot(-1 * xco, wing2, color='black')
    plt.quiver(xco1, yco1, cnx1, zco, angles='xy', scale_units='xy', scale=1, color='red')
    plt.quiver(xco2, -1 * yco2, cnx2, zco, angles='xy', scale_units='xy', scale=1, color='blue')
    plt.grid()
    plt.xlim(-1.5, 6.5)
    plt.ylim(-2, 2)
    plt.title(title + ' Degree AOA, Pressure Coefficient vs Chord (X)')
    plt.show()


def plot3():
    lst1 = angle_input.lst1
    lst2 = angle_input.lst2
    title = angle_input.title
    title = repr(title)
    get_components(lst1, lst2)
    plt.plot(xco, wing1, color='black')
    plt.plot(xco, wing2, color='black')
    plt.quiver(xco1, yco1, zco, cny1, angles='xy', scale_units='xy', scale=1, color='red')
    plt.quiver(xco2, -1 * yco2, zco, cny2, angles='xy', scale_units='xy', scale=1, color='blue')
    plt.grid()
    plt.xlim(-1.5, 6.5)
    plt.ylim(-2, 2)
    plt.title(title + ' Degree AOA, Pressure Coefficient vs Chord (Y)')
    plt.show()


def plot4():
    coeffs = np.empty(36)
    lst1 = angle_input.lst1
    lst2 = angle_input.lst2
    title = angle_input.title
    title = repr(title)
    coeff1(lst1)
    coeff2(lst2)
    z = 0
    z0 = 0
    for r in range(18):
        coeffs[z] = cn1[z0]
        z = z + 1
        z0 = z0 + 1
    z0 = 17
    for r in range(18):
        coeffs[z] = cn2[z0]
        if z0 == 0:
            coeffs[z] = cn1[0]
        z = z + 1
        z0 = z0 - 1
    plt.rcParams.update({'font.size': 14})
    plt.figure(dpi=100)
    plt.grid()
    plt.title(title + ' Degree AOA, Pressure Coefficient vs Percent Chord (X)')
    plt.xlabel('x/c')
    plt.ylabel('Pressure Coefficient')
#    plt.xlim(-.1, 1.1)
#    plt.ylim(-3.5, .6)
    plt.plot(xpco, wingpco, color='black')
    plt.plot(xpco, -wingpco, color='black')
    plt.plot(xpco3, coeffs, color='orange')
    plt.show()
    plt.rcParams.update({'font.size': 14})
    plt.figure(dpi=100)
    plt.grid()
    plt.title(title + ' Degree AOA, Pressure Coefficient vs Percent Chord (Y)')
    plt.xlabel('Pressure Coefficient')
    plt.ylabel('y/c')
#    plt.xlim(-3.5, 1.1)
#    plt.ylim(-1, 1)
    plt.plot(xpco, wingpco, color='black')
    plt.plot(xpco, -wingpco, color='black')
    plt.plot(coeffs, ypco3, color='green')
    plt.show()

#    print(cnu)
#    print(cnl)
#    print(cn)
#    print(ccu)
#    print(ccl)
#    print(cc)
#    print(angle)


def reynolds():
    row = 1.225
    v = 29.5656
    lgth = .1524
    visc = 18.34
    re = (row * v * lgth) / visc
    print(re)


# 00 = Test01/Test01 04 = Test02/Test08 06 = Test03/Test09 08 =Test04/Test110
# 10 = Test05/Test11 12 = Test06/Test12 14 = Test07/Test13
# plot1()
# plot2()
# plot3()
plot4()
# lift_drag()
