import os

def is_target_file(file_path):
    """파일이 지정된 내용만 포함하는지 확인"""
    target_content = """---
published: true
---"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
        return content == target_content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def delete_target_files():
    """현재 디렉토리에서 조건에 맞는 파일 삭제"""
    for file_name in os.listdir():
        if file_name.endswith(".md") and os.path.isfile(file_name):
            if is_target_file(file_name):
                try:
                    os.remove(file_name)
                    print(f"Deleted: {file_name}")
                except Exception as e:
                    print(f"Error deleting {file_name}: {e}")

if __name__ == "__main__":
    delete_target_files()
