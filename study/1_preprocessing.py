# 깃허브에서 PRScs 코드 가져오기
!git clone https://github.com/getian107/PRScs.git

!cd PRScs

!pip install scipy h5py


# plink 설치
!wget http://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20201019.zip
!unzip plink_linux_x86_64_20201019.zip

!chmod +x plink


# GWAS 파일 전처리
import pandas as pd

def parse_vcf_to_gwas(vcf_file, output_file):
    gwas_data = []
    with open(vcf_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            chrom = fields[0]
            pos = fields[1]
            snp_id = fields[2]
            ref = fields[3]
            alt = fields[4]
            info = fields[7]
            format_fields = fields[8].split(':')
            values = fields[9].split(':')

            es_index = format_fields.index('ES')
            lp_index = format_fields.index('LP')

            beta = float(values[es_index])
            p_value = 10 ** (-float(values[lp_index]))

            gwas_data.append([snp_id, ref, alt, beta, p_value])

    df = pd.DataFrame(gwas_data, columns=['SNP', 'A1', 'A2', 'BETA', 'P'])
    df.to_csv(output_file, sep='\t', index=False)

parse_vcf_to_gwas('/content/drive/MyDrive/ieu-a-1183_2.vcf', 'output_gwas_adhd2.txt')



# 23andMe public genetic data 다운로드
! wget --mirror --no-parent --no-host --cut-dirs=1 'https://f117bf2e5dd0945429c1b77666420704-200.collections.ac2it.arvadosapi.com/_/'


# 23andMe data는 txt 파일이기 때문에 bim 파일로 변환
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
