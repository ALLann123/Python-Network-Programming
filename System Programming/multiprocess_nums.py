#!/usr/bin/python3
import time
import multiprocessing as mp
import math

def make_calculation(numbers, results_list):
    for number in numbers:
        results_list.append(math.sqrt(number ** 3))  # Append results to the shared list

if __name__ == '__main__':
    number_list = list(range(1000000))

    # Create a Manager to hold shared lists
    manager = mp.Manager()
    result_a = manager.list()  # Shared list
    result_b = manager.list()  # Shared list
    result_c = manager.list()  # Shared list

    # Create processes
    p1 = mp.Process(target=make_calculation, args=(number_list, result_a))
    p2 = mp.Process(target=make_calculation, args=(number_list, result_b))
    p3 = mp.Process(target=make_calculation, args=(number_list, result_c))

    start = time.time()

    # Start processes
    p1.start()
    p2.start()
    p3.start()

    # Wait for processes to finish
    p1.join()
    p2.join()
    p3.join()

    end = time.time()

    print(f"Execution time: {end - start:.2f} seconds")
