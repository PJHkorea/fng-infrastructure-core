import os
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# ⚙️ Import the pre-baked 3-tier compiler arguments manifold from infrastructure setup templates
try:
    from setup_templates.nvcc_flags import build_fng_3tier_compiler_arguments_manifold
    compiler_args = build_fng_3tier_compiler_arguments_manifold()
except ImportError:
    # Fallback registry default mapping if executed in isolation
    compiler_args = {"cxx": ["-O3", "-std=c++20", "-fPIC"], "nvcc": ["-O3", "--use_fast_math", "-fPIC"]}

# 📦 Define C++ or CUDA extension modules if present in the repository
# Engineers can place their raw custom `.cu` and `.cpp` kernels in `fng_3tier_primitives/`
ext_modules = []
cuda_source = os.path.join("fng_3tier_primitives", "fng_cuda_kernel.cu")
cpp_source = os.path.join("fng_3tier_primitives", "fng_cpp_bridge.cpp")

if os.path.exists(cuda_source) and os.path.exists(cpp_source):
    ext_modules.append(
        CUDAExtension(
            name="fng_3tier_primitives.fng_acceleration_backend",
            sources=[cpp_source, cuda_source],
            extra_compile_args=compiler_args
        )
    )

setup(
    name="fng-infrastructure-core",
    version="0.1.0",
    author="PJHkorea",
    description="Centralized 3-Tier Multi-Framework Distributed Control Plane Hub",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    ext_modules=ext_modules,
    cmdclass={
        "build_ext": BuildExtension
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "torch>=2.2.0",
    ],
)
