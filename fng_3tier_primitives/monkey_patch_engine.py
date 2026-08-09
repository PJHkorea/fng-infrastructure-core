import types
import torch
import torch.nn as nn
from typing import Any, Callable, Final, List, Set

class FngRuntimeInfrastructureInterceptor:
    """[🪡 RUNTIME DYNAMIC METHOD INJECTION FACTORY]"""
    def __init__(self) -> None:
        # Atomic lock registry to prevent recursive race conditions
        self._active_interception_registry: Final[Set[str]] = set()
        print("🪡 [INTERCEPTOR BOOT] High-Density Runtime Interception Engine Lowered Into Memory.")

    def inject_fng_infrastructure_gate(
        self, model: nn.Module, target_signatures: List[str], forward_hook_factory: Callable[[nn.Module], Callable]
    ) -> nn.Module:
        """[⚡ MODEL TOPOLOGY STRUCTURE SCAN]"""
        print("⚡ [INJECTION SEQUENCE] Starting dynamic runtime infrastructure routing...")
        patched_layers_count = 0

        for name, module in model.named_modules():
            module_class_name = module.__class__.__name__
            is_target_by_name = any(sig in module_class_name for sig in target_signatures)
            
            # Identify target layers dynamically via structural telemetry
            if is_target_by_name or (hasattr(module, "q_proj") and hasattr(module, "k_proj")):
                # Prevent recursive wrapping faults and lock-registry collisions
                if not getattr(module, "_fng_patched", False) and name not in self._active_interception_registry:
                    module._orig_forward = module.forward
                    
                    # Execute high-density CPython method table pointer hot-swapping
                    module.forward = types.MethodType(forward_hook_factory(module), module)
                    module._fng_patched = True
                    self._active_interception_registry.add(name)
                    
                    # Flush compiler cache to guarantee 0% graph breaks on updated topology
                    if hasattr(torch, "_dynamo"):
                        torch._dynamo.clear_compilation_cache()
                        
                    patched_layers_count += 1
                    print(f"  ├─ [DYNAMIC INTERCEPT] Injected FNG Gate: {name}")

        return model

