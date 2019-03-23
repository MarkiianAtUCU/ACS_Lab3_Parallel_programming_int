import subprocess
import os
import sys

SINGLE_THREAD_PATH = "./build/prime_numbers_single_thread"+".exe" if os.name == 'nt' else "./build/prime_numbers_single_thread"
MULTI_THREAD_PATH  = "./build/prime_numbers"+".exe" if os.name == 'nt' else "./build/prime_numbers"
THREADS = [4, 8, 16, 32, 64, 256, 512]


def single_thread(number_of_iterations):
    for i in range(number_of_iterations):
        subprocess.run([SINGLE_THREAD_PATH])


def multi_thread(number_of_iterations, number_of_threads):
    for i in range(number_of_iterations):
        subprocess.run([MULTI_THREAD_PATH, number_of_threads])


def main(number_of_iterations):
    single_thread(number_of_iterations)

    # for thread in THREADS:
    #     multi_thread(number_of_iterations, thread)


if __name__ == "__main__":
    main(1)
