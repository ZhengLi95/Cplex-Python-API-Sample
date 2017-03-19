import numpy as np

def Grad(func, x, stepLength= 1e-4):

    grad = np.zeros(x.size)

    for i in range(x.size):

        leftDummyX = x.copy()
        leftDummyX[i] = x[i] - stepLength
        rigthDummyX = x.copy()
        rigthDummyX[i] = x[i] + stepLength

        grad[i] = (func(rigthDummyX) - func(leftDummyX)) / (2 * stepLength)

    return grad

def Hessian(func, x, stepLength= 1e-4):

    hessian = np.zeros((x.size, x.size))

    for i in range(x.size):
        for j in range(x.size):
            leftDummyX = x.copy()
            leftDummyX[i] = x[i] - stepLength
            rigthDummyX = x.copy()
            rigthDummyX[i] = x[i] + stepLength

def Test2(func, x, stepLength= 1e-3):

    leftDummyX = x.copy()
    leftDummyX[0] = x[0] - stepLength
    rigthDummyX = x.copy()
    rigthDummyX[0] = x[0] + stepLength

    print(leftDummyX, rigthDummyX, x)
    val = (func(leftDummyX) + func(rigthDummyX) - 2 * func(x))/(stepLength**2)
    print(func(leftDummyX) + func(rigthDummyX) - 2 * func(x))
    return val

def Test(func, x , stepLength= 1e-4):

    subx1 = x.copy()
    subx1[0] = x[0] + stepLength
    subx1[1] = x[1] + stepLength

    subx2 = x.copy()
    subx2[0] = x[0] - stepLength
    subx2[1] = x[1] - stepLength

    subx3 = x.copy()
    subx3[0] = x[0] + stepLength

    subx4 = x.copy()
    subx4[0] = x[0] - stepLength

    subx5 = x.copy()
    subx5[1] = x[1] + stepLength

    subx6 = x.copy()
    subx6[1] = x[1] - stepLength

    val = (func(subx1) + func(subx2) - func(subx3) - func(subx4) - func(subx5) - func(subx6) + 2*func(x))/(2*stepLength**2)

    return val

def myFunc(x):

    return x[0] + x[0]*x[1]

x = np.array([2., 5.])

print(Test(myFunc, x))