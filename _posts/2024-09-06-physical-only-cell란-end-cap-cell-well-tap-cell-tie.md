---
published: true
---
## Physical only cell란? End cap cell, Well Tap Cell, Tie Cell, Decap cell, Filler cell이란? 반도체

흔히 컴퓨터는 0과 1의 세상이라고 부르고, 학사과정에선 "컴퓨터구조론" 등에서 디지털논리회로를 배웁니다.

실제 반도체 칩은 "논리 회로"로 구성되어있지 않습니다. "물리적인 회로"로 구현되어있습니다.

​

Fabless에서는 Foundry가 보내준 PDK를 통해 회로설계를하고,

PDK는 Foundry에서 만듭니다. (PDK가 뭔지 모르시는 분들은 제가 이전에 PDK에 대해 포스팅하였으니, 그 부분 먼저 보시는 것을 권합니다.)

![0](/assets/img/223375326552/0.png)

PDK를 열어보면, 학교에서 배운 논리회로인 "AND, OR, INVERTER, NAND" 이런 Gate 뿐만 아니라,

Filler cell, decap cell 등 처음 보는 Physical cell들이 존재합니다.

​

실제 반도체 동작 환경은 이상적이지 않다는 것을 전제하면 이해가 쉽습니다.

VLSI 설계에서 'Physical only cell'은 미세공정에서 최적의 성능, 전력 효율성 및 신뢰성을 달성하는 데 도움을 줍니다.

​

Physical Cell이란?

반도체의 물성 때문에 사용되는 cell입니다. 실제 반도체 환경은 이상적이지 않습니다. 그러나 우리는 "디지털 논리 회로"처럼 동작하길 원합니다. 이상적인 동작에 가깝게 동작하게 만들기 위해 사용하는 것입니다. 그렇기 때문에 보통은 RTL Level에서 설계하지 않고, Physical Design 단계에 삽입하는 Cell들입니다. 

Physical only cell 이라고도 하는 이러한 특수 셀은 회로의 Logical 동작에 기여하기보다는 주로 Physical한 구현 목적으로 사용되므로 기능적 로직 셀과는 구별됩니다.

​

logic cell은 신호를 반전시킨다던가, 신호에 대한 논리 처리를 합니다.

phyiscal only cell은 신호가 잘 흐르도록, 공정이 잘 되도록, 돕는 cell들이라고도 볼 수 있습니다.

​

Physical Cell들도 종류가 다양한데,  하나씩 간단히 알아보겠습니다.

각각의 목적에 대해만 설명할 것입니다. 동작 원리가 궁금하신 분들은 따로 검색해보세요~ 글이 끝도 없이 길어질까봐 그럽니다.

![1](/assets/img/223375326552/1.png)

​

​

End Cap Cells / Boundary cap cell

![2](/assets/img/223375326552/2.png)

​

반도체 제조 공정에서 칩의 가장자리 부분이 취약합니다.

엔드 캡 셀은 에어백(?) 역할을 하여 주변부에 위치한 표준 셀의 손상 위험을 최소화합니다.

[![End Cap or Boundary Cell | Use of endCap Cells | Placement of endCap Cell | Layout of endCap Cell](https://i.ytimg.com/vi/cs7xA4gIObM/hqdefault.jpg)](https://www.youtube.com/watch?v=cs7xA4gIObM)

설명 : What is end cap cell or Boundary cell, What is the use of end cap cells in ASIC Design? We have explained all about end cap cells in this session with the he...

​

​

Well Tap Cells:

Well tap cell은 MOSFET Substrate coupling effect로 인해 발생할 수 있는 Latch-up 문제를 완화하려고 씁니다.

​

![3](/assets/img/223375326552/3.png)

![4](/assets/img/223375326552/4.png)

​

[![반도체 공학 10-35 CMOS(Latch up)](https://i.ytimg.com/vi/cJR9CQ8tnuo/hqdefault.jpg)](https://www.youtube.com/watch?v=cJR9CQ8tnuo)

설명 : Inverter 구조

​

​

​

Tie Cell:

주로 ESD(Electro Static Discharge) 보호용입니다.

일부 Signal port는 항상 변하지 않고, 늘 안정적인 고정된 신호로 고정되어야 합니다.

Tie-high cell, Tie-low cell은 Clamping되어야 하는 신호를 Tie-Hie를 통해 VDD에 연결하고, 타이 로우를 통해 VSS에 연결합니다.

![5](/assets/img/223375326552/5.png)

Antenna cell

Antenna effect를 극복하기 위해, 역전하 바이어스를 사용한 다이오드 cell입니다.

​

반도체는 불순물을 "도핑"해서 사용합니다.

도핑 방법으로는 반도체 제조 공정에서 "ion implantation" 공정을 사용합니다.

그런데 모든 칩의 모든 표면에 고르게 주입하는게 현실적으로 어렵습니다. 이런 것들이 반도체 물성을 바꾸죠.

이러한 이온 충전량이 특정 수준을 초과하면 게이트가 파괴됩니다. 이 효과를 "Antenna effect"라고 합니다.

​

![6](/assets/img/223375326552/6.png)

![7](/assets/img/223375326552/7.png)

​

​

​

Decap cell:

Power rail에서 IR Drop 방지를 위해 사용합니다.

디지털 회로는 아래처럼 생겼습니다. 둘 다 똑같은 회로에요. 왼쪽은 MOSFET Level로 그린거고, 오른쪽 그림은 Gate level로 그린겁니다.

![8](/assets/img/223375326552/8.png)

VLSI Design에서 대부분의 전력 소비는 Clock Signal에 의해 이루어집니다.

가정: 모든 Clock 관련 회로, 복잡한 IP가 한쪽에 모여있다고 생각하면, 한쪽 Power Rail에 엄청난 전력 소모가 일어나고, 결국 각 논리게이트들은 작은 양의 전압만 받게되고... 이렇게 되면 이 쪽 로직에서 IR Drop 현상이 발생합니다.

​

이런 경우를 방지하는 것에  decap Cell을 사용할 수 있습니다.

[![DECAP Cell | Use of DeCap Cells | Placement of DeCap Cell | Layout of DeCap Cell](https://i.ytimg.com/vi/kgRM5ASg4pM/hqdefault.jpg)](https://www.youtube.com/watch?v=kgRM5ASg4pM)

설명 : What is decap cell, What is the use of decap cells in ASIC Design? We have explained all about decap cells in this session with the help of Layout of decap c...

Filler Cell:

빈공간을 채워놓는 Cell입니다. Dummy cell, Space cell이라고도 불립니다.

Physical Layout을 하면, Cell과 Cell 사이에 빈 공간이 생기게 됩니다.

제조공정 수율을위해 균일한 밀도를 위함도 있고, Hot spot effect를 피하고자 함도 있고, 전자기학적 문제를 최소화하고자 함도 있습니다.

 해시태그 : 