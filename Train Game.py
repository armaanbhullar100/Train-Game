def common_num(l1, l2):
    for x in l1:
        for y in l2:
            if x == y:
                return True
                 
    return False

def find10(digits):
    perm2 = []
    perm3 = []
    perm4 = []

    for idx, x in enumerate(digits):
        for idy, y in enumerate(digits):
            if (idx != idy):
                perm2.append([str(x) + " + " + str(y), x + y, [idx, idy]])
                perm2.append([str(x) + " - " + str(y), x - y, [idx, idy]])
                perm2.append([str(x) + " * " + str(y), x * y, [idx, idy]])
                if (y != 0):
                    perm2.append([str(x) + " / " + str(y), x / y, [idx, idy]])
                
    for p in perm2:
        for idx, x in enumerate(digits):
            if (idx not in p[2]):
                perm3.append([p[0] + ' + ' + str(x), p[1] + x, p[2] + [idx]])
                perm3.append([p[0] + ' - ' + str(x), p[1] - x, p[2] + [idx]])
                perm3.append([p[0] + ' * ' + str(x), p[1] * x, p[2] + [idx]])
                if (x != 0):
                    perm3.append([p[0] + ' / ' + str(x), p[1] / x, p[2] + [idx]])
                          
    for p in perm3:
        for idx, x in enumerate(digits):
            if (idx not in p[2]):
                perm4.append([p[0] + ' + ' + str(x), p[1] + x, p[2] + [idx]])
                perm4.append([p[0] + ' - ' + str(x), p[1] - x, p[2] + [idx]])
                perm4.append([p[0] + ' * ' + str(x), p[1] * x, p[2] + [idx]])
                if (x != 0):
                    perm4.append([p[0] + ' / ' + str(x), p[1] / x, p[2] + [idx]])

    for p1 in perm2:
        for p2 in perm2:
            if (common_num(p1[2], p2[2]) == False):
                perm4.append([p1[0] + ' + ' + p2[0], p1[1] + p2[1], p1[2] + p2[2]])
                perm4.append([p1[0] + ' - ' + p2[0], p1[1] - p2[1], p1[2] + p2[2]])
                perm4.append([p1[0] + ' * ' + p2[0], p1[1] * p2[1], p1[2] + p2[2]])
                if (p2[1] != 0):
                    perm4.append([p1[0] + ' / ' + p2[0], p1[1] / p2[1], p1[2] + p2[2]])

    for p in perm4:
        if (p[1] == 10):
            print(p[0] + " = " + str(p[1]))

if __name__ == '__main__':
    num = 9553
    digits = [int(x) for x in str(num)]
    find10(digits)