cmake_minimum_required(VERSION 3.13)
project(Lab3)

set(CMAKE_CXX_STANDARD 14)

find_package( Threads )
add_executable(prime_numbers src/multi_thread.cpp src/config.h src/time_meter.h)
target_link_libraries( prime_numbers ${CMAKE_THREAD_LIBS_INIT} )

add_executable(prime_numbers_single_thread src/single_thread.cpp src/config.h src/time_meter.h)
