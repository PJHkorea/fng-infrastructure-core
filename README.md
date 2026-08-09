# fng-infrastructure-core

`fng-infrastructure-core`는 대규모 AI 컴파일러 가속 및 하위 시스템 하이재킹을 제어하기 위한 초고속 최적화 인프라 코어 레포지토리입니다. CPython 내부 구조 제어, 제로 카피 데이터 터널링, 그리고 하드웨어 가속 컴파일 고도화를 자동화합니다.

## 📂 프로젝트 디렉토리 구조

```text
fng-infrastructure-core/
├── .github/workflows/
│   └── 3tier_compiler_audit.yml     # 전역 범용 닌자 가속 & 항상성 회귀 테스트 러너
├── fng_3tier_primitives/
│   ├── dlpack_tunnel.py             # 0-byte 가상 주소선 하이재킹 공통 클래스
│   └── monkey_patch_engine.py       # CPython 메서드 테이블 탈취 공통 팩토리
└── setup_templates/
    └── nvcc_flags.py                # -O3, --use_fast_math, sm_80~sm_90 최적화 맵
```

---

## 🛠️ 핵심 컴포넌트 상세 설명

### 1. CI/CD 및 자동화 가속 (`.github/workflows/`)
* **`3tier_compiler_audit.yml`**
  * **역할:** 전역 범용 Ninja(닌자) 빌드 가속 엔진 및 시스템 항상성 회귀 테스트 러너입니다.
  * **기능:** 컴파일러 최적화 파이프라인의 변경 사항을 감지하고, 고속 병렬 빌드를 수행하여 인프라의 안정성과 제로 회귀를 보장합니다.

### 2. 3계층 하위 시스템 프리미티브 (`fng_3tier_primitives/`)
* **`dlpack_tunnel.py`**
  * **역할:** 오버헤드가 없는 `0-byte` 가상 주소선 하이재킹 공통 클래스입니다.
  * **기능:** 메모리 복사(Copy) 없이 서로 다른 프레임워크나 런타임 간에 텐서 데이터의 가상 주소 포인터를 직접 매핑하여 데이터 통신 지연 시간을 제로로 축소합니다.
* **`monkey_patch_engine.py`**
  * **역할:** CPython 내부 메서드 테이블(Method Table) 탈취 공통 팩토리입니다.
  * **기능:** 런타임 환경에서 CPython 레벨의 함수 및 객체 메서드 테이블을 동적으로 하이재킹하여, 프레임워크 핵심 로직을 커스텀 가속 레이어로 우회시킵니다.

### 3. 컴파일러 셋업 템플릿 (`setup_templates/`)
* **`nvcc_flags.py`**
  * **역할:** NVIDIA CUDA 컴파일러(NVCC) 전용 고성능 최적화 플래그 맵입니다.
  * **기능:** 최고 수준의 컴파일러 최적화 플래그(`-O3`), 고속 부동소수점 연산(`--use_fast_math`), 그리고 Ampere부터 Hopper 아키텍처(`sm_80` ~ `sm_90`)에 최적화된 GPU 마이크로아키텍처 코드를 생성하도록 제어합니다.
