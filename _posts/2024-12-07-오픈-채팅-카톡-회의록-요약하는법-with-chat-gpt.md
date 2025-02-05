---
published: true
---
## 오픈 채팅, 카톡, 회의록 요약하는법 with Chat GPT

혹시 잘 안되거나 이해 안 되시면 말씀해주세요!

​

1.카톡 들어가서 대화방의 메뉴 누르고, -> 대화내용 -> 대화 내보내기

![0](/assets/img/223607412470/0.png)

이 파일을 원하는 경로에 저장하세요.

저는

C:\Users\user-1\Desktop\ 위치에

파일 이름 Kakaotalk.txt로 저장하였습니다.

​

그래서 제 파일 경로는 C:\Users\user-1\Desktop\Kakaotalk.txt 입니다.

​

잘 모르겠으면, 대충 아무대나 저장하고, 파일 우클릭으로 누르면 "경로로 복사"가 있다. 이거 하면 경로가 복사 됨.

![1](/assets/img/223607412470/1.png)

​

2. Python 설치. 다운로드 누르고 기본 설정대로 설치해도 됨.

https://www.python.org/downloads/

[Download Python](https://www.python.org/downloads/) : The official home of the Python Programming Language

![2](/assets/img/223607412470/2.png)

3. 아래 코드를 복사하고 메모장에 저장하기.

```
import re
import os

def split_chat_by_date_and_length(file_path, output_dir, max_chars=4000):
    # 날짜 패턴 정의 (예: 2024년 7월 9일 화요일)
    date_pattern = r"--------------- (\d{4}년 \d{1,2}월 \d{1,2}일 .요일) ---------------"
    
    # 텍스트 파일을 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_data = file.read()
    
    # 날짜별로 대화 로그 분리
    split_data = re.split(date_pattern, chat_data)

    # 디렉터리가 존재하지 않으면 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 불필요한 패턴 정의 (입장 메시지, 나간 메시지, 내보낸 메시지, 인사말 등)
    remove_patterns = [
        r'.*님이 들어왔습니다\.',               # 입장 메시지
        r'.*님이 나갔습니다\.',                 # 나간 메시지
        r'.*님을 내보냈습니다\.',               # 내보낸 메시지
        r'\[오픈채팅봇\].*',                    # 오픈채팅봇 메시지
        r'\*.*강퇴입니다.*',                    # 강퇴 관련 메시지
        r'안녕하세요.*',                        # 인사말 ("안녕하세요" 패턴 제거)
        r'반갑습니다.*',                        # "반갑습니다" 패턴 제거
        r'아이디 변경.*',                      # "아이디 변경" 관련 메시지 제거
        r'잘 부탁드립니다.*',                   # "잘 부탁드립니다" 패턴 제거
        r'.*\b감사합니다\b.*',                  # 감사 인사 제거
        r'화이팅입니다~*',                      # 화이팅 응원 메시지 제거
        r'ㅎㅎ|ㅋ+|\^\^|ㅋㅋ',                    # "ㅎㅎ", "ㅋ"와 같은 감탄사 제거
    ]
    
    # 첫 번째 부분은 날짜가 아닌 내용일 수 있으니 건너뛰고, 날짜와 그에 대응하는 대화 내용을 매칭
    for i in range(1, len(split_data), 2):
        date = split_data[i]
        chat_log = split_data[i + 1].strip()

        # 불필요한 정보 제거
        for pattern in remove_patterns:
            chat_log = re.sub(pattern, '', chat_log).strip()

        # 닉네임과 시간 정보 제거
        chat_log = re.sub(r'\[.*?\] ', '', chat_log).strip()

        # 빈 줄 제거
        chat_log = re.sub(r'\n+', '\n', chat_log).strip()

        # 날짜에서 파일 이름으로 사용할 수 있도록 포맷 변환 (예: 2024-07-09)
        date_for_filename = re.sub(r"[^\w\s요일]", '-', date).strip()  # 한글 요일을 남겨두고 처리
        date_for_filename = re.sub(r"년 |월 |일 ", '-', date_for_filename).strip()

        # 4000글자씩 분할하여 저장, 40,000글자를 초과하는 경우 10개의 파일로 제한
        if len(chat_log) > 40000:
            max_parts = 10
            split_length = len(chat_log) // max_parts
            for j in range(max_parts):
                part = chat_log[j * split_length:(j + 1) * split_length].strip()
                if part:  # 내용이 있을 때만 저장
                    part_number = j + 1
                    file_name = f"{date_for_filename}_part{part_number}.txt"
                    output_file_path = os.path.join(output_dir, file_name)
                    
                    # 파일로 저장
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(part)
                    
                    print(f"Saved chat part {part_number} for {date} to {output_file_path}")
        else:
            for j in range(0, len(chat_log), max_chars):
                part = chat_log[j:j + max_chars].strip()
                if part:  # 내용이 있을 때만 저장
                    part_number = j // max_chars + 1
                    file_name = f"{date_for_filename}_part{part_number}.txt"
                    output_file_path = os.path.join(output_dir, file_name)
                    
                    # 파일로 저장
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(part)
                    
                    print(f"Saved chat part {part_number} for {date} to {output_file_path}")

# 예시 사용법
file_path = r'C:\Users\user-1\Desktop\KakaoTalk.txt'  # 여기에 채팅방 텍스트파일을 넣으세요.
output_dir = r'C:\Users\user-1\Desktop\TEST'  # 결과 파일을 저장할 폴더
split_chat_by_date_and_length(file_path, output_dir) 
```

여기서 file_path랑 output_dir만 본인이 알맞게 수정해도 되고 그대로 냅둬도 됩니다.

이 텍스트 파일 이름은 하고싶은거로 지으세요. .py로만 끝나게 해주세요. 저는 split_chat_log.py로 지었습니다.

​

4. 저장하시면 아래처럼 뜨는데, 이거 더블클릭하면 실행됩니다.

![3](/assets/img/223607412470/3.png)

그러면 output_dir 위치. C:\Users\user-1\Desktop\TEST에 전처리된 파일이 저장됩니다.

​

이런식으로 날짜별로 저장됩니다. part를 나눈 이유는, GPT가 4000자까지 인식률이 높고, 한번에 받을 수 있는 파일이 최대 10개이기 때문입니다.

![4](/assets/img/223607412470/4.png)

5. GPT한테 이런식으로 파일 넣고, 쿼리를 넣으세요. 편하신대로 하시면 됩니다.

![5](/assets/img/223607412470/5.png)

​

그러면... 이런식으로 요약본을 받을 수 있습니다!

![6](/assets/img/223607412470/6.png)

​

 해시태그 : 