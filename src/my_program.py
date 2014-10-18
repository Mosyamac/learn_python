from my_package import arithmetic
try:
    print arithmetic.fibonacci_iterative(0)
except Exception:
    print help(arithmetic.fibonacci_iterative)
