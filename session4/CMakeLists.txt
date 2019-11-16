cmake_minimum_required(VERSION 3.8)
project(lifegame)
set(CMAKE_CXX_STANDARD, 11)
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall")
add_executable(lifegame
  lifegame.cpp
  LifegameRule.cpp
  LifegameRuleTest.cpp)
include_directories(/usr/local/Cellar/cpputest/3.8/include/)
target_link_libraries(lifegame /usr/local/Cellar/cpputest/3.8/lib/libCppUTest.a)
