def GoldenSectionMethod(func, x, direction, accuracy= 1e-6):

    LB = 0
    UB = 1
    goldenPoint = 0.618

    left = LB + (1 - goldenPoint) * (UB - LB)
    right = LB + goldenPoint * (UB - LB)

    while True:

        val_left = func(x + direction * left)
        val_right = func(x + direction * right)

        if val_left <= val_right:
            UB = right
        else:
            LB = left

        if abs(LB - UB) < accuracy:
            opt_theta = (right + left)/2
            return opt_theta
        else:
            if val_left <= val_right:
                right = left
                left = LB + (1 - goldenPoint) * (UB - LB)
            else:
                left = right
                right = LB + goldenPoint * (UB - LB)