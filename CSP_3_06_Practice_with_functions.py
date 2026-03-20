# Heron's Formula
import math

# returns the square root of the number n
def root(n):
    return math.sqrt(n)

# Takes in the 3 side lengths of a triangle as arguments and returns half of
# the perimeter of a triangle.
def semiPerimeter(a, b, c):
    return (a + b + c) / 2

# multiply the first argument by the difference between itself and each individual argument
def multiplyDifferences(s, a, b, c):
    return s * (s - a) * (s - b) * (s - c)

# Given the 3 sides of a triangle return the area using Heron's formula
def herons(a, b, c):
    s = semiPerimeter(a, b, c)
    value = multiplyDifferences(s, a, b, c)
    return root(value)


# Quadratic Equation

# takes in a number as an argument and returns that number multiplied by 2
def denominator(a):
    return 2 * a

# multiply first argument by -1, then return (-b + c, -b - c)
def plusMinus(b, c):
    b = -1 * b
    return (b + c, b - c)

# calculate b^2 - 4ac
def mainCalc(a, b, c):
    return (b ** 2) - (4 * a * c)

# quadratic formula function
def quadratic(a, b, c):
    discriminant = mainCalc(a, b, c)
    sqrt_val = root(discriminant)
    
    num1, num2 = plusMinus(b, sqrt_val)
    denom = denominator(a)
    
    return (num1 / denom, num2 / denom)
