---
published: true
---
## 파일의 입출력 과정은 정확히 어떤식으로 되는걸까? fclose를 해야하는 이유? OS, Kernel, assemby, 컴퓨터구조 개념에서 설명.

파일의 입출력 과정이 일어나기까지 컴퓨터, OS에선 어떤 일이 일어나고 있는지에 대해서 설명하고자 본 페이지를 작성합니다.

이 글에서는 PC에서 가장 널리 쓰이고있는 Intel/AMD core 기반으로 설명합니다. 언어는 C언어,  x86-64 gcc, intel 어셈블리어로 설명 할 예정입니다.

ARM, RISC-V 등 어떤 ISA로 하냐에 따라 Instruction은 달라질 수 있습니다.

​

x86-64 구조를 간단히 요약하면 아래 본문과 같습니다.

![20](/assets/img/223103111793/20.png)

x86은 CISC ISA를 가짐.

데이터 이동 (Data Movement): MOV, PUSH, POP, LEA 등

산술 연산 (Arithmetic): ADD, SUB, MUL, DIV, INC, DEC 등

논리 연산 (Logic): AND, OR, XOR, NOT, TEST 등

비교와 분기 (Comparison and Branching): CMP, JMP, JE, JNE, JZ, JG 등

반복문 (Looping): LOOP, FOR, WHILE 등

스택 조작 (Stack Manipulation): PUSH, POP, CALL, RET 등

데이터 변환 (Data Conversion): MOVZX, MOVSX, CVTSI2SD, CVTSD2SI 등

비트 조작 (Bit Manipulation): AND, OR, XOR, SHL, SHR 등

입출력 (Input/Output): IN, OUT, INT 등

부동 소수점 연산 (Floating-Point Operations): FADD, FMUL, FDIV, FCOM 등

벡터 연산 (Vector Operations): SIMD 명령어 (SSE, AVX 등)를 통한 벡터 연산 지원

메모리 접근 (Memory Access): LOAD, STORE, MOVSB, MOVSX 등

자세한건 Manual을 참고하시면 됩니다.

https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-2a-manual.html?wapkw=processor-identification-cpuid-instruction

