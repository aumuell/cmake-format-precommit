from setuptools import setup, find_packages
setup(
    name="cmakelang-precommit-dummy",
    version="0.0.0",
    packages=find_packages(),
    install_requires=["cmakelang==0.6.13"],
    entry_points={
        # Override the scripts installed by cmakelang so the re.Scanner
        # compatibility shim is active (required on Python 3.15+).
        "console_scripts": [
            "cmake-format = cmake_format_compat.cli:cmake_format",
            "cmake-lint = cmake_format_compat.cli:cmake_lint",
        ],
    },
)
