---
published: true
---
## LVS란? Layout versus Schematic란? ASIC Flow에서 DRC란?

LVS란?

LVS, 즉 Layout versus Schematic는 Layout vs Schematic입니다. Physical Design의 후반 단계에서 진행합니다.

아래 그림처럼, Layout과 Schematic을 비교하는게 LVS라고 보시면 됩니다.

![0](/assets/img/223386321077/0.png)

여기서 Layout은 "공정을 위해 만든 물리적 설계도"

Schematic은 "물리적 설계를 위한 논리적 설계도"라고 이해하시면 대강 맞습니다.

Digital Circuit을 예로 들면, Verilog style의 "Code"를 GDS나 Oasis같은 "Code"와 비교하는 Code2Code verification입니다.

Place&Route Tool에서는 이렇게 Net Route를 하여도 "문제없다!"라고 판단했는데, 실제 공정사 Design rule에서는 이정도 좁은 간격으로는 Net을 연결 할 수 없고... 결국 Design Rule Check에서 위배되어 Short로 판단 될 수도 있습니다. 결국 LVS Fail로 만들어지구요.

​

결론은, Physical Design에 사용되는 EDA가 항상 완벽하게 설계되는 것은 아닙니다.

그러므로 Tape out 이전에 설계가 제대로 되었는지 검증하는 "LVS" 과정이 꼭 필요합니다.

​

이런 작업들이 VLSI의 시대로 오면서, 하나의 칩에 수백 수천억개의 트랜지스터가 들어가니, 인간이 하나 하나 비교 할 수 없는 수준이 되었습니다. 이런 비교 작업은 EDA라는 SW Tool을 이용합니다. (Synopsys의 ICV 같은 Tool을 사용합니다. SIEMENS의 Calibre, Cadence의 Virtuoso)

​

아래 캡쳐본에서 13번째에 진행됩니다.

![1](/assets/img/223386321077/1.png)

​

아래 같은 인풋 파일을 갖고

Layout GDS(oasis)

Schematic netlist

Rule

LVS Script 등등 input file 등.

​

아래 같은 내부 흐름으로 진행됩니다. 자세한건 Synopsys ICV Userguide를 참조하세요~

​

LVS 자체의 내부 흐름을 살펴보려고 합니다.

LVS Flow

아래 그림을 기반으로 LVS 프로세스의 각 단계에 대해 자세히 살펴보겠습니다.

![2](/assets/img/223386321077/2.png)

DesignReuse1. Extraction in LVS

반도체 회로를 구성하는 데 사용되는 다양한 Layer와 Shape에 대한 자세한 정보가 포함된 Design file들을 처리하고, 물리적 설계도와 논리적 설계도를 읽고 표현합니다.

​

2. Reduction in LVS

스케매틱과 레이아웃의 본질적인 특성을 유지하면서 단순화 합니다. 중복을 분석하고, 앞으로 있을 Compare 작업을 최적화하기 위한 작업입니다.

​

3. Comparation in LVS

LVS의 마지막 단계에서는 추출된 Layout을 Schematic과 비교하여 동등성을 검증합니다. 

​

LVS에서 자주 보이는 Result Database

Open

Shorts

Missing components

Missing global net connect

​

​

정리하면,  LVS Tool은 Full Chip design에서 실제 Device의 Shape을 Foundry의 Design Rule 기준으로 물리적 검증을 완벽하게 파악하여, 논리적 설계도와 물리적 설계도의 기능이 일치하는가를 분석합니다.

​

좀 더 이론적으로 자세히 보실 분들을 위해 아래 영상을 첨부합니다. 3시간 정도 영상입니다.

https://www.youtube.com/watch?v=Hq6QD8aX2Q0&list=PLZU5hLL_713xp5sDexQMVdOM86l_wP5w8&index=1

[![Digital-on-top Physical Verification (Fullchip LVS/DRC) - Part 1](https://i.ytimg.com/vi/Hq6QD8aX2Q0/hqdefault.jpg)](https://www.youtube.com/watch?v=Hq6QD8aX2Q0&list=PLZU5hLL_713xp5sDexQMVdOM86l_wP5w8&index=1)

설명 : This is a 6-part lecture series on how to run physical verification, i.e., LVS and DRC, on a block created with a digital implementation flow (place and rout...

​

 해시태그 : 