import os
import re
import datetime

def rename_md_files():
    # 현재 디렉토리의 모든 *.md 파일 목록 가져오기
    md_files = [f for f in os.listdir('.') if re.match(r'^\d+\.md$', f)]
    
    if not md_files:
        print("No matching .md files found.")
        return
    
    # 파일 이름에서 숫자 추출 후 정렬
    numbers = sorted([int(re.match(r'^(\d+)\.md$', f).group(1)) for f in md_files])
    
    # 오늘 날짜 및 3일 전 날짜 계산
    today = datetime.date.today()
    three_days_ago = today - datetime.timedelta(days=3)
    
    # 가장 큰 숫자 파일은 오늘 날짜로, 나머지는 3일 전 날짜로 변경
    for i, num in enumerate(numbers):
        new_date = today if i == len(numbers) - 1 else three_days_ago
        new_filename = f"{new_date.year}-{new_date.month}-{new_date.day}-{num}.md"
        
        old_filename = f"{num}.md"
        os.rename(old_filename, new_filename)
        print(f"Renamed: {old_filename} -> {new_filename}")

if __name__ == "__main__":
    rename_md_files()

