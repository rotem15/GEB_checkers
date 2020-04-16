import board

b = [[(i, j) for j in range(8)] for i in range(8)]

for row in b:
    print(row)
    
    
def direction(sqr1, sqr2):
    if sqr1[0] == sqr2[0] or sqr1[1] == sqr2[1]:
        return 's'
    if ((sqr1[0]-sqr2[0]) / (sqr1[1]-sqr2[1]))**2 == 1:
        return 'd'


def between(sqr1, sqr2, sqr3):
    if direction(sqr1, sqr2) == direction(sqr1, sqr3) and direction(sqr1, sqr2) is not None:
        print(1)
        if ((sqr3[0]-sqr1[0]) * (sqr3[0]-sqr2[0])) < 1 and ((sqr3[1]-sqr1[1]) * (sqr3[1]-sqr2[1])) < 1:
            return True
    return False

print(between(b[1][0], b[4][3], b[2][1]))
