import time

cache = {}
def func(n):
    if n == 0 or n == 1:
        return n        
    if n in cache:
        return cache[n]
    result = func(n-1) + func(n-2)
    cache[n] = result
    return result



# start = time.time()
# result1 = func(40)
# end = time.time()
# print("First call took: ", end - start, "seconds")

# start = time.time()
# result2 = func(40)
# end = time.time()
# print("Second call took: ", end - start, "seconds")

# print("Both results are equal: ", result1 == result2)
