cmake_minimum_required(VERSION 3.8)
project(lifegame)
add_library(lifegame lifegame.cpp)
include_directories(/usr/local/Cellar/cpputest/3.8/include/)
target_link_libraries(lifegame /usr/local/Cellar/cpputest/3.8/lib/libCppUTest.a)

