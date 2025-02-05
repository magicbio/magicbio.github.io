---
published: true
---
## ASIC Physical Design: Coarse Placement란?

디지털 회로 설계에는 다양한 단계가 있습니다.

Synthesis 엔지니어가 RTL code를 Netlist로 변환하여 Place & Route engineer에게 전달합니다.

​

P&R 단계에는 Floor planing, Power Plan, Placement, CTS, Routing, Chipfinish 등 다양한 단계가 있는데..

이 단계를 들여다보면 또 다양한 세부 단계들이 있습니다.

이 세부 단계를 들여다보면... 다양한 EDA 알고리즘을 볼 수 있는데, 차차 알아가보도록 합시다.

​

![0](/assets/img/223678361784/0.png)

​

Coarse Placement란?

Coarse Placement은 디지털 회로 설계의 Place &Route 단계에서 Cell을 실제 좌표계에 배치하는 과정입니다.

Coarse Placement는 설계의 초기 물리적 구현을 준비한다고 보시면 됩니다.

​

(1) Synthesis가 끝난 Netlist에는 "Library cell name과 Instance name으로 구성된 Verilog code"입니다.

(2) 현대 회로 설계에서 Chip 하나의 Instance count가 Billion(10억개)인데, 이것들을 회로 설계 규칙/회로의 목표 스펙에 맞춰서 레이아웃을 하려면 엄청나게 많은 경우의 수 계산을 해야합니다.

(3) 그렇기 때문에 초기단계에서는 모든 것을 고려하진 않습니다. 회로 목표 스펙에 집중해서, 스펙을 맞출 수 있도록 먼저 초기 설계를 끝냅니다.

(나중에 설계 규칙 위반한 부분에 대해서는 Legalizer라는 EDA 알고리즘이 어느정도 수정을하고... EDA tool이 수정하지 못한 부분은 사람이 manual하게 수정합니다.) 

​

요약하면,

초기적 물리적 구현은 "Netlist에 있는 Cell들을 SDC/UPF/Library에 있는 제약 정보를 통해서 대강 배치하는 것입니다."

초기 구현이기 때문에, "DRC와 Legality에 문제가 있을 수 있습니다.

​

백문이 불어일견이죠. 사진을 보면,

![1](/assets/img/223678361784/1.png)

위 그림처럼 평면상에 있어야 할 Cell들이 서로 일부 겹치고... 올라타고... 이런 비현실적인 설계가 됩니다.

배치된 셀은 Grid에서 떨어지지 않으며 서로 겹칠 수 있습니다. 초기 밑그림을 빠르게 그리는 방법입니다.

​

그리고 Legalization 단계에서, 아래 그림처럼 Grid에 맞춰서 + 셀이 서로 올라타지 않게 규칙을 확인하면서 수정하는 단계가 있는거죠.

![2](/assets/img/223678361784/2.png)

​

요약하면,

(1) Coarse Placement는 설계의 물리적 배치를 대략적으로 결정하는 초기 단계입니다. 이 단계에서는 정확한 세부 배치보다는, 셀들을 논리적인 연결성과 PPA 효율을 고려해 대략적으로 배치합니다.

(2) Global Optimization: 셀들의 위치를 결정할 때, 설계 전체의 배선 길이(Net Length)와 성능 목표를 고려하여 전역적으로 최적화합니다.

(3) Routability Check: Coarse Placement는 배선이 가능할지에 대한 초기 평가를 제공합니다. 만약 배치된 셀들이 지나치게 밀집되거나 연결이 복잡하면, 이후 배선 단계에서 문제가 발생할 수 있습니다. 이를 사전에 감지하여 설계 변경이 가능하도록 합니다.

​

​

궁금한 점이 있거나 더 알고 싶은 내용이 있다면 댓글로 남겨주세요! 😊

 해시태그 : 