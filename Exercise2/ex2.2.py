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

def test_quick_sort():
    with open("./ex2.json", "r") as f:
        data = json.load(f)
    results = []
    for case in data:
        start_time = time.time()
        func1(case, 0, len(case) - 1)
        end_time = time.time()
        results.append(end_time - start_time)
    return results

def plot_results(results):
    plt.plot(results)
    plt.xlabel("Test case number")
    plt.ylabel("Execution time (seconds)")
    plt.title("Quick Sort algorithm performance")
    plt.show()

if __name__ == "__main__":
    results = test_quick_sort()
    plot_results(results)
