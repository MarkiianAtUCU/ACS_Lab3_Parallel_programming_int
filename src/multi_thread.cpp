// This is a personal academic project. Dear PVS-Studio, please check it.
// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com

#include <iostream>
#include <thread>
#include <chrono>
#include <atomic>

#include "time_meter.h"
#include "config.h"


void prime(int n, int thread_n, int num_of_threads, std::atomic<int> & res_thread) {
    if (n<2) return;
    int res = 0;
    int flag ;
    for (int i = 3 + 2* thread_n; i <= n; i+=2*num_of_threads) {

        flag = 0;
        if (((i > 10) && (i % 10 == 5)) || (i % 2 == 0)) {
            continue;
        }

        for (int j = 3; j < n; j += 2) {
            if (j * j > i) {
                res += 1;
                flag = 1;
                break;
            }

            if (i % j == 0) {
                flag = 1;
                break;
            }
        }
        if (!flag) {
            res += 1;
        }
    }
    res_thread += res;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Usage:  prime_numbers th\n"
                     "Where:  th -- number of threads used" << std::endl;
        return 1;
    }


    int num_threads = std::stoi(argv[1]);
    std::atomic<int> res{0};
    std::thread all_threads[num_threads];

    auto start = get_current_time_fenced();
    for (int i = 0; i < num_threads; ++i) {
        all_threads[i] = std::thread(prime, testing_num, i, num_threads, std::ref(res));
    }

    for (int i = 0; i < num_threads; ++i) {
        all_threads[i].join();
    }
    res+=1;

    auto end = get_current_time_fenced();
    long long time = to_us(end - start);

    std::cout<<"T: "<<time<<std::endl;
    std::cout<<"Res: "<<res<<std::endl;
    return 0;
}

