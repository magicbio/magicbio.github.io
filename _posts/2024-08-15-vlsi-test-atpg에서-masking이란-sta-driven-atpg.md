---
published: true
---
## VLSI Test: ATPG에서 Masking이란? STA Driven ATPG

양산 과제를 하면 보통 ATE 장비를 이용하여 칩 테스팅을 합니다.

​

ATE 장비라 하면 아래 장비 같은 것을 떠올리시면 됩니다. Teradyne 장비가 유명합니다.

![1](/assets/img/223316519530/1.png)

디지털 회로를 기준으로 설명하면,

디지털 논리 회로 설계 -> 공정 라이브러리를 통한 합성 -> DFT & ATPG -> P&R -> STA -> Tape-out 이런 흐름으로 진행 됩니다.

​

DFT는 "Function 구현만 되어있는 Chip에, 높은 Test coverage로 테스팅이 가능하도록 설계를 한다"고 보시면 대략 맞겠습니다.

ATPG는 Chip Test를 할 때 ATE 장비에 넣는 Vector를 생성하는 방법론입니다.

​

![2](/assets/img/223316519530/2.png)

​

ATE 장비에 넣고 테스트를 한다는게, Chip의 Input port에 어떤 값을 넣었을 때 어떤 값이 Output port에 나와야 Pass Chip이라는건데요. 그러려면 Test하는 동작 모드에서도 Timing close를 해야합니다.

근데 Test 동작 모드에 Timing close를 하다가 Mission(원래 칩의 동작) mode에 나쁜 영향을 줘서 둘 중 하나를 포기해야 하는 경우가 있는데요.

​

이런 경우에, Test mode에서 특정 path의 coverage를 포기하고(이 쪽에 벡터 생성을 제한함) 이 부분의 Test mode에서 timing path를 false_path로 사용하는 방법들이 있습니다.

​

대표적인게 add_capture_mask입니다. (STA에서 사용하는 Synopsys Design Constraints처럼.. ATPG에서 사용하는 Constraints라고 보셔도 됩니다. 가능하면 사용하지 않아야합니다. 이 부분을 Chip testing시에 체크를 못하거든요.)

![3](/assets/img/223316519530/3.png)

만약에 Test mode에서 Timing close를 안 하고 ATPG를 했다? -> 이거 ATPG상에서는 문제 없는 것처럼 나옵니다. ATPG Tool들은 DRC만 따지거든요.

그러나 실제 ATE Test 할 때 Pass chip들도 Fail로 나오는 불상사가 펼쳐집니다.

​

ATPG는 말 그대로 Automatic Test Pattern Generation입니다.

(1) Model을 build하고, DRC Check하고, Pattern generation하는거에요. ATPG Tool에는 STA엔진이 들어있지 않습니다. STA 결과에서 Timing violation 있으면, 이 쪽 벡터를 생성하지 않도록 만들어야 하는데, 대표적인 방법이 마스킹인거구요.

(2)  벡터 생성이 기본입니다. ATPG는 넷리스트를 수정하지 않아요. Mask Tape Out 된 후에 벡터를 생성해도 Chip Testing 가능합니다.

​

![4](/assets/img/223316519530/4.png)

​

근데 DFT, ATPG가 정~말 까다로운 이유 중 몇가지가,

1) DFT 하나만으로도 Chip이 정말 커지고 Congestion이 심해지며 IR Drop도 자주 발생하고,

2) STA가 Sign-off 되고 GDS Freeze 되었을 때는 이미 MTO 일정에 바짝 다가와 있습니다. 이 때 Test Coverage를 Target에 도달하지 못한다?

-> 칩테스팅 단계에서 불량 걸러낼 확률이 낮아지는겁니다. 이런 칩을 자율주행, 방산, 의료용에 쓸 수 있을까요?

3) 만약에 Test coverage를 도달 했지만, ATE 장비에서 모든 웨이퍼가 Fail Chip이라고 결과를 내렸다고 합시다. "이런 경우면, Test pattern이 잘못된건지? 진짜 전부 다 Fail인건지?" 이 고민을 해야하고.. 이러는 사이에 값비싼 TAT가 날아갑니다. 칩 테스팅 회사들은 미리 날짜 예약 주문을 받기 때문에, 뒤늦게 예약하면 한참 뒤에야 내 차례가 옵니다.

​

그래서, 

(1) spyglass 등.. RTL Level에서 DFT coverage 예상치를 미리 보고

(2) 안 나올 부분들 미리 Test Point Insetion

(3) 패턴 만들었으면, chip 나오기 전에 DTA. Dynamic Timing Analysis. 그러니까 Vector timing simulation을 해야합니다.

​

칩 나오면 DTA Pass한 패턴으로 넣구요.

​

1) STA에서 완벽히 Timing close를 하는걸 1번 목표로 하고,

2) ATE 장비에서 Fail이 나오더라도 빠른 디버깅을 할 수 있도록, 칩 나오기 전에 DTA도 수행해야합니다.

 해시태그 : 