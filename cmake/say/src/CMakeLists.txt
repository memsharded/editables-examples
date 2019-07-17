cmake_minimum_required(VERSION 2.8)
project(Say CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)

add_library(say say.cpp)
