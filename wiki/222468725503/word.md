## Verilog RTL coding으로 Stopwatch 설계하는법 베릴로그 스톱워치 스탑워치 코드 如何使用 Verilog RTL 编码设计秒表 Verilog 秒表代码

Stopwatch code는 아래에서 다운로드 받을 수 있습니다.

https://github.com/gc-na/rtl_stop_watch

​

스탑워치의 기본 기능부터 생각해보겠습니다.

1. 시작을 하면, 시간이 흘러가야함.

2. Stop을 누르면 시간이 멈춰야함. (코드엔 ring으로 표시)

3. Record를 누르면 현재 시간이 기록되어야함.

4.시간은 시, 분, 초임. 60초가 되면 1분으로, 60분이 되면 1시간으로 전환.

5.Reset 버튼을 누르면 시간이 0으로 초기화 되어야함.

​

우선, 위와 같은 방식으로 코드를 작성하면, 아래와 같은 방식으로 프로그램을 작성할 것입니다.

```
`timescale 1ns / 1ps

module stopwatch1(
input	clk,
input reset,
input stop,
output reg ring,
output reg [5:0] sec
	 );
	 
	 always @ (posedge clk or posedge reset)
	 
		 if (reset==1)
			begin
				sec<=5'b00000;
				ring<=0;
			end	
		 else
			 begin
					if( stop!=1 )
						begin
							sec<=sec+1;
						end
					else
						begin
							ring<=1;
						end
			end

endmodule

```

클럭이 들어올 때마다 1초씩 증가하고, 리셋이 되면 시간이 초기화되고, 스탑을 누르면 시간 증가가 멈춥니다.

시, 분 개념이 없을 때는 if문이 2개 뿐이라서, 실제 회로를 설계할 때에 MUX가 2개만 있는 간단한 회로가 만들어집니다.

​

그러나 아래와 같이 시, 분, 초의 개념을 넣는다면

60초가 된다면, 60분이 된다면, xx시(본 코드에서는 12시간을 스탑워치의 최대시간으로 설정했습니다.)가 된다면 내 값은 0이 되고, 올림 수가 발생합니다.

그러면 초, 분, 시니까 총 3개의 if문이 추가가 되죠. 거기에 추가기능까지 넣으면 꽤나 길어집니다.

​

```
`timescale 1ns / 1ps

module stopwatch3(
input	clk,
input reset,
input stop,
input record,
output reg ring,
output reg [6:0] sec,
output reg [6:0] min,
output reg [4:0] hour,
output reg [6:0] rec_sec,
output reg [6:0] rec_min,
output reg [4:0] rec_hour
	 );
	 always @ (posedge clk or posedge reset)
		begin
			 if (reset==1)
				begin
					sec<=6'b000000;
					min<=6'b000000;
					hour<=4'b0000;
					ring<=0;
				end	
			 else
				 begin
						if( stop!=1 )
							begin
								sec<=sec+1;
								if (sec==60)
								begin
								min<=min+1;
								sec<=0;
								if (min==60)
									begin
									hour<=hour+1;
									if(hour==13)
										begin
										hour<=4'b0000;
										end
									end
								end
							end
						else
							begin
								ring<=1;
							end
				end
		end
		
		always @ (posedge record)
		begin
			if(reset)
			begin
				rec_sec<=0;
				rec_min<=0;
				rec_hour<=0;
			end
			else
				begin
					rec_sec<=sec;
					rec_min<=min;
					rec_hour<=hour;
				end
		end
endmodule

```

​

​

​

MUX의 수를 최소화해보고싶어서 이런저런 코드를 작성해보다가 이런 방식을 생각해봤습니다.(사진에는 minute단에 누락이 있습니다.)

클럭이 들어올때마다

real_time=real_time+1;

hour=real_time 

minute=(real_time/60)-(hour*60);

sec=real_time%60;

결론은 이 코드는 안됩니다.

```
`timescale 1ns / 1ps
module test(
input	clk,
input reset,
input stop,
output reg [6:0] sec,
output reg [6:0] min,
output reg [4:0] hour,
output reg [16:0] real_sec
	 );
	 always @ (posedge clk or posedge reset)
		begin
			 if (reset==1)
				begin
					real_sec<=16'b0000000000000000;
					sec<=6'b000000;
					min<=6'b000000;
					hour<=4'b0000;
				end	
			 else
				 begin
						if( stop!=1 )
							begin
								real_sec<=real_sec+1;
								hour <= real_sec / 3600;
								min <= (real_sec / 60) - (hour * 60);
								sec <= real_sec % 60;
							end
				end
		end
		
endmodule

```

​

Operator is only supported when the second operand is a power of 2 와 같은 오류가 나타납니다.

내용은.... 2^n의 연산만 연산자에 쓸 수 있다는 거에요.(비트연산만으로 할 수 있는 계산식만 가능해요.)

그래서 60, 3600같은 수를 연산하고싶으면 전용 연산 블락(가산기, 감산기, 곱셈기, 나눗셈기 등을)을 만들어줘야합니다!

 해시태그 : 