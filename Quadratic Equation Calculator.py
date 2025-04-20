# Quadratic Equation Solver

# quadratic form pos = (-(b) + math.sqrt(math.pow(b, 2) - (4*a*c))) / 2 * a
# quadratic form neg = (-(b) - math.sqrt(math.pow(b, 2) - (4*a*c))) / 2 * a

def calculator():
    print("Quadratic equations, in standard form, take the form of ax^2 + bx + c.")
    a = float(input("a equals...? "))
    b = float(input("b equals...? "))
    c = float(input("c equals...? "))

    discriminant = (b**2 - (4*a*c))
    if discriminant < 0:
        import cmath
        firstroot = (-(b) + cmath.sqrt(discriminant)) / (2*a)
        secondroot = (-(b) - cmath.sqrt(discriminant)) / (2*a)
    else:
        import math
        firstroot = (-(b) + math.sqrt(discriminant)) / (2*a)
        secondroot = (-(b) - math.sqrt(discriminant)) / (2*a)
    print("Calculation complete! Here are the solution(s).")
    if firstroot==secondroot:
        print("x = " + str(firstroot))
    else:
        print("x = " + str(firstroot))
        print("x = " + str(secondroot))


while True:
    calculator()
    meow=input("Continue? Y/N ")
    if meow.lower() != "y":
        print("Goodbye, thanks for using my program!")
        break