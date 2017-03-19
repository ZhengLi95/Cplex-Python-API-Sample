import numpy as np

def isConvergent(x, newX, accuracy= 1e-6):

    difference = np.linalg.norm(x - newX)/np.linalg.norm(x)

    if difference <= accuracy:
        return True
    else:
        return False