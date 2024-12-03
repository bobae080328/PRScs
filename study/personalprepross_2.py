import pandas as pd
import gzip

def convert_23andme_to_plink(input_file, output_prefix):
    # 데이터 저장을 위한 리스트
    bim_data = []
    fam_data = []
    bed_data = bytearray()

    # 입력 파일 읽기
    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            fields = line.strip().split('\t')
            chrom = fields[1]

            # X, Y, MT 염색체 제외
            if chrom not in map(str, range(1, 23)):
                continue

            snp_id = fields[0]
            pos = fields[2]
            genotype = fields[3]

            # BIM 데이터 추가
            ref_allele = genotype[0]
            alt_allele = genotype[1] if genotype[0] != genotype[1] else '0'
            bim_data.append([chrom, snp_id, '0', pos, ref_allele, alt_allele])

            # BED 데이터 추가
            if genotype == '--':
                bed_data.append(0)  # 00 (missing)
            elif genotype[0] == genotype[1]:
                bed_data.append(3)  # 11 (homozygous for second allele)
            else:
                bed_data.append(2)  # 10 (heterozygous)

    # FAM 파일 데이터 (단일 샘플)
    fam_data = ['FAM001', 'ID001', '0', '0', '2', '-9']  # 여성, 표현형 미상

    # BIM 파일 저장
    pd.DataFrame(bim_data, columns=['CHR', 'SNP', 'CM', 'BP', 'A1', 'A2']).to_csv(f'{output_prefix}.bim', sep='\t', index=False, header=False)

    # FAM 파일 저장
    pd.DataFrame([fam_data], columns=['FID', 'IID', 'PAT', 'MAT', 'SEX', 'PHENOTYPE']).to_csv(f'{output_prefix}.fam', sep='\t', index=False, header=False)

    # BED 파일 저장
    with open(f'{output_prefix}.bed', 'wb') as f:
        f.write(bytes([108, 27, 1]))  # 매직 넘버
        f.write(bytes(bed_data))

convert_23andme_to_plink('genome.txt', 'plink_output')
