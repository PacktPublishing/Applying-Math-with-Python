
import numpy as np
from setuptools import setup, Extension
from Cython.Build import cythonize

hybrid = Extension(
    "hybrid_mandel",
    sources=["python_mandel.py"],
    include_dirs=[np.get_include()],
    define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]
)

cython = Extension(
    "cython_mandel",
    sources=["cython_mandel.pyx"],
    include_dirs=[np.get_include()],
    define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]
)

extensions = [hybrid, cython]

setup(
    ext_modules = cythonize(extensions, compiler_directives={"language_level": "3"}),
)