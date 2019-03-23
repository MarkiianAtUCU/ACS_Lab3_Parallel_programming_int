import subprocess
import os
import sys

SINGLE_THREAD_PATH = "./build/prime_numbers_single_thread"+".exe" if os.name == 'nt' else "./build/prime_numbers_single_thread"
MULTI_THREAD_PATH  = "./build/prime_numbers"+".exe" if os.name == 'nt' else "./build/prime_numbers"
THREADS = [4, 8, 16, 32, 64, 256, 512]


def single_thread(number_of_iterations):
    time = []
    res = []
    for i in range(number_of_iterations):
        print("SINGLE ITERATION: ", i + 1)
        result = subprocess.run([SINGLE_THREAD_PATH], stdout=subprocess.PIPE)
        temp = result.stdout.decode('utf-8').strip().split()
        time.append(temp[1])
        res.append(temp[3])
        f = open("out.txt", "a")
        f.write(f"SINGLE ITERATION:{i + 1} {temp[1]} {temp[3]}\n")
        f.close()
    return time, res


def multi_thread(number_of_iterations, number_of_threads):
    time = []
    res = []
    for i in range(number_of_iterations):
        print("MULTI ITERATION: ", i + 1)
        result = subprocess.run([MULTI_THREAD_PATH, str(number_of_threads)], stdout=subprocess.PIPE)
        temp = result.stdout.decode('utf-8').strip().split()
        time.append(temp[1])
        res.append(temp[3])
        f = open("out.txt", "a")
        f.write(f"MULTI ITERATION:{i + 1} {temp[1]} {temp[3]}\n")
        f.close()
    return time, res


def check_results(results):
    res = set(results)

    if len(res) == 1:
        print("All values are equal")
    else:
        print("Some values are different")


def main(number_of_iterations):
    single_time, single_res = single_thread(number_of_iterations)

    multi_time_res = []
    for thread in THREADS:
        print("THREADS: ", thread)
        f = open("out.txt", "a")
        f.write(f"THREADS:{thread}\n")
        f.close()
        multi_time, multi_result = multi_thread(number_of_iterations, thread)
        multi_time_res.append([multi_time, multi_result])

    all_results = []

    for i in range(len(multi_time_res)):
        all_results += multi_time_res[i][1]
    all_results += single_res

    check_results(all_results)


if __name__ == "__main__":
    if sys.argv.__len__() != 2 and sys.argv[1].isdigit():
        print("You don't enter number of iterations")
    else:
        main(int(sys.argv[1]))
