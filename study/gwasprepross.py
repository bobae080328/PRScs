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

parse_vcf_to_gwas('/my_test_data/ieu-a-1183_2.vcf', 'output_gwas_adhd2.txt')
