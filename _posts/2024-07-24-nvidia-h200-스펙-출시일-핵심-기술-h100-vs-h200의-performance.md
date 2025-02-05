---
published: true
---
## NVIDIA H200 스펙, 출시일, 핵심 기술. H100 vs H200의 Performance, power 비교

NVIDIA는 2023년 11월 14일, Hopper 아키텍처 기반의 서버용 GPU인 H200을 발표했습니다.

출시예정일 : 2024년 2분기

![0](/assets/img/223284091006/0.png)

현존 최강 GPU

H200은 서버향 GPU로, Cloud & Data Center에서 AI Training 및 Inference에 사용될 것입니다.

​

NVIDIA H200은 HBM3e를 제공하는 최초의 GPU입니다. NVIDIA H200은 4.8TB/seconds의 속도로 141GB의 메모리를 제공합니다.

이는 이전 제품인 NVIDIA A100에 비해 용량은 거의 두 배, 대역폭은 2.4배 더 커졌습니다.

​

H100 vs H200 (Performance & Power)

![1](/assets/img/223284091006/1.png)

​

![2](/assets/img/223284091006/2.png)

​

![3](/assets/img/223284091006/3.png)

​

​

가격

H200의 가격은 아직 공개되지 않았습니다. H100의 현재 시세가 $40,000정도입니다.

​

​

이번 H200의 핵심기술은 아래 2가지입니다.

​

1. HBM3e

일단 HBM3E를 할 수 있는 Foundry는 삼성전자, SK하이닉스, 마이크론. 3개의 회사입니다.

이 3개의 회사 모두 샘플을 엔비디아에 제출했습니다. 내년 1분기말부터 양산, 2분기부터 공급 예정이니, 엄청나게 치열할 것으로 보입니다.

​

저는 3개의 주식 중 뭘 샀을까요?

![4](/assets/img/223284091006/4.png)

기존 DRAM은 수평적으로 연결하였지만,

1)HBM은 D램을 수직으로 연결하여,

2)메모리 간 거리를 아주 가깝게 만들어

3)메모리 간 데이터 전송 속도도 줄이고, 프로세서와 가까이 위치 시켜

단위시간당 대역폭을 높인 기술이라고 보시면 됩니다.

![5](/assets/img/223284091006/5.png)

출처: 삼성전자​

HBM3e는 세대 이름이구요. 삼성전자와 하이닉스는 HBM3E라는 이름을 쓰고, 마이크론은 HBM3 Gen2라는 이름을 사용합니다.

​

업계 소개를 간단히 하면,

![6](/assets/img/223284091006/6.png)

SK 하이닉스 : 가장 먼저 HBM3E 개발함, 현재 가장 높은 점유율 + 높은 신뢰도 + 대형 AI 회사들과 많은 경험 + HBM 시장 선도자

마이크론 : 가장 높은 전력효율 + HBM 후발 주자 + 미국기업이라, 미국에서 엄청 밀어줌.

삼성전자 : HBM3E는 가장 늦게 개발함. HBM3E는 가장 높은 성능. DRAM은 업계1위이고, HBM도 업계 1위 도전.

![7](/assets/img/223284091006/7.png)

​

​

2. NVLink-C2C Interconnect (Chiplet)

![8](/assets/img/223284091006/8.png)

NVLink-C2C는 칩렛(Chiplet)을 통해 NVIDIA GPU, DPU, CPU를 일관성 있게 맞춤형 실리콘에 상호 연결하도록 합니다.

SerDes 및 Link 설계 기술을 바탕으로 구축됩니다.

NVIDIA NVLink-C2C 상호 연결은 Advanced Packaging을 통해

- 최대 25배 더 높은 Energy Efficiency

- 면적 효율성은 NVIDIA 칩의 PCIe Gen 5 PHY보다 90배 우수

- 초당 900GB 상호 대역폭

추가로, NVIDIA NVLink-C2C는 PCB 수준 통합, MCM, 실리콘 인터포저, 웨이퍼 레벨 연결을 통해 더욱 확장이 가능.

​

​

​

무어의 법칙 종말에 대응하려면,

-> SoC 설계 기술 발전. 그러나 Chip size가 너무 커지면 수율+경제성 문제

-> Chiplet

​

​

 해시태그 : 