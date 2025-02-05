---
published: true
---
## Auto P&R: Placement Blockage란? [VLSI Physical Design]

Introduction: Placement Blockage란?

반도체 Physical Design에서 Placement Blockage는 Cell이 특정 영역에 배치되지 않도록하는 제약 조건"입니다.

이는 EDA Tool의 단점을 막을 수도 있고, 제조 공정을 위한 설계에도 필요한 기술입니다.

​

Placement Blockage는 설계 품질에 직접적인 영향을 미칩니다.

이를 올바르게 설정하지 않으면 다음과 같은 문제가 발생할 수 있습니다:

Routing Congestion: 배선 경로가 부족해 타이밍과 신호 품질이 저하됩니다. 주요 경로에서 셀이 잘못 배치되면, 메탈을 계속 갈아타면서 Net delay도 커지고, Routing congestion으로 인한 Crosstalk으로 인해 Delta delay가 길어져 성능이 저하됩니다. 그리고 Noise는 수율에 영향을 미칩니다.

열 관리(Thermal Management): 특정 영역에 전력이 집중되면 발열 문제가 발생할 수 있습니다. 이는 수율에 직접 영향을 미칩니다.

​

​

​

![0](/assets/img/223680574652/0.png)

Congestion & Timing Optimization Techniques at 7nm Design, By Jaya Patel, Atul Kumar Einfochips![1](/assets/img/223680574652/1.png)

Congestion & Timing Optimization Techniques at 7nm Design, By Jaya Patel, Atul Kumar Einfochips예를 간단히 들어보면,

(1) SRAM이나 PHY 설계는 Full custom 혹은 Semi custom으로 진행하고, Macro cell이라는 형태로 만듬 (Not standard cell) 그래서 모양이 정해져있고, 크기가 꽤나 큰 편이다.

(2)  위 그림의 7시 방향 사각형이 Macro Cell. 이런 Macro cell 근처에.. 특히 모서리 부분에 routing congestion이 매우 크게 발생하는 경향이 자주 보인다.

(3) 그런데 Place 단계에서 이런 모서리에 Standard cell들을 가득 박아놓으면, 이런 곳에 Routing congestion, Short, Crosstalk noise가 발생하고... 결국 이런 것들이 Signoff를 힘들게 만듬.

---

Placement Blockage의 주요 유형

1. Hard Blockage란?

Hard Blockage는 특정 영역에 어떤 셀도 배치되지 않도록 완전히 제한하는 영역입니다.

매크로(macros) 또는 고정된 객체(fixed objects) 주변 공간 보호.

reserved routing regions 확보.

이후 특정 단계에서 셀을 배치하기 위해서, 빈자리를 만들기 위하여 사용.

​

​

2. Soft Blockage란?

Soft Blockage는 기본적으로 Place를 제한하지만, 완전히 금지하지 않고... 일부 Cell만 배치되는 것을 허용합니다.

예를들어 버퍼만 들어올 수 있게 하는 것입니다. "이 부분에서는 DRC Fix, Timing fix만 허용한다~" 이런거죠.

​

3. Partial Blockage란?

배치 할 수 있는 utilization %를 설정

​

4. Keep-Out Margin / Halo란?

Keep-Out Margin은 매크로 주변에 일정한 여유 공간을 설정하여 셀 배치를 제한하는 기능입니다.

매크로 주변에 충분한 공간을 확보해 배선 경로의 혼잡을 방지.

열 방출을 위해 매크로와 셀 간 거리 확보.

![2](/assets/img/223680574652/2.png)

​

​

그래서 이런 것들 왜 한다?

Routing 하고 나면 발생하는 DRC / DFM 문제 방지를 위해 미리 설정하는 것.

​

그러면 이거 어떤식으로 설정해야 잘 설정하는걸까?

이런건 SDC처럼 스펙으로 딱 정해져 있지도 않고.. 디자인 특성과 P&R 엔진을 잘 이해하고... 해도 딱히 명쾌한 답을 찾기 어려움.

그래서 이러한 constraining이나 floor plan guide가 인터넷에 돌아다니지만, 경험 많은 경력자들이 잘하고 있다.

​

그래도 명쾌한 답이 없다. 현재 가장 많이 사용되는 방법은 몇 가지 법칙(?)들을 갖고, 그 법칙 내에서 여러 케이스를 시도해보는 것.

(물론 이것도 어느정도 자동화를 해놓는다.)

​

​

Google의 Alphachip이 이러한 floorplaning 기능을 포함한 AI를 출시했고, (2024년 현재 이거 갖고, 결과 값에 대한 진실 공방이있다만...)

Synopsys나 Cadence는 오래 전부터 이런 AI driven Floorplan을 연구해왔다.

