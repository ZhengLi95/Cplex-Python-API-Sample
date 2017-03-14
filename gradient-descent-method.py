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

def gradientDescentMethod(func, initialX, displayDetail = False):
    counter = 0
    while True:
        if displayDetail == True:
            print("ITERATION TIMES: " + str(counter))
        grad = minusGrad(func, initialX)
        if displayDetail == True:
            print("GRADIENT AT POINT " + str(roundList(initialX, 4))
                  + " IS " + str(roundList(grad, 4)))
        alpha = 0
        fmin = float("inf")
        recorder = 0
        while alpha <= 1:
            bufferX = []
            for i in range(len(initialX)):
                bufferX.append(initialX[i] + alpha*grad[0])
            f = func(bufferX)
            alpha += 1e-4
            if f <= fmin:
                fmin = f
                recorder = alpha
        newX = []
        for i in range(len(initialX)):
            newX.append(initialX[i] + recorder*grad[0])
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
    return 2*(x[0]-3)**2 + (x[1]-1.5)**2

initialX = [8, 5]

optX = gradientDescentMethod(myFunc, initialX, displayDetail= True)


