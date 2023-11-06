import os

from setuptools import find_namespace_packages, setup

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SETUP_PTH, "README.rst")) as f:
    desc = f.read()


setup(
    name="pymatgen-analysis-myaddon",
    packages=find_namespace_packages(include=["pymatgen.analysis.*"]),
    version="0.0.1",
    install_requires=["pymatgen>=2023.8.10"],
    extras_require={
        "dev": [
            "pytest==7.1.2",
            "pytest-cov==3.0.0",
            "coverage==6.2",
            "mypy==0.950",
            "ruff",
        ]
    },
    package_data={},
    python_requires=">=3.9",
    author="materials virtual lab",
    author_email="ongsp@eng.ucsd.edu",
    maintainer="materials virtual lab",
    url="https://github.com/materialsproject/pymatgen-addon-template",
    license="BSD",
    description="A template for creating add-ons for pymatgen.",
    long_description=desc,
    keywords=["pymatgen"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
