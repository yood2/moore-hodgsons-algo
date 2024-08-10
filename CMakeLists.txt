cmake_minimum_required(VERSION 3.4)
project(moore_hodgsons)
add_subdirectory(pybind11)
pybind11_add_module(moore_hodgsons main.cpp)