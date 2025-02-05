---
published: true
---
## Tie Cell이란? Tie High Cell, Tie Low Cell

학사 신입 면접질문에 종종 나오는 것 같습니다.

​

Q1. 이 Cell의 동작을 알려주세요?

Q2. 이 Cell이 어떤 곳에 사용될 것 같아요?

![4](/assets/img/223609237659/4.png)

어어.. 음... (왜 입력이 없고 출력만 있는거지... 이거 이렇게 되면 무조건 VCC 값만 출력 될텐데?)

​

이게 Tie Cell중 Tie High cell입니다.

​

​

Tie cell이란?: Tie High cell과 Tie Low cell

Tie High Cell은 반도체 설계에서 Logic Gate의 input pin을 논리적 '1'(High signal, VCC, VDD 등)에 연결,

Tie Low Cell은 '0'(Low signal, VSS/GND)에 안전하게 연결하기 위해 사용되는 특수한 Cell 입니다.

​

단순히 VDD나 Ground에 직접 연결하지 않고 Tie cell을 통하면, 아래의 이점이 있습니다.

​

ESD란 무엇이며, 왜 발생하는가?

1. ESD의 정의

ESD(Electrostatic Discharge)는 정전기 방전으로, 서로 다른 전위를 가진 두 물체 사이에 전하가 급격하게 이동하는 현상입니다. 이로 인해 순간적으로 매우 큰 전류나 전압이 발생할 수 있습니다.

2. ESD의 발생 원인

정전기 축적: 건조한 환경 + 물체 간의 마찰이나 접촉으로 정전기가 축적됩니다.

3. ESD의 효과

VDD 혹은 GND에 설계한 전압보다 더 높거나 더 낮은 전압이 칩에 인가되게 만들 수 있습니다.

그러면 위 문제 때문에 Breakdown Voltage 같은 현상이 일어날 수도 있고,

과도한 전류가 흐르면 Gate와 Metal에 BTI 같은 Aging issue들이 발생 할 수 있습니다.

-> 결국, 외부 물리적인 요인들 때문에 반도체 신뢰성 문제가 발생 할 수 있게됩니다.

​

그래서, VDD Line, GND Line을 Logic gate에 직접 연결하면 ESD 이슈가 그대로 전파되니, 이런 것들을 Filtering 할 수 있는 Cell이 필요합니다.

​

![5](/assets/img/223609237659/5.png)

Tie-High Cell 에서 NMOS Drain과 Gate는 Short되어 있는데, 그 이유는 NMOS가 Saturation region에 있기 때문입니다. 따라서 out은 로직 1 또는 Vdd에 연결됩니다.

Tie-Low Cell 에서 PMOS Drain과 Gate는 Short되어 있는데, 그 이유는 PMOS가 Saturation region에 있기 때문입니다. 따라서 out은 로직 0 또는 Vss에 연결됩니다.

만약에 이게 이해가 안 되시면, NMOS PMOS의 Behavior을 보고나서, VDD가 0일 때, 1일 때. GND가 0일 때 1일 때를 가정해 보세요.

​

​

​

이러한 Physical cell들은 논리 회로 설계에서는 신경을 쓰는 부분이 아닌데,

수율을 높이고 오랫동안 사용 할 수 있는 Reliability를 만드는 것에 도움을 주는 Cell들입니다.

 해시태그 : 