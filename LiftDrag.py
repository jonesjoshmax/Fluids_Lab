import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

np.set_printoptions(suppress=True)


d_pull = np.array(
    ['Test01.dat', 'Test02.dat', 'Test03.dat', 'Test04.dat', 'Test05.dat', 'Test06.dat',
     'Test07.dat', 'Test08.dat', 'Test09.dat', 'Test10.dat', 'Test11.dat', 'Test12.dat', 'Test13.dat']
)
mirror = np.zeros([np.size(d_pull), 18])
angles = np.array(
    [0, 4, 6, 8, 10, 12, 14]
)
mirror_a = np.zeros([2, np.size(angles)])
xpco1 = np.array(
    [0, .035, .088, .14, .193, .246,
     .298, .351, .404, .456, .509, .562,
     .614, .667, .72, .772, .825, .878]
)
ypco1 = np.array(
    [0, .0304, .0446, .0524, .057, .0593,
     .06, .0595, .0579, .0555, .0524, .0487,
     .0444, .0398, .0347, .0292, .0234, .0172]
)


def press_coeff():
    zindex = 0
    for r in d_pull:
        unpack = np.loadtxt(r, unpack=True)
        z0 = 0
        z1 = 1
        for s in range(18):
            ps = unpack[2][z1]
            pd = unpack[1][z1]
            print(ps)
            print(pd)
            pc = ps / pd
            mirror[zindex, z0] = pc
            z0 = z0 + 1
            z1 = z1 + 1
        zindex = zindex + 1


def summations():
    press_coeff()
    z0 = 0
    for r in range(7):
        cpu = np.empty(17)
        cpl = np.empty(17)
        if r == 0:
            cpu = mirror[0]
            cpl = mirror[0]
        elif r > 0:
            if r == 1:
                cpu = mirror[1]
                cpl = mirror[7]
            if r == 2:
                cpu = mirror[2]
                cpl = mirror[8]
            if r == 3:
                cpu = mirror[3]
                cpl = mirror[9]
            if r == 4:
                cpu = mirror[4]
                cpl = mirror[10]
            if r == 5:
                cpu = mirror[5]
                cpl = mirror[11]
            if r == 6:
                cpu = mirror[6]
                cpl = mirror[12]
        z = 0
        a = 0
        b = 0
        for t in range(17):
            dx = xpco1[z+1] - xpco1[z]
            dy = ypco1[z+1] - ypco1[z]
            pu = cpu[z+1] + cpu[z]
            a = (.5 * pu * dx) + a
            b = (.5 * pu * dy) + b
            z = z + 1
        cnu = a
        ccu = b
        z = 0
        a = 0
        b = 0
        for t in range(17):
            dx = xpco1[z+1] - xpco1[z]
            dy = -1 * (ypco1[z+1] - ypco1[z])
            pu = cpl[z+1] + cpl[z]
            a = (.5 * pu * dx) + a
            b = (.5 * pu * dy) + b
            z = z + 1
        cnl = a
        ccl = b
        cn = cnl - cnu
        cc = ccu - ccl
        ang = np.deg2rad(r)
        cl = (cn * np.cos(ang)) - (cc * np.sin(ang))
        cd = (cc * np.cos(ang)) + (cn * np.sin(ang))
        mirror_a[0][z0] = cl
        mirror_a[1][z0] = cd
        z0 = z0 + 1
    print(mirror_a)


def plot():
    summations()
    plt.plot(mirror_a[1], mirror_a[0], color='black', marker='o')
    plt.grid()
    plt.title('Lift Coefficient vs Drag Coefficient')
    plt.show()
    plt.plot(angles, mirror_a[0], color='blue', marker='^')
    plt.grid()
    plt.title('Lift Coefficient vs Angle')
    plt.show()
    plt.plot(angles, mirror_a[1], color='red', marker='s')
    plt.grid()
    plt.title('Drag Coefficient vs Angle')
    plt.show()


plot()
