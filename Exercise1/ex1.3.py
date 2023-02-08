# Implement a version of the code above that uses memoization to improve performance. Provide this as ex1.3.py. (2 pts)

cache = {}
def func(n):
    if n == 0 or n == 1:
        return n        
    if n in cache:
        return cache[n]
    result = func(n-1) + func(n-2)
    cache[n] = result
    return result

