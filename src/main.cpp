#include <pybind11/pybind11.h>
#include <algorithm>
#include <execution>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

template<typename T> T* get_ptr(py::buffer& buf)
{
    py::buffer_info buf_info = buf.request();
    if(buf_info.size == 0)
        return nullptr;
    return static_cast<T*>(buf_info.ptr);
};


//void argsort(unsigned long *pidx, const double *parr, unsigned long length)
void argsort(py::buffer idx, py::buffer args, size_t length)
{
    unsigned long *pidx = get_ptr<unsigned long>(idx);
    unsigned long *pidx2 = pidx + length;
    const double *parr = get_ptr<double>(args);
    //std::sort(pidx, pidx2, 
    std::sort(std::execution::par_unseq, pidx, pidx2, 
                         [parr](size_t i1, size_t i2)
                         { return *(parr + i1) < *(parr + i2); });
};



PYBIND11_MODULE(midia_cpp, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: python_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("argsort", &argsort, R"pbdoc(
        Argsort in c++

    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
