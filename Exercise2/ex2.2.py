import sys
import time
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


start = time.time()
with open("./ex2.json", "r") as new_file:
    data = json.load(new_file)
results = []
for case in data:
    start_time = time.time()
    func1(case, 0, len(case) - 1)
    end_time = time.time()
    results.append(end_time - start_time)
end = time.time()

print("The Quick Sort algorithm time:", end - start, "seconds")
plt.plot(results)
plt.xlabel("n")
plt.ylabel("Execution time (seconds)")
plt.title("Quick Sort algorithm")
plt.show()
