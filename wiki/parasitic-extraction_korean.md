# Parasitic Extraction

## 1. Definition: What is **Parasitic Extraction**?
**Parasitic Extraction**는 디지털 회로 설계에서 중요한 과정으로, 회로의 물리적 구현에서 발생하는 비원하는 전기적 특성(즉, 기생 요소)을 분석하고 추출하는 기술을 의미합니다. 이러한 기생 요소는 회로의 성능, 타이밍, 전력 소비 및 신호 무결성에 중대한 영향을 미칠 수 있습니다. Parasitic Extraction은 주로 VLSI(Very Large Scale Integration) 설계에서 필수적인 단계로, 설계자가 회로의 실제 동작을 보다 정확하게 예측할 수 있도록 돕습니다.

Parasitic Extraction의 중요성은 다음과 같습니다. 첫째, 기생 요소는 회로의 동작에서 예기치 않은 지연을 초래할 수 있으며, 이는 클록 주파수 및 타이밍 요구 사항을 충족하는 데 문제를 일으킬 수 있습니다. 둘째, 기생 커패시턴스와 인덕턴스는 신호의 전파 속도에 영향을 미쳐 신호의 왜곡을 초래할 수 있습니다. 셋째, 이러한 기생 요소는 전력 소비를 증가시키고, 이는 모바일 기기와 같은 전력 제한 환경에서 문제를 일으킬 수 있습니다. 따라서 Parasitic Extraction은 회로 설계 과정에서 필수적으로 수행되어야 하는 단계입니다.

이 과정은 일반적으로 CAD(Computer-Aided Design) 도구를 사용하여 수행되며, 회로의 레이아웃 정보를 바탕으로 기생 요소를 수치적으로 계산합니다. 이러한 계산은 기생 요소가 회로의 성능에 미치는 영향을 예측하고 최적화하는 데 사용됩니다. Parasitic Extraction의 결과는 회로의 SPICE(Simulation Program with Integrated Circuit Emphasis) 모델에 통합되어, 후속 동적 시뮬레이션에서 사용됩니다.

## 2. Components and Operating Principles
Parasitic Extraction의 구성 요소와 작동 원리는 매우 정교하며, 여러 단계로 나뉘어져 있습니다. 이 과정은 주로 레이아웃 정보의 수집, 기생 요소의 모델링 및 시뮬레이션으로 구성됩니다.

첫 번째 단계는 레이아웃 정보의 수집입니다. 이 단계에서는 회로의 물리적 레이아웃을 분석하여 각 구성 요소 간의 거리, 배치 및 연결 상태를 파악합니다. 이 정보는 기생 커패시턴스, 인덕턴스 및 저항을 계산하는 데 필수적입니다. 레이아웃 정보는 일반적으로 GDSII 또는 OASIS 형식으로 저장됩니다.

두 번째 단계는 기생 요소의 모델링입니다. 이 과정에서는 수집된 레이아웃 정보를 바탕으로 기생 커패시턴스, 인덕턴스 및 저항을 수학적으로 모델링합니다. 기생 커패시턴스는 주로 인접한 도체 간의 전기적 유도에 의해 발생하며, 기생 인덕턴스는 도체의 길이와 회로의 배치에 따라 결정됩니다. 이들 기생 요소는 회로의 동작에 중대한 영향을 미치므로, 정확한 모델링이 필요합니다.

세 번째 단계는 시뮬레이션입니다. 모델링된 기생 요소는 SPICE와 같은 시뮬레이션 도구에 통합되어, 회로의 동작을 시뮬레이션합니다. 이 단계에서는 기생 요소가 회로의 성능에 미치는 영향을 분석하여, 설계자가 필요한 조정을 할 수 있도록 합니다. 최적화 과정에서는 기생 요소를 최소화하거나, 회로의 배치를 재조정하여 성능을 향상시킬 수 있습니다.

이러한 과정은 각기 다른 CAD 도구와 알고리즘을 통해 수행되며, 각 도구는 고유한 기법과 방법론을 가지고 있습니다. 예를 들어, FastCap과 같은 도구는 3D 기생 커패시턴스를 빠르게 계산할 수 있는 알고리즘을 사용합니다. 또한, 기생 요소의 추출은 회로의 복잡성에 따라 다르게 접근해야 하며, 대규모 VLSI 설계에서는 더욱 정교한 방법이 요구됩니다.

### 2.1 (Optional) Subsections
#### 2.1.1 Layout Extraction
Layout Extraction은 회로의 레이아웃에서 기생 요소를 추출하는 첫 번째 단계입니다. 이 과정에서는 도체 간의 거리, 크기 및 배치 정보를 수집하여 기생 요소의 전기적 특성을 계산합니다.

#### 2.1.2 Parasitic Modeling
Parasitic Modeling은 기생 요소를 수학적으로 표현하는 과정입니다. 이 단계에서는 기생 커패시턴스와 인덕턴스를 정의하고, 이를 통해 회로의 동작을 예측할 수 있도록 합니다.

#### 2.1.3 Simulation Integration
Simulation Integration은 모델링된 기생 요소를 SPICE와 같은 시뮬레이션 도구에 통합하는 과정입니다. 이 단계에서는 기생 요소가 회로의 성능에 미치는 영향을 분석하여 최적화를 위한 데이터를 제공합니다.

## 3. Related Technologies and Comparison
Parasitic Extraction은 여러 관련 기술 및 방법론과 비교될 수 있습니다. 이들 기술은 기생 요소의 영향을 다루는 방식에서 차이를 보입니다.

첫째, **RC Extraction**은 기생 저항과 커패시턴스를 추출하는 데 중점을 둔 기술입니다. RC Extraction은 Parasitic Extraction의 한 부분으로 간주될 수 있으며, 회로의 타이밍 분석 및 전력 소비 예측을 위해 필수적입니다. 그러나 RC Extraction은 기생 인덕턴스를 고려하지 않기 때문에 고속 회로에서는 한계가 있습니다.

둘째, **Signal Integrity Analysis**는 신호의 무결성을 평가하는 과정으로, Parasitic Extraction의 결과를 바탕으로 수행됩니다. Signal Integrity Analysis는 기생 요소가 신호의 왜곡 및 지연에 미치는 영향을 분석하여, 설계자가 회로의 성능을 개선할 수 있도록 합니다. 이 과정은 고속 디지털 회로에서 특히 중요합니다.

셋째, **Timing Analysis**는 회로의 타이밍 특성을 평가하는 과정입니다. Parasitic Extraction의 결과는 Timing Analysis에 통합되어, 회로의 클록 주파수 및 타이밍 요구 사항을 충족하는지 여부를 평가합니다. Timing Analysis는 회로의 성능을 최적화하는 데 필수적입니다.

이러한 기술들은 각각의 목적과 방법론이 다르지만, Parasitic Extraction과 밀접하게 연결되어 있으며, 회로 설계의 전반적인 성능을 향상시키는 데 기여합니다. 예를 들어, 고속 디지털 회로 설계에서는 Parasitic Extraction과 Signal Integrity Analysis를 함께 수행하여 신호의 왜곡을 최소화하고, 최적의 타이밍을 확보할 수 있습니다.

## 4. References
- Cadence Design Systems
- Synopsys
- Mentor Graphics
- IEEE (Institute of Electrical and Electronics Engineers)
- ACM (Association for Computing Machinery)

## 5. One-line Summary
Parasitic Extraction은 디지털 회로 설계에서 기생 저항, 커패시턴스 및 인덕턴스를 분석하여 회로 성능을 최적화하는 필수적인 과정입니다.