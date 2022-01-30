# Mandelbrot.py

from math import log, log2

MAX_ITER = 80 # Maximum number of times to iterate in computing set

def mandelbrot(c):
    """
    Returns the number of iterations needed for a start point to reach a 
    modulus greater than 2 under the Mandelbrot equations z_(n+1) = z_n^2 + c. 
    This is known as the escape time algorithm.

    Args:
       c (complex): Point in complex space to test for membership in
          Mandelbrot set.
    
    Returns:
       int: number of iterations to reach modulus greater than 2, or else
          MAX_ITER if more iterations would be needed
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c 
        n += 1
    return n

def mandelbrot_smooth(c):
    """
    Returns the fractional escape count or normalized iteration count of an 
    initial complex number c

    Args:
       c (complex): Point in complex space to test for membership in
          Mandelbrot set.
    
    Returns:
       int: number of iterations to reach modulus greater than 2, or else
          MAX_ITER if more iterations would be needed
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c 
        n += 1

    if n == MAX_ITER: 
        return MAX_ITER
    
    return n + 1 - log(log2(abs(z)))

if __name__ == "__main__":
    for x in range(-10, 10, 5):
        for y in range(-10, 10, 5):
            z = complex(x / 10, y / 10)
            print(f"z = {z}; Escape time = {mandelbrot(z)}")