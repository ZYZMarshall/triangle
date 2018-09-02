def classify_triangle(a, b, c):
    '''Classify Triangles combinded by sides a,b,c'''

    valid_a = isinstance(a, (float, int))
    valid_b = isinstance(b, (float, int))
    valid_c = isinstance(c, (float, int))
    if not (valid_a and valid_b and valid_c):
        return 'InvalidInput'


    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'


    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        return 'Not a Triangle'

    triangle_type = ""
    if a*a +b*b == c*c:
        triangle_type = "Right triangle"
    elif a == b and b == a and c == a:
        triangle_type = 'Equilateral triangle'
    elif (a != b) and  (b != c) and (a != c):
        triangle_type = 'Scalene triangle'
    else:
        triangle_type = 'Isoceles triangle'
    return triangle_type