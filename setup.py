from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import platform


ld_flags = ["-lgomp"]
if platform.freedesktop_os_release()["ID"] == "fedora":
    ld_flags.append("-ltbb")

__version__ = "0.0.1"

ext_modules = [
    Pybind11Extension(
        "midia_cpp",
        ["src/main.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        cxx_std=20,
        extra_compile_args=[
            "-O3",
            "-fopenmp",
            "-D_GLIBCXX_PARALLEL",
            "-march=native",
            "-mtune=native",
        ],
        extra_link_args=ld_flags,
    ),
]

setup(
    name="midia_cpp",
    version=__version__,
    author="Michał Startek",
    description="Export some C++ functions",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
