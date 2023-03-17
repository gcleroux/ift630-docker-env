"""
Testing OpenCL support for intel/nvidia GPU

Author: Guillaume Cleroux
"""
import subprocess as sp

from . import TESTS_PATH


def test_clinfo():
    """Testing supported platform"""
    output = sp.run(["clinfo"], capture_output=True, text=True, check=True)

    assert (
        output.stdout != "Number of platforms                               0\n"
    ), "No detected platform for linked GPU"


def test_opencl():
    """Testing OpenCL support"""
    sp.run(["python3", f"{TESTS_PATH}/opencl/opencl.py"], check=True)
