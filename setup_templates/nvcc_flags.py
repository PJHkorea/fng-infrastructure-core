import sys
from typing import Tuple, Final

# 🔒 [GLOBAL HARDWARE ARCHITECTURE PLATFORM REGISTRY]
# Statically pre-bakes device-side compilation targets (Ampere to Blackwell)
FNG_STATIC_NVCC_ARCH_GENCODE: Final[Tuple[str, ...]] = (
    "-gencode=arch=compute_80,code=sm_80",
    "-gencode=arch=compute_86,code=sm_86",
    "-gencode=arch=compute_89,code=sm_89",
    "-gencode=arch=compute_90,code=sm_90",
    "-gencode=arch=compute_100,code=sm_100"  # Blackwell Support
)

# 🔒 [CORE METADATA COMPILER CONFIGURATIONS]
# Enforces optimized performance flags
FNG_BASE_NVCC_OPTIMIZATION_OPTIONS: Final[Tuple[str, ...]] = (
    "-O3", "--use_fast_math", "-Xcompiler", "-fPIC", "--maxrregcount", "64"
)

def resolve_local_accelerator_capability() -> Tuple[str, ...]:
    """
    [🛰️ BARE-METAL ACCELERATOR TELEMETRY SWEEP]
    Dynamically interrogates the physical GPU runtime registers to extract Compute Capability.
    Appends native hardware targets at compilation time to thoroughly bypass JIT latency spikes.
    """
    dynamic_flags: list[str] = []
    
    # Deferred Import Guard against early bootstrap ModuleNotFoundError anomalies
    try:
        import torch
        if torch.cuda.is_available():  # [[likely]]
            major, minor = torch.cuda.get_device_capability()
            current_arch = f"sm_{major}{minor}"
            
            # Cross-validate against pre-baked static registries to reject redundant mappings
            is_pre_baked = any(f"code={current_arch}" in baked_flag for baked_flag in FNG_STATIC_NVCC_ARCH_GENCODE)
            
            if not is_pre_baked:  # [[unlikely]]
                dynamic_flags.append(f"-gencode=arch=compute_{major}{minor},code={current_arch}")
    except Exception:
        # Bypasses hardware query errors silently on headless cloud CPU compilation hosts
        pass
        
    return tuple(dynamic_flags)

# 🔒 [CORE HOST-SIDE CXX COMPILER OPTIONS]
# Freezes GCC/Clang optimization flags to maximize host-side thread swap suppression.
FNG_BASE_CXX_OPTIMIZATION_OPTIONS: Final[Tuple[str, ...]] = (
    "-O3",         # Maximum inline expansion and aggressive loop unrolling
    "-std=c++20",  # Triggers explicit C++20 concepts and exception fences
    "-fPIC"        # Position Independent Code allocation for shared memory objects
)

def build_fng_3tier_compiler_arguments_manifold() -> dict[str, list[str]]:
    """
    [⚙️ TIER 2 MASTER COMPILER MANIFOLD INTERLOCK]
    Aggregates static optimization targets, host specs, and dynamic device appendices.
    Yields a perfectly structured extra_compile_args dictionary to feed PyTorch's CUDAExtension.
    """
    # Gather localized physical hardware capability profile appendices
    dynamic_hardware_appendix = resolve_local_accelerator_capability()
    
    # Seamlessly fuse immutable static flags with runtime device telemetry arrays
    complete_nvcc_flags = list(FNG_BASE_NVCC_OPTIMIZATION_OPTIONS) + \
                          list(FNG_STATIC_NVCC_ARCH_GENCODE) + \
                          list(dynamic_hardware_appendix)
                          
    complete_cxx_flags = list(FNG_BASE_CXX_OPTIMIZATION_OPTIONS)

    # Direct interface binding back to setup.py compilation engine paths
    return {
        "cxx": complete_cxx_flags,
        "nvcc": complete_nvcc_flags
    }

# 🚀 [ENTRYPOINT LATCH]: Commits structural lock display only during terminal test verification
if __name__ == "__main__":
    manifold_report = build_fng_3tier_compiler_arguments_manifold()
    print("====================================================================")
    print("⚙️ FNG TIER 2 MASTER COMPILER FLAGS MANIFOLD LOCKED")
    print(f" -> Total Aggregated NVCC Flags : {len(manifold_report['nvcc'])}")
    print(f" -> Total Aggregated CXX Flags  : {len(manifold_report['cxx'])}")
    print(" └─ [AOT BINDING COMPLETE] Standardized configuration manifest frozen.")
    print("====================================================================\n")
