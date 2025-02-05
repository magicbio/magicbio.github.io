---
published: true
---
## Verilog Simulation과 Debugging이란? VCS란? Verdi란?

복잡한 디지털 회로 설계를 검증하고 디버깅하는 데 있어서 "Simulation Tool과 Debug Tool"은 필수적인 역할을 합니다.

현업에서 가장 많이 쓰이는 Synopsys의 VCS와 Verdi입니다.

​

학생들은 EDA Playground에서 맛보기 정도 볼 수 있고, Vivado, 쿼터스, 모델심 등에서도 맛보기를 할 수 있습니다. 

https://www.edaplayground.com/

[EDA Playground](https://www.edaplayground.com/) : Edit, save, simulate, synthesize SystemVerilog, Verilog, VHDL and other HDLs from your web browser.

Simulator Tool

회로 시뮬레이션이란, 디지털 회로 설계의 Functional Design Verification을 위해 설계된 모델을 테스트하고 분석하는 과정입니다. 이는 설계자가 회로의 동작을 예측하고 다양한 입력 조건에 대해 설계가 올바르게 작동하는지 확인하는 데 사용됩니다.

![0](/assets/img/223459347743/0.png)

사실 VCS로 Graphic UI 볼 일은 거의 없긴한데, GUI는 이런 화면입니다. 보통은 그냥 텍스트파일로 봅니다.

Synopsys사의 VCS (Verilog Compiler Simulator)가 대표적인 Simulator tool입니다. 

​

기본적인 컨셉 자체는 Verilog File에 Verilog testbench 넣고 결과 파형을 본다는 것인데,

테스트 벡터 이외에도 SDF 등 다양한 입력 파일을 넣을 수 있고, 출력파일으로도 다양한 파일을 출력 할 수 있습니다.

Function Simulation, DFT simulation, Dynamic Timing Analysis 등이 Simulator tool로 진행됩니다.

​

Debug Tool

디버깅은 시뮬레이션 중 발견된 오류를 편리하게 분석하기 위해 사용됩니다.

​

예를들어 RTL Code나 Verilog Netlist에서 Simulation을 하고, 718ns에 Top/Subsystem/Flipflop97/Q에 1이 나와야하는데 왜 X가 나왔지????

Root cause를 보려면 결국 propagation되는 signal들을 따라가야하는데, 이런걸 편하게 해주는 Tool이에요.

이외에도, GUI로 회로를 보기가 이것만큼 편한 툴이 없기에 다양한 이유들로 사용합니다.

![1](/assets/img/223459347743/1.png)

Verdi는 VCS와 자주 연동되어 사용되는 디버깅 도구로, 엔지니어가 시뮬레이션 결과를 시각적으로 분석하고, 신호의 변화와 타이밍을 확인하며, 문제를 빠르게 찾고 해결할 수 있도록 도와줍니다.

엔진이 다른 EDA에 비해 가볍기 때문에 instance간 이동하면서 보기도 쉽고, 매우 편리한 tool입니다.

​

Design만 있으면 Debug tool을 사용 할 수 있고,

Waveform file이 있으면 파형도 볼 수 있습니다.

​

그래서 Simulation -> Debug tool 이런 식으로 유기적으로 사용됩니다.

입출력파일

- Verilog

- SDF

- KDB

- FSDB

- SAIF

- VPD 이런 것들 있습니다.

​

근데 이런 강의들을 유튜브에서 한국어 강의로 볼 수 있더라구요? VCS Training이긴한데,  업계에서 잘 나가는 툴인만큼, 다른 툴도 비슷합니다.

Design Verification업무, Physical Implementation, DFT 업무 하실 분들은 꼭 보세요 ㅎㅎ

참고로 이런 강의 들으려면.. $800정도 가격이고, 대부분이 영어 강의입니다. 

https://youtu.be/JifEOTIuDuc?si=G5SXG-hQehJbb1pw

[![1. VCS -  VCS flow overview (VCS VerdiBasic  강의)](https://i.ytimg.com/vi/JifEOTIuDuc/hqdefault.jpg)](https://youtu.be/JifEOTIuDuc?si=G5SXG-hQehJbb1pw)

설명 : VCS Verdi basic 집합 강의입니다.음질 좋습니다. 그동안 음질 안좋은 강의 듣느라 고생하셨습니다.

https://youtu.be/uNWSHwAHP-U?si=vL-1ELi7J7OEuhsF

[![[Synopsys tool 강좌] VCS (1/3) - VCS 기본 flow 및 기본 option](https://i.ytimg.com/vi/uNWSHwAHP-U/hqdefault.jpg)](https://youtu.be/uNWSHwAHP-U?si=vL-1ELi7J7OEuhsF)

설명 : Synopsys VCS 에 대해 알아볼까요?1편으로 VCS 기본 사용법입니다. (flow 및 option)음질 안좋은 건 죄송 ㅠㅠ문의사항은 댓글로 해주세요

https://youtu.be/LxOg_qnA0dM?si=SMAjaHTfrzsD08uq

[![[Synopsys tool] VCS advanced feature - DTL (Dynamic Test Loading)](https://i.ytimg.com/vi/LxOg_qnA0dM/hqdefault.jpg)](https://youtu.be/LxOg_qnA0dM?si=SMAjaHTfrzsD08uq)

설명 : VCS의 advanced feature 중의 하나인 DTL에 대한 설명입니다. example 도 있습니다.

​

 해시태그 : 