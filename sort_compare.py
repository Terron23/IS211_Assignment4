import time
import random



def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return a_list, time.time() - start_time



def shell_sort(a_list):
    start_time = time.time()
    sublist_count = len(a_list) / 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count / 2
    return a_list, time.time() - start_time
    

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    start_time = time.time()
    a_list.sort()
    return a_list, time.time() - start_time
    

def main():
    n = 100
    sample = [500, 1000, 10000]
    avg = {"ins": 0,
        "shell": 0,
        "py_sort": 0,}

    for i in range(n):
        random_num = random.choice(sample)
        arr = random.sample(range(0, random_num), random_num)
        avg["ins"] += insertion_sort(arr)[1]
        avg["shell"] += shell_sort(arr)[1]
        avg["py_sort"] += python_sort(arr)[1]
    
    #Print statements
    ins_avg = 'Insertion Sort took {0} seconds to run, on average'.format(str(avg["ins"] /n))
    shell_avg = 'Shell Sort took {0} seconds to run, on average'.format(str(avg["shell"] /n))
    py_sort_avg = 'Python Built-in Sort took {0} seconds to run, on average'.format(str(avg["py_sort"] /n))
    print(ins_avg)
    print(shell_avg)
    print(py_sort_avg)
    return avg

if __name__ == '__main__':
    #no need for argparse as data is random
    main()