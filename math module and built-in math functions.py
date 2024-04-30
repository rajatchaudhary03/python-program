import math

# Basic arithmetic operations
print("Addition:", 5 + 3)
print("Subtraction:", 10 - 2)
print("Multiplication:", 4 * 6)
print("Division (floating-point):", 12 / 3)
print("Integer division:", 12 // 3)  # Integer quotient
print("Modulo (remainder):", 14 % 5)

# Exponentiation
print("Power:", 2 ** 3)  # 2 raised to the power of 3

# Logarithms (base 10 and base e)
print("Logarithm (base 10):", math.log10(100))
print("Logarithm (base e):", math.log(math.e))

# Trigonometric functions (radians)
print("Sine (90 degrees):", math.sin(math.pi / 2))
print("Cosine (180 degrees):", math.cos(math.pi))
print("Tangent (45 degrees):", math.tan(math.pi / 4))

# Inverse trigonometric functions (radians)
print("Arcsine:", math.asin(1))
print("Arccosine:", math.acos(-1))
print("Arctangent:", math.atan(1))

# Absolute value
print("Absolute value:", abs(-5))

# Floor and ceiling functions
print("Floor:", math.floor(3.14))  # Rounds down to nearest integer
print("Ceiling:", math.ceil(3.14))  # Rounds up to nearest integer

# Factorial
print("Factorial:", math.factorial(5))  # 5! (5 factorial)

# Greatest common divisor (GCD)
print("GCD:", math.gcd(12, 18))

# Least common multiple (LCM)
print("LCM:", math.lcm(8, 12))

# Square root
print("Square root:", math.sqrt(16))

# Other mathematical constants
print("Pi:", math.pi)
print("Euler's number (e):", math.e)
