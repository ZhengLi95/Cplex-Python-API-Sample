import numpy as np

def Grad(func, x, stepLength= 1e-4):

    grad = np.zeros(x.size)

    for i in range(x.size):

        leftDummyX = x.copy()
        leftDummyX[i] = x[i] - stepLength
        rigthDummyX = x.copy()
        rigthDummyX[i] = x[i] + stepLength
        SubGrad = (func(rigthDummyX) - func(leftDummyX)) / (2 * stepLength)

        grad[i] = SubGrad

    return grad

def isConvergent(x, newX, accuracy= 1e-4):
    difference = np.linalg.norm(x - newX)/np.linalg.norm(x)
    if difference <= accuracy:
        return True
    else:
        return False

def GoldenSectionMethod(func, x, direction, accuracy= 1e-6):

    LB = 0
    UB = 1
    goldenPoint = 0.618

    left = LB + (1 - goldenPoint) * (UB - LB)
    right = LB + goldenPoint * (UB - LB)

    while True:

        leftX = x + direction * left
        rightX = x + direction * right
        val_left = func(leftX)
        val_right = func(rightX)

        if val_left <= val_right:
            UB = right
        else:
            LB = left

        if abs(LB - UB) < accuracy:
            opt_theta = (right + left)/2.0
            return opt_theta
        else:
            if val_left <= val_right:
                right = left
                left = LB + (1 - goldenPoint) * (UB - LB)
            else:
                left = right
                right = LB + goldenPoint*(UB - LB)

def gradientDescentMethod(func, initialX, displayDetail= False, decimal= 3, accuracy= 1e-6):

    counter = 0

    while True:

        if displayDetail == True:
            print("ITERATION TIMES: " + str(counter))

        negativeGrad = - Grad(func, initialX)

        if displayDetail == True:
            print("NEG-GRADIENT AT POINT " + str(initialX.round(decimal))
                  + " IS " + str(negativeGrad.round(decimal)))

        optAlpha = GoldenSectionMethod(func, initialX, negativeGrad, accuracy)
        newX = initialX + optAlpha * negativeGrad

        if displayDetail == True:
            print("THE NEXT POINT IS: " + str(newX.round(decimal)))
            print("======================================================================")

        if isConvergent(initialX, newX):
            if displayDetail == True:
                print("ITERATION BREAK! THE MINIMAL VALUE OBTAINED AT POINT: "
                      + str(initialX.round(decimal)))
                print("THE MINIMAL VALUE OF FUNCTION IS: " + str(round(func(initialX), 4)))
            return initialX
        else:
            initialX = newX.copy()
            counter += 1


# ===============================================

def myFunc(x):
    return 2*(x[0]+2.3)**2 + (x[1]-1.5)**2

initialX = np.array([8., 5.])

optX = gradientDescentMethod(myFunc, initialX, displayDetail= True)


