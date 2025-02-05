import os
import re
from datetime import datetime, timedelta

# 특수문자 제거 및 공백 "-" 변환 함수
def sanitize_title(title):
    title = title.strip()  # 앞뒤 공백 제거
    title = re.sub(r"[^\w가-힣\s-]", "", title)  # 한글, 영어, 숫자, 공백, "-"만 유지
    title = re.sub(r"\s+", "-", title)  # 공백을 "-"로 변환
    title = title[:50]  # 제목이 너무 길면 50자까지 제한
    return title.lower()  # 소문자로 변환 (옵션)

# 첫 번째 `##` 헤더를 추출하는 함수
def extract_title_from_md(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^##\s+(.+)", line.strip())  # `## 제목` 형식 찾기
            if match:
                return match.group(1)  # `## ` 이후의 제목만 반환
    return None  # 제목을 찾지 못한 경우

# 현재 디렉토리 내의 모든 .md 파일 가져오기
files = [f for f in os.listdir() if re.match(r"\d{4}-\d{1,2}-\d{1,2}-\d+\.md", f)]

# 파일을 글번호(숫자) 기준으로 정렬
files.sort(key=lambda x: int(re.search(r"-(\d+)\.md", x).group(1)), reverse=True)

# 기준 날짜 설정 (최신 글이 2025-02-02)
base_date = datetime(2025, 2, 2)

# 파일 이름 변경
for i, file in enumerate(files):
    # 새로운 날짜 계산
    new_date = base_date - timedelta(days=i)

    # 기존 글번호 추출
    match = re.search(r"-(\d+)\.md", file)
    if not match:
        continue
    post_number = match.group(1)

    # 첫 번째 `##` 헤더에서 제목 가져오기
    title = extract_title_from_md(file)
    
    # 제목이 없으면 기본값 사용
    if not title:
        title = f"untitled-{post_number}"

    # 파일명 변환
    clean_title = sanitize_title(title)
    new_filename = f"{new_date.strftime('%Y-%m-%d')}-{clean_title}.md"

    # 파일 이름 변경
    os.rename(file, new_filename)
    print(f"{file} -> {new_filename}")
