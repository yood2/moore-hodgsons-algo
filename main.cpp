#include <pybind11/pybind11.h>
#include <iostream>

namespace py = pybind11;
using namespace std

void test_func() {
    cout << "hello world";
}

PYBIND11_MODULE(module_name, handle) {
    handle.doc() = "Doc string here";
    handle.def("python_func", &test_func);
}