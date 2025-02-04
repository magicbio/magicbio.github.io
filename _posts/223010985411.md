## CTS를 잘 하려면 어떻게? CTS 이후 Violation이 너무 크다면

이전에 설명했던 것처럼, Logical Synthesis에서 Timing을 기가막히게 잡았더라도, P&R, CTS에서 Timing 틀어지면 처음부터 다시해야 할 수도 있고.. 그런 경우도 많기에,

​

Logical Synthesis -> Pre CTS Timing Check -> Physical Synthesis -> Post CTS Timing check를 해야한다.

​

CTS 한번에 Skew를 완벽히 맞추는건 매우 어렵다.

2022년에 출시된 iPhone 14 pro의 Processor인 A16 Bionic은 약 1600만 Transistor count인데... 이 Logic gate들을 Timing constraints 고려해서 P&R하고.. CTS도 해야한다면... 너무 많은 경우의 수들이 있어 Resource를 엄청나게 사용한다.

​

​

​

​

​

​

Physical Design을 3단계로만 나누면, Floor plan -> P&R -> CTS 순서로 가는데, Chip이 작을 수록 경제적이기 때문에 오밀조밀하게 FP, P&R 할 수밖에 없다.

그러면 CTS를 좁은 곳에서 해야하는데, 일부 Routing들의 길이가 길면, Latency가 길어질거고.. 모든 Sink pin들이 이 Latency를 맞추려면 Clock buffer (Inverter pair)가 엄청 들어가야하는데, 이러면 DRC 문제가 야기된다.

그러면 결국 Floor Plan부터 다시 하던가 P&R에서부터... 거의 사람이 직접 CTS를 해야하는 상황이 올 수 있다. 

그런 일들을 최소화하려면 어떻게 해야할까?

​

​

이전에 쓴 것처럼, Floor plan을 잘 하는게 중요하다.

잘하는 엔지니어들은 안 되는걸 미리 안 된다라고 빨리 말하고 스펙 변경을 한다. 사이즈를 좀 더 키우든지 뺄 기능을 빼든지.

​

그래서 Floor plan을 잘하고, 안 되는건 안 된다 이걸 말하려면?

Synthesis -> PRE STA -> P&R -> CTS -> POST STA 이 Trial CTS를 빨리 해보는 수 밖에 없다.

Trial CTS turn에서 DRC 문제되는 지점이 어디고, CTS Skew 어디가 크게 틀어졌고, OCC를 어디에 배치하고, OCC Member를 어떻게 바운드치고... 어떤 그룹을 특별히 관리해야하고, Floor plan 어떻게해야하고.. 이걸 빨리 봐야한다.

​

그리고 Function clock으로만 CTS 돌리는게 아니라, IJTAG, BIST, SCAN 등 다양한 clock으로 CTS를 하기에

Synthesis & DFT Tool에서 CTS 고려해서 '잘' 해야 한다. 안 그러면 타 Mode의 CTS랑 충돌 날 수 있다. 이런건 POST-GLS에선 쉽고 느리게 발견된다. STA에서도 발견 할 수 있긴한데, 이러면 SDC랑 STA를 '잘' 해야 함.

​

​

​

​

​

​

​

​

POST STA 결과를 보니 일부 Path만 CTS가 잘 안되었다면,

Latency 비슷한 근처 Clock path를 따다 붙이거나,

clock path의 일부 cell들을 지우거나 추가하거나,

CDC나 Timing budgeting 같은 기법을 쓰거나... 이정도만 떠오르네요. 또 뭐가 있으려나? 

​

​

이 장에선 Timing constraint를 만족하기 위한 CTS만 작성했는데, Low power를위한 CTS는 나중에 정리해야겠다.

 해시태그 : 