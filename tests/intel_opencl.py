import subprocess as sp


def test_intel_clinfo():
    """Testing supported platform"""
    output = sp.run(["clinfo"], capture_output=True, text=True, check=True)
    print(output)

    assert (
        output.stdout != "Number of platforms                               0\n"
    ), "No detected platform for intel GPU"


def test_intel_opencl():
    """Testing OpenCL support"""
    sp.run(["python3", "/tests/opencl.py"], check=True)
