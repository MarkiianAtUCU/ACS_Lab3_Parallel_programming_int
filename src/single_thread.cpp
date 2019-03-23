// This is a personal academic project. Dear PVS-Studio, please check it.
// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com

#include <iostream>
#include <thread>
#include "time_meter.h"
#include "config.h"


int prime(int n) {
    if (n<2) return 0;
    int res = 0;
    int flag ;
    for (int i = 3; i <= n; i+=2) {

        flag = 0;
        if ( ((i > 10) && (i % 10 == 5)) || (i % 2 == 0)) {
            continue;
        }

        for (int j = 3; j < n; j+=2) {
            if (j*j > i) {
                res += 1;
                flag = 1;
                break;
            }

            if (i % j == 0){
                flag = 1;
                break;
            }
        }
        if (!flag) {
            res +=1;
        }
    }
    return res;
}

int main() {
    int res;
    auto start = get_current_time_fenced();

    res = prime(testing_num) + 1;

    auto end = get_current_time_fenced();
    long long time = to_us(end - start);

    std::cout<<"T: "<<time<<std::endl;
    std::cout<<"Res: "<<res<<std::endl;
    return 0;
}

