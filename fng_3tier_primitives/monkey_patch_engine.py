import types
import torch
import torch.nn as nn
from typing import Any, Callable, Dict, Final, List, Set

class FngRuntimeInfrastructureHijacker:
    """[🪡 RUNTIME DYNAMIC METHOD INJECTION FACTORY]"""
    def __init__(self) -> None:
        # 경쟁 상태 방지를 위한 원자적 락 레지스트리
        self._active_interception_registry: Final[Set[str]] = set()
        print("🪡 [HIJACKER BOOT] High-Density Runtime Interception Engine Lowered Into Memory.")

    def inject_fng_infrastructure_gate(
        self, model: nn.Module, target_signatures: List[str], forward_hook_factory: Callable[[nn.Module], Callable]
    ) -> nn.Module:
        """[⚡ MODEL TOPOLOGY SURGICAL SWEEP]"""
        print("⚡ [HIJACK SEQUENCE] Starting surgical infiltration...")
        patched_layers_count = 0

        for name, module in model.named_modules():
            module_class_name = module.__class__.__name__
            is_target_by_name = any(sig in module_class_name for sig in target_signatures)
            
            # 구조적 특징을 통한 대상 식별
            if is_target_by_name or (hasattr(module, "q_proj") and hasattr(module, "k_proj")):
                # 무한 루프 방지를 위한 중복 패치 검사
                if not getattr(module, "_fng_patched", False) and name not in self._active_interception_registry:
                    module._orig_forward = module.forward
                    # CPython 메서드 테이블 포인터 핫스왑
                    module.forward = types.MethodType(forward_hook_factory(module), module)
                    module._fng_patched = True
                    self._active_interception_registry.add(name)
                    
                    if hasattr(torch, "_dynamo"):
                        torch._dynamo.clear_compilation_cache()
                    patched_layers_count += 1
                    print(f"  ├─ [SURGICAL HIJACK] Injected FNG Gate: {name}")

        return model
