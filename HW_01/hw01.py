# "I pledge my Honor that I have abided by the Stevens Honor System." - Maximo Ruiz

import math

def classify_triangle(a, b, c):

    try:
        a = float(a)
        b = float(b)
        c = float(c)

    except ValueError:
        return "Failed: All sides must be numeric values!"

    if a <= 0 or b <= 0 or c <= 0:
        return "Failed: All sides must be positive lengths!"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Failed: The sum of any two sides needs to be greater than the third (triangle inequality theorem)!"

    hypotenuse = max(a, b, c)

    if hypotenuse == a:
        leg1 = b
        leg2 = c

    elif hypotenuse == b:
        leg1 = a
        leg2 = c

    else:
        leg1 = a
        leg2 = b

    isRight = math.isclose(leg1**2 + leg2**2, hypotenuse**2)

    if a == b == c:
        return "Passed: This triangle is an equilateral triangle!"

    if isRight:

        if leg1 == leg2:
            return "Passed: This triangle is a right isosceles triangle!"
            
        else:
            return "Passed: This triangle is a right scalene triangle!"

    if leg1 == leg2 or leg1 == hypotenuse or leg2 == hypotenuse:
        return "Passed: This triangle is an isosceles triangle!"

    else:
        return "Passed: This triangle is a scalene triangle!"

print("Sample Outputs:")
print(classify_triangle(3, 4, 5))
print(classify_triangle(2, 2, 3))
print(classify_triangle(5, 12, 13))