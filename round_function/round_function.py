# Why Floating-Point Errors Occur.
# print(0.1 + 0.2)
# Output: 0.30000000000000004 so floating point error

# A round-off error occurs when a computer stores an approximate value
# instead of the exact value due to limitations in representing floating-point
# numbers.

# x = 0.1 + 0.2
# print(x)
# Output:0.30000000000000004
# Expected:0.3
# Difference:0.00000000000000004 This is round-off error.

# OVERFLOWERROR -  number becomes too large for Python's floating-point storage capacity
# print(3.0 ** 1024)
# Output: OverflowError

#Round function -> The round() function is used to reduce decimal places and improve output readability.
# Syntax: round(number, decimal_places)

x = 2.451
print(round(x,2))


