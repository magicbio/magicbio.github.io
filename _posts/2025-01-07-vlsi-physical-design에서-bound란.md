---
published: true
---
## VLSI Physical Design에서 Bound란?

VLSI Physical Design에서 Bounds의 개념과 활용

반도체 설계에서 타이밍, 배선 길이, 라우팅 복잡도 등을 최적화하는 것은 매우 중요합니다. 이러한 최적화를 달성하기 위해 Placement Bound라는 개념이 활용됩니다. 

​

![0](/assets/img/223686673490/0.png)

Tile base design---

Placement Bound란?

Placement Bound는 회로 설계의 Physical placement 단계에서 특정 Cell 그룹이 배치될 수 있는 영역을 제한하는 제약 조건입니다.

​

Blockage는 특정 영역에 Cell 배치를 강제적으로 막는 방법이고,

Bound는 특정 영역 안에서만 Cell 배치가 되도록 하는 방법입니다.

​

Cell 배치를 강제적으로 제한해서, 특정 위치에 특정 Cell들이 모이게 함에 있습니다.

이렇게 해서, 배선 길이를 최소화하고, Net delay를 최소화 할 수 있습니다.

예를들어 

(1) Cell들이 좌표계 여기저기에 퍼지게 되는데, 이후에 이 Cell들의 Routing 후 Timing을 보니 Net delay가 너무 커졌다고 가정합시다.

(2) Physical Design Engineer는 현재 EDA Tool 동작에 한계점을 파악하고, Net delay를 최소화 할 방법을 찾습니다.

(3) Cell 일부만 해당 영향이 있고, 충분한 공간이 있다면, 그냥 사용자가 직접 Cell을 옮길 것입니다.

만약에 Cell이 너무 많고, 충분한 공간도 없다면? Placement 단계로 다시 돌아가는 것이 방법이 됩니다.

​

그렇게 Bound를 칩니다.

Bound의 위치, 영역, cell 종류 제한에는 엔지니어가 결정합니다.

​

좀 더 자세한 내용은 아래 내용을 참조하세요.

https://www.design-reuse.com/articles/48441/bounds-in-placement.html

[Bounds in Placement](https://www.design-reuse.com/articles/48441/bounds-in-placement.html) : A placement bound is a constraint that controls the placement of groups of leaf cells and hierarchical cells. It allows us to group the cells and minimize the wire length. It helps us to place the cells at the most appropriate location.

Soft Bound와 Hard Bound

Placement Bounds는 설계의 유연성과 제약 조건 강도에 따라 크게 두 가지 유형으로 나뉩니다:

​

Soft Bound: Cell이 특정 영역에 배치되도록 설계 도구에 권장하지만, 반드시 해당 영역에 위치해야 한다는 보장은 없습니다. 예를들어 중대한 Design Rule이 있다면, 해당 Rule을 더 우선합니다.

​

Hard Bound: Cell이 반드시 지정된 경계 내에 배치되어야 하는 강제적인 제약 조건입니다.

​

그런데 이런 것들은 EDA와 Design을 잘 이해한 PD 엔지니어를 위한 기술입니다.

잘 건들면 EDA Default보다 더 좋은 결과가 나오겠지만, 초급 엔지니어는 이런거 차라리 안 하는게 나을 수도..

​

 해시태그 : 