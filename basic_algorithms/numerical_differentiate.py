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

def Hessian(func, x, stepLength= 1e-4, decimal = 4):

    hessian = np.zeros((x.size, x.size))

    for i in range(x.size):
        for j in range(x.size):

            if i == j:

                part1 = x.copy()
                part1[i] = x[i] - stepLength
                part2 = x.copy()
                part2[i] = x[i] + stepLength

                hessian[i][j] = (func(part1) + func(part2) - 2 * func(x)) / (stepLength ** 2)

            else:

                part1 = x.copy()
                part1[i] = x[i] + stepLength
                part1[j] = x[j] + stepLength

                part2 = x.copy()
                part2[i] = x[i] - stepLength
                part2[j] = x[j] - stepLength

                part3 = x.copy()
                part3[i] = x[i] + stepLength

                part4 = x.copy()
                part4[i] = x[i] - stepLength

                part5 = x.copy()
                part5[j] = x[j] + stepLength

                part6 = x.copy()
                part6[j] = x[j] - stepLength

                hessian[i][j] = (func(part1) + func(part2) - func(part3) - func(part4)
                                 - func(part5) - func(part6) + 2 * func(x)) / (2 * stepLength ** 2)

    return hessian.round(decimal)

# =====================================

# def myFunc(x):
#
#     return x[0]*x[0]*x[0] + x[0]*x[1]
#
# x = np.array([4. , 5.], dtype= float)
#
# print(Hessian(myFunc, x))