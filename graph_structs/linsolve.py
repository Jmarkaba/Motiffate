## AUTHOR: JAH MARKABAWI
## DATE: 05/20/2019
##
## Intersection of two lines

def intersects(p1,p2,p3,p4):
    try:
        ta = ( (p3[1] - p4[1]) * (p1[0] - p3[0]) + (p4[0] - p3[0]) * (p1[1] - p3[1]) ) \
            /( (p4[0] - p3[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (p4[1] - p3[1]) )
        
        tb = ( (p1[1] - p2[1]) * (p1[0] - p3[0]) + (p2[0] - p1[0]) * (p1[1] - p3[1]) ) \
            /( (p4[0] - p3[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (p4[1] - p3[1]) )

        if(ta < 0 or ta > 1):
            return False
        elif(tb < 0 or tb > 1):
            return False
        else:
            return True
    except ZeroDivisionError:
        return False


## @Unused/Deprecated
def _get_intersection_point(c_vector, p1, p2):
    ta = c_vector[0]
    x = p1[0]+ta*(p2[0]-p1[0])
    y = p1[1]+ta*(p2[1]-p1[1])
    return x,y
