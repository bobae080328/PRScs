import pandas as pd

def convert_to_bim(input_file, output_file):
    # BIM 데이터 저장을 위한 리스트
    bim_data = []

    # 입력 파일 읽기
    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue  # 헤더 행은 무시

            fields = line.strip().split('\t')
            snp_id = fields[0]  # SNP ID (rsid 또는 internal id)
            chrom = fields[1]    # 염색체 번호
            pos = fields[2]      # 위치
            genotype = fields[3] # 유전자형

            # A1과 A2를 유전자형에서 추출
            if genotype == '--':
                a1 = 'N'  # 대립유전자 정보가 없을 경우 'N'으로 설정
                a2 = 'N'
            else:
                a1 = genotype[0] if len(genotype) > 0 else 'N'  # 첫 번째 대립유전자
                a2 = genotype[1] if len(genotype) > 1 else 'N'  # 두 번째 대립유전자

            # 염색체 번호 변환 (문자형을 정수형으로 변환)
            if chrom == 'X':
                chrom_num = 23
            elif chrom == 'Y':
                chrom_num = 24
            elif chrom == 'MT':
                chrom_num = 25
            else:
                chrom_num = int(chrom)  # 정수로 변환

            # BIM 데이터 추가 (chrom, ID, 더미값, position, A1, A2)
            bim_data.append([chrom_num, snp_id, 0, pos, a1, a2])

    # DataFrame으로 변환
    bim_df = pd.DataFrame(bim_data, columns=['chrom', 'ID', '0', 'position', 'A1', 'A2'])

    # 결과를 BIM 파일로 저장
    bim_df.to_csv(output_file, sep='\t', header=False, index=False)

convert_to_bim('/content/genome.txt', '/content/hu794D40_xym.bim')
