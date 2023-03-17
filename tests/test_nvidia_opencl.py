"""
Testing OpenCL support for nvidia GPU with C++ bindings
Relevant for 1st TP, since only C++ bindings through CUDA are available

Author: Guillaume Cleroux
"""
import subprocess as sp

from . import IMAGE_PATH, TESTS_PATH


def test_cuda_opencl():
    """Testing CUDA C++ bindings"""
    sp.run(
        [
            "g++",
            "-std=c++11",
            "-I/usr/local/cuda/include",
            "-O3",
            "-o",
            f"{TESTS_PATH}opencl/convolution",
            f"{TESTS_PATH}opencl/convolution.cpp",
            "-L/usr/local/cuda/lib64",
            "-lOpenCL",
        ],
        check=True,
    )
    sp.run(
        [
            f"{TESTS_PATH}opencl/convolution",
            "384",
            "0",
            "512",
            "512",
            IMAGE_PATH,
            f"{TESTS_PATH}opencl/sortie.raw",
            "5",
        ],
        check=True,
    )
    sp.run(
        [
            "convert",
            "-size",
            "512x512",
            "-depth",
            "8",
            f"gray:{TESTS_PATH}cpp/sortie.raw",
            f"{TESTS_PATH}cpp/sortie.png",
        ],
        check=True,
    )
