import time
from progressbar import progressbar

# defining a series:


k = 500000000000000000000000000000000
d = 200
a1 = 1
sum_series = 0
method = 2 # Method for sum, 1 for Brute force, 2 for smart

# with a series as list we can calculate the sum of the first n numbers of the series.
print(f"The size of my series is {k}")
index = k  # this is how many numbers you want to sum

if method == 1:

    # calculating the sum the brute force way
    # Creating the list
    time_list1 = time.time()
    series = []
    for i in progressbar(range(k)):
        series.append(a1 + i * d)
    time_list2 = time.time()
    print(f"Time for creating the list of numbers of size {k} and common difference {d}: {(time_list2 - time_list1) * 1000} ms")

    time1 = time.time()  # timing for the loop.
    i = 0


    while i != (index):
        sum_series = sum_series + series[i]
        i = i + 1
    time2 = time.time()  # end of loop

    print(f"Time it took for calculating the sum using method {method}: {(time2 - time1) * 1000} ms")
    print(f"The sum of the first {index} elements of my series is {sum_series}")


elif method == 2:
    # calculating the sum using math
    time1 = time.time()  # timing for the loop.
    ak = a1 + (index-1)*d
    sum_series = (a1 + ak) * index // 2
    time2 = time.time()
    print(f"Time it took for calculating the sum using method {method}: {(time2 - time1) * 1000} ms")
    print(f"The sum of the first {index} elements of my series is {sum_series}")

# calcultaing the time it took to do this.

