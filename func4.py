import math

def near_distance(x1, y1, x2, y2, x3, y3):
    p1 = (x1,y1)
    d1 = (x2,y2)
    d2 = (x3,y3)


    dx= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dy= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d1<d2:


        return"the nearest cab is", d1
    else:
        return"the nearest cab is", d2   
print(near_distance(1,2,3,4,5,6))

