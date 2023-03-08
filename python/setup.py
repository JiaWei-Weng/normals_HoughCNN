from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext_modules = [Extension(
       "NormalEstimatorHoughCNN",
       sources=["NormalEstimatorHoughCNN.pyx", "houghCNN.cxx"],
       include_dirs=["../third_party_includes/"],
       language="c++",             # generate C++ code
       extra_compile_args = ["-fopenmp", "-std=c++11"],
       extra_link_args=['-lgomp']
  )]

setup(
    name = "Hough Normal Estimator CNN",
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext},
    include_dirs=[np.get_include()]
)
