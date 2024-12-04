from setuptools import setup
from Cython.Build import cythonize
setup(
    name='find_imgae',
    ext_modules=cythonize("find_imgae.pyx"),
    language_level=3
)

