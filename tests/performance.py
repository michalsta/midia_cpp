import midia_cpp

import numpy as np
import timeit

array_size = 100000000
arr = np.random.rand(array_size)


# Measure the execution time of numpy.argsort
def run_sort():
    sorted_indices = np.argsort(arr)


def c_sort():
    res = np.empty(len(arr), dtype=np.uint64)
    sorted_indices_c = midia_cpp.argsort(res, arr, len(arr))


# Time the execution of numpy.argsort
execution_time = None
# execution_time = timeit.timeit(run_sort, number=3)  # You can adjust the number of iterations
print(
    f"Execution time for numpy.argsort with an array of size {array_size}: {execution_time} seconds"
)
execution_time2 = timeit.timeit(
    c_sort, number=3
)  # You can adjust the number of iterations
print(
    f"Execution time for cpp argsort with an array of size {array_size}: {execution_time2} seconds"
)

try:
    print(f"Gain: {execution_time/execution_time2}")
except TypeError:
    pass
