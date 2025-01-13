## Parasitic Extraction 및 Metal Layer Stack, RC extraction

Parasitic Extraction란?

Parasitic Extraction (PEX)은 반도체 회로의 Layout을 바탕으로 전기적 특성(Resistance, Capacitance 등)을 추출하는 과정입니다. 그리고 우리는 이것을 R,C Value라고 합니다.

이 과정은 Physical Domain과 Electrical Domain 간의 정보를 연결하여 회로의 성능을 최적화합니다.

특히 타이밍과 파워 분석에 필수적입니다.

​

![0](./asset/0.png)

​

EDA에서 PEX는 전자 회로에서 설계된 소자와 배선 Interconnect에 존재하는 Parasite 효과를 계산하는 과정이다. 여기에는 Parasitic Capacitance, Parasitic Resistance, Parasitic Inductance가 포함됩니다.

​

PEX의 핵심 목적은 회로의 정확한 modeling입니다. 이를 통해 디지털 및 아날로그 회로의 실제 반응을 상세히 시뮬레이션할 수 있다.

​

디지털 회로의 경우, PEX 데이터는 다음과 같은 분석 및 시뮬레이션에 사용됩니다.

Timing Analysis

Power Analysis

Circuit Simulation

Signal Integrity Analysis (Signal delay, Signal noise)

IR Drop

LVS

​

Wikipedia를 따르면, 초기 집적회로(IC)에서는 Routing의 영향이 미미했기 때문에 배선을 회로의 전기적 요소로 고려하지 않았다고합니다.  0.5um부터 설계자들이 고려를 하기 시작했구요.

https://en.wikipedia.org/wiki/Parasitic_extraction

[Parasitic extraction - Wikipedia](https://en.wikipedia.org/wiki/Parasitic_extraction) : In electronic design automation , parasitic extraction is the calculation of the parasitic effects in both the designed devices and the required wiring interconnects of an electronic circuit : parasitic capacitances , parasitic resistances and parasitic inductances , commonly called parasitic device...

Interconnect Capacitance Extraction

Interconnect Capacitance는 다음 정보를 추출 도구에 제공하여 계산됩니다.

설계의 레이아웃(Top View Layout) 정보(Layer 상의 input polygon)

LVS(Layout Versus Schematic) 분석을 통해 얻은 소자 및 Pin mapping 정보

레이어의 구조 정보와 Cap 값

이 정보를 기반으로, 레이아웃 배선에 입력 폴리곤과 단면 구조에 따라 기생 커패시터를 추가, 추출된 출력 넷리스트에는 입력 디자인 넷리스트와 동일한 입력 넷이 포함되며, 이들 넷 사이에 기생 커패시터 소자가 추가됩니다.

​

https://youtu.be/p1GXl6ZI90Q

[![VLSI - Lecture 6a: Interconnect (Capacitance)](https://i.ytimg.com/vi/p1GXl6ZI90Q/hqdefault.jpg)](https://youtu.be/p1GXl6ZI90Q)

설명 : Bar-Ilan University 83-313: Digital Integrated CircuitsThis is Lecture 6 of the Digital Integrated Circuits (VLSI) course at Bar-Ilan University. In this cou...

---

Interconnect Resistance Extraction

설계의 레이아웃(Top View Layout) 정보(레이어 상의 입력 폴리곤)

LVS(Layout Versus Schematic) 분석을 통해 얻은 소자 및 Pin mapping 정보

레이어의 구조 정보와 저항값(Resistivity)

이 정보를 기반으로 배선의 여러 부분 간에 추가 Resistance을 배치한 Sub-wires set를 생성한다. Interconnect Resistance는 이 Sub-node들 간에 분배됩니다.

​

https://www.youtube.com/watch?v=kk2z8WnVSLM&ab_channel=AdiTeman

[![VLSI - Lecture 6b: Resistance and Interconnect Modeling](https://i.ytimg.com/vi/kk2z8WnVSLM/hqdefault.jpg)](https://www.youtube.com/watch?v=kk2z8WnVSLM&ab_channel=AdiTeman)

설명 : Bar-Ilan University 83-313: Digital Integrated CircuitsThis is Lecture 6 of the Digital Integrated Circuits (VLSI) course at Bar-Ilan University. In this cou...

​

이제 진짜 단순한 개념 정도는 보았고,

Pharasitic device에 대해서 읽어보고, 그리고 각 파일을 해석하는 방법들까지 알아보겠습니다.

​

그리고 위 영상들 퀄리티가 엄청 좋습니다. 시간 있으실 때 정주행 함 하시지요.

 해시태그 : 