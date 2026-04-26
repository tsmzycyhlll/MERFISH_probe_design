from setuptools import setup, find_packages

setup(
    name="merfish_probe_design",
    version="0.1.0",
    description="MERFISH probe design toolkit with customizable readout-bit allocation",
    author="tsmzycyhlll",
    url="https://github.com/tsmzycyhlll/MERFISH_probe_design",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "biopython",
    ],
)
