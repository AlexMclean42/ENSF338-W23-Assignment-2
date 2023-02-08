import time
import matplotlib.pyplot as plt

def original_func(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)

cache = {}
def func(n):
    if n == 0 or n == 1:
        return n        
    if n in cache:
        return cache[n]
    result = func(n-1) + func(n-2)
    cache[n] = result
    return result


start = time.time()
rez_original_func = []
time_original_func = []
for i in range(1, 36):
    t1 = time.time()
    rez_original_func.append(original_func(i))
    t2 = time.time()
    time_original_func.append(t2-t1)
end = time.time()
print("The original code time:", end - start, "seconds")

start = time.time()
rez_func = []
time_func = []
for i in range(1, 36):
    t1 = time.time()
    rez_func.append(func(i))
    t2 = time.time()
    time_func.append(t2-t1)
end = time.time()
print("The improved version time:", end - start, "seconds")

plt.plot(time_original_func, color = "red", label = "original_func" )
plt.plot(time_func, color = "green", label = "improved_func")
plt.title("Time of Original vs Improved Version of Fibonacci Functions")
plt.xlabel("Fibonacci Numbers (1 - 35)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