이외에 많은 Fabless들도 "본인 만의 EDA 툴을 개발"하고 있기 때문에 이런 것들을 다들 연구하고 있다고 생각함.

​

아래 예시를 보면, 바둑은 경우의 수가 10^360인데, P&R은 10^90,000이다. 더 미세한 공정으로 들어가고, 칩 사이즈가 더 커진다면 이 경우의 수보다 커질 것은 당연하고...

![3](/assets/img/223680574652/3.png)

일단 알파칩 Git으로 다운 받아놓고, 이것저것 해보고 있는데... 아직은 지원 안되는 것들이 많아서, 개선해야 할 부분들이 많이 보임.

오픈소스로 풀었으니까 중국이 EDA 자립을 위해 먼저 달려들듯?

​

​

​

그리고, EDA의 권위자인 Igor가 12월 4일에 서울대학교에서 아래 주제로 세미나를 한다고 하니 꼭 들어보시길 추천.

​

​

Synopsys Igor Markov, Challenges and Opportunities for AI in Commercial Chip Implementation Tools, 12월 04일(수) , 2024

https://gsds.snu.ac.kr/challenges-and-opportunities-for-ai-in-commercial-chip-implementation-tools-synopsys-igor-markov-12%EC%9B%94-04%EC%9D%BC%EC%88%98/

[Synopsys Igor Markov, Challenges and Opportunities for AI in Commercial Chip Implementation Tools, 12월 04일(수) – 서울대학교 데이터사이언스대학원](https://gsds.snu.ac.kr/challenges-and-opportunities-for-ai-in-commercial-chip-implementation-tools-synopsys-igor-markov-12%EC%9B%94-04%EC%9D%BC%EC%88%98/) : 우리 나라 반도체 산업이 위기를 맞았습니다. NVIDIA, TSMC가 새로 판을 짠 AI 수퍼 컴퓨팅 시장에서 삼성전자나 SK Hynix는 메모리 칩이나 메모리 칩을 여러개 패키징한 HBM의  단순 공급자에 불과하고 CPU 시대에 비해 축소된 현재의 ‘을’ 위상을 벗어날 특별한 전략도 아직 보이지 않습니다. 반면 Google은 AlohaGo와 올해 노벨 화학상을 받은 AlphaFold 2 혁신의 경험을 살려 AI로 컴퓨터 칩 설계를 자동화하는 AlphaChip 프로젝트를 2020년 Nature 논문을 통해 공개했습니다. 이번 주 D...

우리 나라 반도체 산업이 위기를 맞았습니다. NVIDIA, TSMC가 새로 판을 짠 AI 수퍼 컴퓨팅 시장에서 삼성전자나 SK Hynix는 메모리 칩이나 메모리 칩을 여러개 패키징한 HBM의  단순 공급자에 불과하고 CPU 시대에 비해 축소된 현재의 ‘을’ 위상을 벗어날 특별한 전략도 아직 보이지 않습니다.

반면 Google은 AlohaGo와 올해 노벨 화학상을 받은 AlphaFold 2 혁신의 경험을 살려 AI로 컴퓨터 칩 설계를 자동화하는 AlphaChip 프로젝트를 2020년 Nature 논문을 통해 공개했습니다.

이번 주 Data Science 세미나는 한국 반도체 산업의 축소된 위상에 대해 새로운 아이디어를 찾기 위해 구글 AlphaChip 팀과 디테일에서 논쟁을 벌여온 Synopsys(제1의 반도체 CAD 툴 회사)의 Distinguished Architect인 Igor Markov 박사를 초청했습니다.

연사 Markov 박사는 Google AlphaChip 팀의 2000년 Nature 논문의 Academic Integrity 문제를 Comm of ACM 저널에 제기했습니다. 한 때 Google에서 근무한 적도 있습니다. Markov 박사의 강연을 통해 AI + 반도체 설계 도메인 지식의 결합을 통해 미래 반도체 산업 발전 방향에 대한 인사이트를 얻고자 합니다.

Markov 박사 CACM YouTube video 및 CACM article:

https://youtu.be/H7u4MbXonwA

https://dl.acm.org/doi/10.1145/3676845

구글 AlphaChip과 네이처 논문

https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/

Markov 박사에 대한 Google의 반박(Jeff Dean이 공동 저자)

https://arxiv.org/abs/2411.10053

Title: Challenges and Opportunities for AI in Commercial Chip Implementation Tools

Time: 2024. 12. 04. (Wed) 09:00 ~ 10:30

Zoom: https://snu-ac-kr.zoom.us/j/2507466555

​

![4](/assets/img/223680574652/4.png)

​

 해시태그 : https://pubpeer.com/publications/CF94A6B61B60CED3884318FE9F45BD#1