def minusGrad(func, x):

    grad = []
    sigma = 1e-4
    upsilon = 1e-1

    for i in range(len(x)):

        leftDummyX = x.copy()
        leftDummyX[i] = x[i] - sigma
        leftSubGrad = (func(x) - func(leftDummyX))/sigma

        rigthDummyX = x.copy()
        rigthDummyX[i] = x[i] + sigma
        rightSubGrad = (func(rigthDummyX) - func(x))/sigma

        if abs(leftSubGrad - rightSubGrad) > upsilon:
            raise Exception("This function cannot obtain the gradient at point x!")
        else:
            grad.append(round(-(leftSubGrad + rightSubGrad)/2, 5))

    return grad

def roundList(list, accuracy):
    newList = []
    for elem in list:
        newList.append(round(elem, accuracy))
    return newList

def isConvergent(x, newX):
    upsilon = 1e-4
    diff = []
    for i in range(len(x)):
        diff.append(x[i] - newX[i])
    relativeDiff = abs(sum(diff))/abs(sum(x))
    if relativeDiff <= upsilon:
        return True
    else:
        return False

def GoldenSectionMethod(func, x, direction, accuracy):

    LB = 0
    UB = 1
    goldenPoint = 0.618

    left = LB + (1 - goldenPoint) * (UB - LB)
    right = LB + goldenPoint * (UB - LB)

    while True:

        leftX = []
        rightX = []
        for i in range(len(x)):
            leftX.append(x[i] + direction[i] * left)
        for i in range(len(x)):
            rightX.append(x[i] + direction[i] * right)

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

def gradientDescentMethod(func, initialX, displayDetail = False):
    counter = 0
    while True:
        if displayDetail == True:
            print("ITERATION TIMES: " + str(counter))
        minusgrad = minusGrad(func, initialX)
        if displayDetail == True:
            print("GRADIENT AT POINT " + str(roundList(initialX, 4))
                  + " IS " + str(roundList(minusgrad, 4)))
        optAlpha = GoldenSectionMethod(func, initialX, minusgrad, accuracy= 1e-6)
        newX = []
        for i in range(len(initialX)):
            newX.append(initialX[i] + optAlpha*minusgrad[i])
        if displayDetail == True:
            print("THE NEXT POINT IS: " + str(roundList(newX, 4)))
            print("======================================================================")
        if isConvergent(initialX, newX):
            for i in range(len(initialX)):
                initialX[i] = round(initialX[i], 4)
            if displayDetail == True:
                print("ITERATION BREAK! THE MINIMAL VALUE OBTAINED AT POINT: "
                      + str(roundList(initialX, 4)))
                print("THE MINIMAL VALUE OF FUNCTION IS: " + str(round(myFunc(initialX), 4)))
            return initialX
        else:
            initialX = newX.copy()
            counter += 1


# ===============================================
def myFunc(x):
    return 2*(x[0]+2.3)**2 + (x[1]-1.5)**2

initialX = [8, 5]

optX = gradientDescentMethod(myFunc, initialX, displayDetail= True)


