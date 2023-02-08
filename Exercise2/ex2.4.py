import sys
import time
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

start = time.time()
with open("./ex2.json", "r") as new_file:
    data = json.load(new_file)
results_merge = []
for case in data:
    start_time = time.time()
    mergeSort(case)
    end_time = time.time()
    results_merge.append(end_time - start_time)
end = time.time()

print("The Merge Sort algorithm time:", end - start, "seconds")
plt.plot(results_merge, label="Merge Sort")
plt.xlabel("n")
plt.ylabel("Execution time (seconds)")
plt.title("Merge Sort algorithm")
plt.legend()
plt.show()
