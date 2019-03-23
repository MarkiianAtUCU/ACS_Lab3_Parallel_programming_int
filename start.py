import subprocess
import os
import sys

SINGLE_THREAD_PATH = "./build/prime_numbers"+".exe" if os.name == 'nt' else ""
MULTI_THREAD_PATH  = "./build/prime_numbers_single_thread"+".exe" if os.name == 'nt' else ""


def single_thread(number_of_iterations):
    for i in range(number_of_iterations):
        subprocess.run(SINGLE_THREAD_PATH)


def multi_thread(number_of_iterations, number_of_threads):
    for i in range(number_of_iterations):
        subprocess.run(MULTI_THREAD_PATH)


def main(number_of_iterations):
    pass


if __name__ == "__main__":
    main(100)
