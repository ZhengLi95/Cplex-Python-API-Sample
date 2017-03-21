import numpy as np
import basic_algorithms as ba

def gradientDescentMethod(func, initialX, displayDetail= False, decimal= 3, accuracy= 1e-6):

    counter = 0

    while True:

        if displayDetail == True:
            print("ITERATION TIMES: " + str(counter))

        negativeGrad = - ba.numerical_differentiate.Grad(func, initialX)

        if displayDetail == True:
            print("NEG-GRADIENT AT POINT " + str(initialX.round(decimal))
                  + " IS " + str(negativeGrad.round(decimal)))

        optAlpha = ba.linear_search.GoldenSectionMethod(func, initialX, negativeGrad, accuracy)
        newX = initialX + optAlpha * negativeGrad

        if displayDetail == True:
            print("THE NEXT POINT IS: " + str(newX.round(decimal)))
            print("======================================================================")

        if ba.check_convergence.isConvergent(initialX, newX, accuracy= 1e-6):
            if displayDetail == True:
                print("ITERATION BREAK! THE MINIMAL VALUE OBTAINED AT POINT: "
                      + str(initialX.round(decimal)))
                print("THE MINIMAL VALUE OF FUNCTION IS: " + str(round(func(initialX), decimal)))
            return initialX
        else:
            initialX = newX.copy()
            counter += 1


# ===============================================

def myFunc(x):
    return 2*(x[0]+2.3)**2 + (x[1]-1.5)**2

initialX = np.array([8., 5.], dtype= float)

optX = gradientDescentMethod(myFunc, initialX, displayDetail= True)


