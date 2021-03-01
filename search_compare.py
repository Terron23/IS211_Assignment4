import time
import random

def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found, time.time() - start_time

def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    return found, time.time() - start_time

def binary_search_iterative(a_list, item):
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, time.time() - start_time

def binary_search_recursive(a_list, item):
    start_time = time.time()
    if len(a_list) == 0:
        return False, time.time() - start_time
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True, time.time() - start_time
        elif item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

def main():
    n = 100
    sample = [500]
    #Not sure if it should be 100 list of 500 or 100 list of [500, 1000, 10000] un comment below for the latter
    #sample = [500, 1000, 10000]
    look_for = -1
    avg = {"seq": 0,
        "ord_seq": 0,
        "bin_iter": 0,
        "bin_recur":0}

    for i in range(n):
        random_num = random.choice(sample)
        arr = random.sample(range(0, random_num * 10 + i), random_num)
        arr.sort()
        avg["seq"] += sequential_search(arr, look_for)[1]
        avg["ord_seq"] += ordered_sequential_search(arr, look_for)[1]
        avg["bin_iter"] += binary_search_iterative(arr, look_for)[1]
        recur = binary_search_recursive(arr, look_for)
        if recur[0] == True or recur[0] == False: 
            avg["bin_recur"] += recur[1]
    
    #Print statements
    seq_avg = 'Sequential Search took {0} seconds to run, on average'.format(str(avg["seq"] /n))
    ord_seq_avg = 'Ordered Sequential Search took {0} seconds to run, on average'.format(str(avg["ord_seq"] /n))
    bin_iter_avg = 'Binary Iterative Search took {0} seconds to run, on average'.format(str(avg["bin_iter"] /n))
    bin_recur_avg = 'Binary Recursive Search took {0} seconds to run, on average'.format(str(avg["bin_recur"] /n))
    print(seq_avg)
    print(ord_seq_avg)
    print(bin_iter_avg)
    print(bin_recur_avg)
    return avg
        
if __name__ == '__main__':
    #no need for argparse as data is random
    main()