[Intel® 64 and IA-32 Architectures Developer's Manual: Vol. 2A](https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-2a-manual.html?wapkw=processor-identification-cpuid-instruction) : Architectures Software Developer's Manual: Intel® 64 and IA-32, Vol. 2A: instruction set reference, A-M

​

2. word는 Memory에 Littel-endian  byte order를 따름.

3. SIMD

4. Immediate addressing offsets와 immediate data는 8bit(-128~127)로 표현 가능. -> 대부분의 명령어 길이는 2~3byte

5. 사용되는 register는 아래와 같습니다. 이 레지스터들은 프로그램 실행 중 데이터의 저장 및 조작을 위해 사용됩니다. 

![21](/assets/img/223103111793/21.png)

RBP (Base Pointer):

RBP는 "Base Pointer"를 의미하며, 함수 프레임에 대한 포인터로 사용됩니다. 함수 내에서 로컬 변수 및 매개변수에 접근하기 위해 필요한 정보를 담고 있습니다.

​

RSP (Stack Pointer):

RSP는 "Stack Pointer"를 나타내며, 스택의 최상위 주소를 가리킵니다. 함수 호출 및 복귀, 로컬 변수 및 임시 데이터의 저장 등 스택 기반 작업에 사용됩니다.

​

ESI (Extended Source Index):

ESI는 "Extended Source Index"를 의미하며, 데이터 블록 복사, 문자열 조작, 배열 인덱싱 등에서 소스 인덱스로 활용됩니다.

​

EDI (Extended Destination Index):

EDI는 "Extended Destination Index"를 나타내며, 데이터 블록 복사, 문자열 조작, 배열 인덱싱 등에서 대상 인덱스로 사용됩니다.

​

RAX (Accumulator):

RAX는 "Accumulator"를 의미합니다. 주로 산술 및 논리 연산의 결과를 저장하는 데 사용되며, 함수 호출 시 반환 값이 저장되기도 합니다.

​

RCX:

RCX는 함수 호출 시 매개변수의 전달에 사용되거나 루프 카운터로 활용될 수 있는 레지스터입니다.

​

EDX:

EDX는 산술 및 논리 연산에 사용되거나 I/O 작업에서 데이터 포인터로 사용될 수 있는 x86 아키텍처의 레지스터입니다.

​

​

​

간단한 C언어 script를 작성해보겠습니다.

​

아래 스크립트는 

1. test.txt라는 파일을 write mode로 열고

2. pFile이라는 포인터 변수에 저장 후

3. pFile을 닫기

하는 간단한 예제입니다.

```
#include<stdio.h>
int main(void)
{
    FILE* pFile = fopen("test.txt", "w"); //write mode
    fprintf(pFile, "Chase");        //printf -> fprintf
    fclose(pFile);
    return 0;
}

```

​

이걸 x86-64 gcc, intel asm형태로 Compile하면 아래와 같은 어셈블리어로 출력됩니다.

​

```
.LC0:
        .string "w"
.LC1:
        .string "test.txt"
.LC2:
        .string "Chase"
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     esi, OFFSET FLAT:.LC0
        mov     edi, OFFSET FLAT:.LC1
        call    fopen
        mov     QWORD PTR [rbp-8], rax
        mov     rax, QWORD PTR [rbp-8]
        mov     rcx, rax
        mov     edx, 10
        mov     esi, 1
        mov     edi, OFFSET FLAT:.LC2
        call    fwrite
        mov     rax, QWORD PTR [rbp-8]
        mov     rdi, rax
        call    fclose
        mov     eax, 0
        leave
        ret
```

Label

라벨은 코드 내에서 문자열 데이터, 특정 위치를 참조/식별하기 위한 이름입니다.

.LC0, .LC1, .LC2:

이 세 줄은 문자열을 저장하는 부분입니다. 코드에서는 "w", "test.txt", "Chase"라는 세 가지 문자열이 사용됩니다. 이들은 데이터 영역에 저장되어 프로그램이 필요할 때 참조됩니다.

​

main 함수:

파일 입출력 작업은 main 함수에서 이루어집니다. main 함수는 프로그램의 시작점이며, 실행되는 동안 여러 작업을 수행합니다. 코드의 첫 부분에서는 함수 프롤로그로서 스택 프레임을 설정합니다.

​

push

operand의 내용을 Stack에 Push

rbp rsp 등은 위에서 register 설명할 때 했으니 skip하겠습니다.

​

​

mov

mov reg, 값 : reg를 값으로 덮어씌움

mov reg, reg : 첫번째 reg를 두번째 reg 값으로 덮어씌움, 단 두 레지스터의 크기가 같아야 한다.

​

call

프로시저 호출. 현재 위치를 스택에 push 하고 jmp한다는 점에서 단순 jmp 와 다르다. call된 위치에서 ret를 실행하면 스택에서 주소를 꺼내와 call한 다음 위치부터 시작

​

ret

호출된 함수에서 호출한 함수로 복귀

​

fopen

이 코드에서는 fopen 함수를 호출하여 파일을 엽니다. fopen 함수는 OS에게 파일을 열도록 요청합니다. 그리고 OS는 해당 파일을 찾아 열고, 파일을 가리키는 파일 포인터를 반환합니다. 이 포인터는 rax 레지스터에 저장됩니다.

​

fwrite

fwrite 함수는 파일에 데이터를 씁니다. 이 코드에서는 문자열을 파일에 쓰기 위해 fwrite 함수를 호출합니다. fwrite 함수는 운영 체제에게 데이터를 쓰도록 요청하며, 운영 체제는 이를 실제 파일에 기록합니다.

​

fclose

파일 작업이 완료되면 fclose 함수를 호출하여 파일을 닫습니다. 파일을 닫으면 운영 체제는 해당 파일에 대한 자원을 해제하고, 이후 다른 프로세스나 사용자가 해당 파일에 접근할 수 있도록 합니다.

​

​

​

fopen~fclose까지의 과정을 OS 측면에서 좀 더 자세히 알아보겠습니다.

​

![22](/assets/img/223103111793/22.png)

​

​

1. 사용자 프로그램에서 fopen 함수 호출:

사용자 프로그램은 fopen 함수를 호출하여 파일을 엽니다. 함수 호출 시 파일 이름과 모드 등의 매개변수를 전달합니다.

​

​

2. fopen system call 처리 및 UI -> Kenel로 전환:

fopen 함수는 내부적으로 시스템 호출을 사용하여 커널 내부로 진입합니다. 이를 위해 사용자 프로그램은 커널의 system call을 사용하기 위해 커널 모드로 전환됩니다.

system call address와 함께 프로그램의 실행이 운영 체제의 커널로 진입합니다.

x86에서는 "software interrupt" 혹은 "System call"이라고도 불리는 명령어들을 사용하여 커널모드로 전환됩니다.

​

UI -> Kernel 로의 전환을 요청하면, CPU는 현재 실행 중인 프로세스의 상태를 저장하고, 커널 모드에서 실행될 때 필요한 초기화된 레지스터 및 스택 등의 정보를 설정합니다. 그런 다음, CPU는 커널의 시작 주소로 분기하여 커널 코드의 실행을 시작합니다.

​

이렇게 전환되면 프로그램은 커널의 권한 아래에서 실행되며, 커널은 하드웨어 및 시스템 자원에 대한 직접적인 접근 및 제어를 할 수 있습니다. 커널은 시스템 호출을 통해 사용자 프로그램이 필요로 하는 서비스를 제공하고, 필요한 작업을 수행합니다. 작업이 완료되면, 커널은 다시 UI mode로 전환하여 사용자 프로그램에 return 값을 보낼겁니다.

​

3. system call 처리:

system call은 커널 내부에서 처리됩니다. 커널은 시스템 호출 번호에 해당하는 처리기를 실행하여 요청된 작업을 수행합니다. 파일 열기를 위해 open 시스템 호출이 호출됩니다.

​

4. 파일 시스템 검색:

open 시스템 호출은 전달된 파일 이름을 기반으로 파일 시스템에서 해당 파일을 검색합니다. 파일 시스템은 파일 시스템 트리를 통해 파일을 찾는 작업을 수행합니다.

​

5.1 파일 접근 권한 확인:

파일 시스템은 검색된 파일의 접근 권한을 확인합니다. 파일이 존재하지 않거나 접근 권한이 없는 경우, open 시스템 호출은 실패를 반환할 수 있습니다.

​

5.2 파일 시스템에서 파일을 성공적으로 찾고, 접근 권한이 허용된다면 파일을 엽니다.

​

6. 파일에 대한 메타데이터(크기, 위치 등)를 유지하고, 파일에 대한 작업을 수행할 수 있는 파일 디스크립터(파일 포인터)를 생성 후, open system call은 file description을 return하여 사용자 프로그램에게 전달합니다.

​

7. 커널 모드 종료 및 사용자 모드 전환:

open 시스템 호출 처리가 완료되면, 커널은 사용자 프로그램에게 제어를 반환하고 사용자 모드로 전환됩니다. 이후 사용자 프로그램은 반환된 파일 디스크립터를 사용하여 파일 작업을 수행할 수 있습니다.

​

8. 파일 작업 수행:

사용자 프로그램은 반환된 파일 디스크립터를 사용하여 파일에 대한 작업을 수행합니다. 예를 들어, 읽기, 쓰기, 위치 이동 등의 작업을 수행할 수 있습니다.

​

9. fclose 함수 호출:

파일 작업이 완료되면, 사용자 프로그램은 fclose 함수를 호출하여 파일을 닫을 수 있습니다. fclose 함수는 내부적으로 close 시스템 호출을 사용하여 파일을 닫습니다.

​

10. 파일 닫기:

close 시스템 호출은 파일 디스크립터를 전달받아 해당 파일을 닫습니다. 파일 닫기는 커널 내부에서 수행되며, 파일과 관련된 자원을 정리하고 파일 디스크립터를 반환합니다.

​

11. 커널 모드 종료 및 사용자 모드 전환:

close 시스템 호출 처리가 완료되면, 커널은 사용자 프로그램에게 제어를 반환하고 사용자 모드로 전환됩니다.

​

이와 같이, 리눅스에서 fopen 함수는 커널을 통해 파일을 열고 닫습니다. 사용자 프로그램은 fopen 함수를 호출하여 파일 작업을 요청하고, 해당 요청은 커널 내부의 시스템 호출을 통해 처리됩니다. 커널은 파일 시스템과 상호작용하여 파일을 검색하고 열고 닫는 등의 작업을 수행하며, 사용자 프로그램은 반환된 파일 디스크립터를 사용하여 파일 작업을 수행할 수 있습니다.

​

fopen을 했으면 fclose를 해야 하는 이유?

fopen을 하면 Stream memory인 buffer에 디스크립터(포인터) 정보를 쓴다고 했습니다.

fclose를 하면 이 디스크립터를 비우는.. fflush 과정이 있습니다.

​

fclose를 하지 않았고, OS도 이걸 fflush하지 않은 경우엔.. 이 디스크립터가 비워지지 않습니다.

fclose하지 않은상태로 프로세스들이 늘어나면, 결국 fopen 가용한 자리가 줄어들게 됩니다.

​

만약 fclose 안 한 상태로 데이터들이 쌓이면, Too many open files error가 발생 할 수도 있습니다.

OS에 따라 이런게 충돌이 나서 기존 데이터에 영향이 있을 수도 있지만... 보통 최신 OS에서는 그런건 Bug로 보기에 그런 경우는 잘 안 일어납니다.

Windows는 process간 배타적으로 유지하기에, fclose되지 않은 경우, 파일을 삭제하거나 수정하지 못하게 되어있구요.

​

![23](/assets/img/223103111793/23.png)

위 그림은 리눅스 커널 맵입니다. 운영체제론 시간 때 배웠던 것 같은데 기억이 하나도 안 나네요...ㅎㅎ 역시 휴먼 메모리는 volatile.... 한 때 SW 엔지니어를 꿈꿨는데..

​

​

​

다시 어셈블리로 돌아와서,

leave, ret

코드의 마지막 부분에서는 leave와 ret 명령어를 사용하여 함수를 종료합니다. leave 명령어는 함수의 프롤로그에서 설정한 스택 프레임을 복원하고, ret 명령어는 호출자로 돌아가는 역할을 합니다. 이를 통해 main 함수의 실행이 종료되고, 프로그램은 이후에 정의된 작업을 계속 수행하거나 종료됩니다.

​

요약하면, 파일 입출력 작업은 코드에서 fopen, fwrite, fclose 함수 호출을 통해 이루어지며, 운영 체제는 커널을 통해 실제 파일을 열고 데이터를 기록하고 닫는 작업을 수행합니다. 컴퓨터 구조는 이러한 작업을 위해 레지스터와 스택을 사용하여 함수 호출과 데이터 처리를 하드웨어 레벨에서 관리합니다.

 해시태그 : 