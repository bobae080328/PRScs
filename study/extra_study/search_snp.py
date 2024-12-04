import pandas as pd

# 검색할 문자열을 포함한 txt 파일 읽기
with open('/content/drive/MyDrive/ColabNotebooks/PRScs_code/search_strings.txt', 'r') as f:
    search_strings = [line.strip() for line in f]

# genome.txt 파일 읽기
df = pd.read_csv('/content/drive/MyDrive/ColabNotebooks/PRScs_code/genome.txt', sep='\t', comment='#', header=None, 
                 names=['rsid', 'chromosome', 'position', 'genotype'],on_bad_lines='skip')

# 각 열에 대해 검사
for column in df.columns:
    # 열의 모든 값을 문자열로 변환
    column_values = df[column].astype(str)
    
    # 모든 검색 문자열에 대해 확인
    if any(column_values.str.contains('|'.join(search_strings))):
        print(f"'{column}' 열에서 검색 문자열이 발견되었습니다.")
        
        # 검색 문자열이 포함된 행만 필터링
        matched_rows = df[column_values.str.contains('|'.join(search_strings))]
        
        # 해당 열의 값들 출력
        print(f"{column} 열의 일치하는 값들:")
        print(matched_rows.to_string(index=False))
        print("\n")  # 가독성을 위한 빈 줄 추가
