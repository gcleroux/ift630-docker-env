"""
Testing C++, python and SR implementation in docker image

Author: Guillaume Cleroux
"""
import subprocess as sp

from . import IMAGE_PATH, TESTS_PATH


def test_cpp():
    """Testing C++"""
    # Compile c++ program
    sp.run(
        [
            "g++",
            "-std=c++11",
            f"{TESTS_PATH}cpp/convolution.cpp",
            "-o",
            f"{TESTS_PATH}cpp/convolution",
            "-lpthread",
        ],
        check=True,
    )
    sp.run(
        [
            f"{TESTS_PATH}cpp/convolution",
            "1",
            "512",
            "512",
            IMAGE_PATH,
            f"{TESTS_PATH}cpp/sortie.raw",
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


def test_pythonMP():
    """Testing python with multiprocessing module"""
    sp.run(
        [
            "python3",
            f"{TESTS_PATH}pythonMP/convolution.py",
            "1",
            "512",
            "512",
            IMAGE_PATH,
            f"{TESTS_PATH}pythonMP/sortie.raw",
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
            f"gray:{TESTS_PATH}pythonMP/sortie.raw",
            f"{TESTS_PATH}pythonMP/sortie.png",
        ],
        check=True,
    )


def test_pythonMT():
    """Testing python with threading module"""
    sp.run(
        [
            "python3",
            f"{TESTS_PATH}pythonMT/convolution.py",
            "1",
            "512",
            "512",
            IMAGE_PATH,
            f"{TESTS_PATH}pythonMT/sortie.raw",
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
            f"gray:{TESTS_PATH}pythonMT/sortie.raw",
            f"{TESTS_PATH}pythonMT/sortie.png",
        ],
        check=True,
    )


def test_sr():
    """Testing SR"""
    sp.run(
        ["sr", "-o", f"{TESTS_PATH}sr/convolution", f"{TESTS_PATH}sr/convolution.sr"],
        check=True,
    )
    sp.run(
        [
            f"{TESTS_PATH}sr/convolution",
            "1",
            "512",
            "512",
            IMAGE_PATH,
            f"{TESTS_PATH}sr/sortie.raw",
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
            f"gray:{TESTS_PATH}sr/sortie.raw",
            f"{TESTS_PATH}sr/sortie.png",
        ],
        check=True,
    )


def test_clinfo():
    """Testing clinfo util"""
    sp.run(["clinfo"], check=True)
