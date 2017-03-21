import numpy as np
import basic_algorithms as ba

def guardedNewtionMethod(func, initialX, displayDetail= False, decimal= 3, accuracy= 1e-6):

    counter = 0

    while True:

        if displayDetail == True:
            print("ITERATION TIMES: " + str(counter))

        gradient = ba.numerical_differentiate.Grad(func, initialX)
        hessianMatrix = ba.numerical_differentiate.Hessian(func, initialX)

        if not ba.numerical_differentiate.isPositiveDenifite(hessianMatrix):
            raise ValueError("This problem is not convex, cannot use this method to solve!")

        invHessianMatrix = np.linalg.inv(hessianMatrix)

        if displayDetail == True:
            print("INV-HESSIAN-MATRIX AT POINT " + str(initialX.round(decimal))
                  + " IS: \n" + str(invHessianMatrix.round(decimal)))

        if ba.check_convergence.isNewtonConvergent(gradient, invHessianMatrix):
            if displayDetail == True:
                print("ITERATION BREAK! THE MINIMAL VALUE OBTAINED AT POINT: "
                      + str(initialX.round(decimal)))
                print("THE MINIMAL VALUE OF FUNCTION IS: " + str(round(func(initialX), decimal)))
            return initialX

        newtonDirection =  - invHessianMatrix.dot(gradient)
        optAlpha = ba.linear_search.GoldenSectionMethod(func, initialX, newtonDirection, accuracy)
        newX = initialX + optAlpha * newtonDirection

        if displayDetail == True:
            print("THE NEXT POINT IS: " + str(newX.round(decimal)))
            print("======================================================================")

        initialX = newX.copy()
        counter += 1

# ===============================================

def myFunc(x):
    return 2*(x[0]*+2.3)**2 + (x[1]-1.5)**2

initialX = np.array([8., 5.], dtype= float)

optX = guardedNewtionMethod(myFunc, initialX, displayDetail= True)
