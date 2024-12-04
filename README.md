# 테스트 결과
## 사용데이터
1. reference : UK Biobank AMR data (Common Allele)

2. GWAS data : ADHD Dataset - ieu-a-1183 (from ieu open gwas project)

3. validation data (from 23andMe public genetic data)

Public Profile -- hu794D40

[Public profile url](https://my.pgp-hms.org/profile/hu794D40)


## 실행 결과
FID     IID  PHENO    CNT   CNT2 SCORESUM

FAM001   ID001     -9 101328  50664 0.013033

#### 결과의 의미
1. PHENO = -9 : 표현형에 대한 정보. 특별한 표현형 정보가 없음을 의미
2. CNT = 101328 : 계산에 사용된 총 SNP의 갯수
3. CNT2 = 50664 : 계산에 사용된 Effect Allele 의 갯수
4. SCORESUM = 0.0130331 : 최종 PRS 점수

#### PRS 점수
PRS 함수는 표준 정규분포 (평균 0, 표준편차 1) 을 따르는 확률밀도함수의 확률값으로 나타남

즉, 데이터를 비교한 결과 개인 Allele들 중 ADHD RISK 에 대한 확률 합은 약 0.013 표준편차 정도 = 백분위기준 약 50.5%

평균보다는 약간 높지만 크게 위험있는 수준은 아님

(환자는 실제 ADHD 진단을 받고, Vyvanse 를 복용한 적이 있음 / 현재까지 복용여부는 알 수 없음)



# 추가 탐구
#### ADHD RISK SNP 관련 논문 서치
Discovery of the first genome-wide significant risk loci for attention deficit/hyperactivity disorder, ADHD Group of PGC, et al, 2019-1, Nature Genetics

Transcriptome-wide association study of attention deficit hyperactivity disorder identifies associated genes and phenotypes, Liao, et al, 2019, Nature Communication

등의 논문에서 찾은 Allele 목록은 다음과 같다.

[search_string.txt](study/extra_study/search_strings.txt)

#### 원본 genome.txt 파일에서 찾기
[실행파일](study/extra_study/search_snp.py)

#### 결과
```
rsid chromosome position genotype
rs11210892 1 44100084 AG
```
rs11210892 Allele은 G>A 인데 genotype 이 A/G인것으로 보아 Heterozygous로 보인다.

여러 논문에서 해당 Allele이 위치한 유전자는 DLPFC(dorsolateral prefrontal cortex, 전전두피질)에 관계된 유전자라고 말하고 있다.

```
FMRI data showed that the risk allele “G” of rs11210892 was associated with an increased activation
within the right dorsolateral prefrontal cortex(Sample III) and the bilateral striatum (Sample IV).
We conclude that rs11210892 is significantly associated with working memory and its neural underpinnings,
so the genes near this SNP might be potential gene targets for treating cognitive impairment associated with schizophrenia.
(Effects of Trans-ancestry Schizophrenia Risk Gene Polymorphisms on Working Memory and Underlying Brain Mechanisms, Yanyan Su, et al, 2021, Schizophrenia Bulletin)
```
```
Among the 23 SNP loci of ADHD children, no mutation was detected in 6 loci, and 2 loci did not conform to Hardy-Weinberg equilibrium.
Of the remaining 15 loci, there were 9 SNPs, rs2652511 (SLC6A3 locus), rs1410739 (OBI1-AS1 locus), rs3768046 (TIE1 locus),
rs223508 (MANBA locus), rs2906457 (ST3GAL3 locus), rs4916723 (LINC00461 locus), rs9677504 (SPAG16 locus), rs1427829 (intron) and rs11210892 (intron),
correlated with the severity of clinical symptoms of ADHD.
Specifically, rs1410739 (OBI1-AS1 locus) was found to simultaneously affect conduct problems,
control ability and abstract thinking ability of children with ADHD.
(Correlation research of susceptibility single nucleotide polymorphisms and the severity of clinical symptoms in attention deficit hyperactivity disorder, Xu, et al, 2022, Front. Psychiatry)
```
#### 결론
ADHD는 전두엽의 도파민 등의 부족으로 추정되는 문제가 야기시킨 실행기능 부족으로인해 주의력부족, 충동조절 어려움 등을 호소하는 뇌신경발달장애이다. 따라서, 한개의 SNP 결과만으로 결론내기는 어렵겠지만, 전전두피질과 관련된 유전자의 변이의 발견과 ADHD 발병의 상관관계를 생각해볼 수는 있겠다.









# [이하 README.md]

## PRS-CS

**PRS-CS** is a Python based command line tool that infers posterior SNP effect sizes under continuous shrinkage (CS) priors
using GWAS summary statistics and an external LD reference panel.

- Details of the development and evaluation of PRS-CS are described in: \
  T Ge, CY Chen, Y Ni, YCA Feng, JW Smoller. Polygenic Prediction via Bayesian Regression and Continuous Shrinkage Priors. *Nature Communications*, 10:1776, 2019.

- An extension of PRS-CS to PRS-CSx for cross-population polygenic prediction is available at https://github.com/getian107/PRScsx and described in: \
  Y Ruan, YF Lin, YCA Feng, CY Chen, M Lam, Z Guo, Stanley Global Asia Initiatives, L He, A Sawa, AR Martin, S Qin, H Huang, T Ge. Improving polygenic prediction in ancestrally diverse populations. *Nature Genetics*, 54:573-580, 2022.

- A review of the methods and best practices for cross-ancestry polygenic prediction is available at: \
  L Kachuri, N Chatterjee, J Hirbo, DJ Schaid, I Martin, IJ Kullo, EE Kenny, B Pasaniuc, JS Witte, T Ge. Principles and methods for transferring polygenic risk scores across global populations. *Nature Reviews Genetics*, 25:8-25, 2024.


#### Version History

**May 14, 2024**: Replaced some scipy functions with numpy due to changes in the latest scipy version.

**Apr 9, 2024**: Allowed for the output of all posterior samples, which can be used to estimate the uncertainty of individualized PRS.

🔴
**Aug 10, 2023**: Added BETA/OR + SE as a new input format (see the format of GWAS summary statistics below), which is now the recommended input data. When using BETA/OR + P as the input, p-values smaller than 1e-323 are truncated, which may reduce the prediction accuracy for traits that have highly significant loci.

**Aug 10, 2023**: Allowed for the output of variant-specific shrinkage estimates.

**Nov 3, 2022**: Import random module from numpy instead of scipy.

**Jun 4, 2021**: Expanded reference panels to five populations.

**May 26, 2021**: Added suggestions for limiting the number of threads in scipy when running PRS-CS (see Computational Efficiency section below).

**Apr 6, 2021**: Added projection of the LD matrix to its nearest non-negative definite matrix.

**Mar 4, 2021**: LD reference panels constructed using the UK Biobank data are now available. 

**Jan 4, 2021**: Improved the accuracy and robustness of random sampling from the generalized inverse Gaussian distribution. Prediction accuracy will probably slightly improve over previous versions.

**Sept 10, 2020**: Fixed a bug in strand flip when there are non-ATGC alleles (e.g., indels) in the GWAS summary statistics. Previous versions erroneously remove variants that can be matched across GWAS summary statistics, the reference panel and the validation bim file via strand flip, which reduces the number of SNPs used in prediction and may slightly affect prediction accuracy. 

**Apr 24, 2020**: Accounted for a rare ZeroDivisionError in MCMC sampling.

**Apr 20, 2020**: Added non-ATGC allele check.

**Apr 11, 2020**: Added strand flip check.

**Mar 25, 2020**: Minor changes to make the software Python 2 and 3 compatible.

**Oct 20, 2019**: Added `--seed`, which can be used to seed the random number generator using a non-negative integer.

**Jun 6, 2019**: Fixed a bug in `--beta_std`. If you explicitly specified `--beta_std=False`, the output was actually standardized beta (in contrast to desired per-allele beta) and we recommend rerunning the analysis. If you left `--beta_std` as default or used `--beta_std=True`, the results were not affected.


#### Getting Started

- Clone this repository using the following git command:
   
    `git clone https://github.com/getian107/PRScs.git`

    Alternatively, download the source files from the github website (`https://github.com/getian107/PRScs`)

- Download the LD reference panels and extract files:

    LD reference panels constructed using the 1000 Genomes Project phase 3 samples:
    
     [AFR reference](https://www.dropbox.com/s/mq94h1q9uuhun1h/ldblk_1kg_afr.tar.gz?dl=0 "AFR reference") (~4.44G);
     `tar -zxvf ldblk_1kg_afr.tar.gz`
     
     [AMR reference](https://www.dropbox.com/s/uv5ydr4uv528lca/ldblk_1kg_amr.tar.gz?dl=0 "AMR reference") (~3.84G);
     `tar -zxvf ldblk_1kg_amr.tar.gz`
        
     [EAS reference](https://www.dropbox.com/s/7ek4lwwf2b7f749/ldblk_1kg_eas.tar.gz?dl=0 "EAS reference") (~4.33G);
     `tar -zxvf ldblk_1kg_eas.tar.gz`
        
     [EUR reference](https://www.dropbox.com/s/mt6var0z96vb6fv/ldblk_1kg_eur.tar.gz?dl=0 "EUR reference") (~4.56G);
     `tar -zxvf ldblk_1kg_eur.tar.gz`
     
     [SAS reference](https://www.dropbox.com/s/hsm0qwgyixswdcv/ldblk_1kg_sas.tar.gz?dl=0 "SAS reference") (~5.60G);
     `tar -zxvf ldblk_1kg_sas.tar.gz`
    
    LD reference panels constructed using the UK Biobank data ([Notes](https://www.dropbox.com/s/y3hsc15kwjxwjtd/UKBB_ref.txt?dl=0 "Notes")):
    
     [AFR reference](https://www.dropbox.com/s/dtccsidwlb6pbtv/ldblk_ukbb_afr.tar.gz?dl=0 "AFR reference") (~4.93G);
     `tar -zxvf ldblk_ukbb_afr.tar.gz`
     
     [AMR reference](https://www.dropbox.com/s/y7ruj364buprkl6/ldblk_ukbb_amr.tar.gz?dl=0 "AMR reference") (~4.10G);
     `tar -zxvf ldblk_ukbb_amr.tar.gz`
    
     [EAS reference](https://www.dropbox.com/s/fz0y3tb9kayw8oq/ldblk_ukbb_eas.tar.gz?dl=0 "EAS reference") (~5.80G);
     `tar -zxvf ldblk_ukbb_eas.tar.gz`
    
     [EUR reference](https://www.dropbox.com/s/t9opx2ty6ucrpib/ldblk_ukbb_eur.tar.gz?dl=0 "EUR reference") (~6.25G);
     `tar -zxvf ldblk_ukbb_eur.tar.gz`
    
     [SAS reference](https://www.dropbox.com/s/nto6gdajq8qfhh0/ldblk_ukbb_sas.tar.gz?dl=0 "SAS reference") (~7.37G);
     `tar -zxvf ldblk_ukbb_sas.tar.gz`
     
    For regions that don't have access to Dropbox, reference panels can be downloaded from the
    [alternative download site](https://personal.broadinstitute.org/hhuang//public//PRS-CSx/Reference).

- PRScs requires Python packages **scipy** (https://www.scipy.org/) and **h5py** (https://www.h5py.org/) installed.
 
- Once Python and its dependencies have been installed, running

    `./PRScs.py --help` or `./PRScs.py -h`

    will print a list of command-line options.


#### Using PRS-CS

`
python PRScs.py --ref_dir=PATH_TO_REFERENCE --bim_prefix=VALIDATION_BIM_PREFIX --sst_file=SUM_STATS_FILE --n_gwas=GWAS_SAMPLE_SIZE --out_dir=OUTPUT_DIR [--a=PARAM_A --b=PARAM_B --phi=PARAM_PHI --n_iter=MCMC_ITERATIONS --n_burnin=MCMC_BURNIN --thin=MCMC_THINNING_FACTOR --chrom=CHROM --beta_std=BETA_STD --write_psi=WRITE_PSI --write_pst=WRITE_POSTERIOR_SAMPLES --seed=SEED]
`
 - PATH_TO_REFERENCE (required): Full path (including folder name) to the directory that contains information on the LD reference panel (the snpinfo file and hdf5 files). If the 1000 Genomes reference panel is used, folder name would be `ldblk_1kg_afr`, `ldblk_1kg_amr`, `ldblk_1kg_eas`, `ldblk_1kg_eur` or `ldblk_1kg_sas`; if the UK Biobank reference panel is used, folder name would be `ldblk_ukbb_afr`, `ldblk_ukbb_amr`, `ldblk_ukbb_eas`, `ldblk_ukbb_eur` or `ldblk_ukbb_sas`. Note that the reference panel should match the ancestry of the GWAS sample (not the target sample).

 - VALIDATION_BIM_PREFIX (required): Full path and the prefix of the bim file for the target (validation/testing) dataset. This file is used to provide a list of SNPs that are available in the target dataset.

 - SUM_STATS_FILE (required): Full path and the file name of the GWAS summary statistics. The summary statistics file must include either BETA/OR + SE or BETA/OR + P. When using BETA/OR + SE as the input, the file must have the following format (including the header line):

```
    SNP          A1   A2   BETA      SE
    rs4970383    C    A    -0.0064   0.0090
    rs4475691    C    T    -0.0145   0.0094
    rs13302982   A    G    -0.0232   0.0199
    ...
```
Or:
```
    SNP          A1   A2   OR        SE
    rs4970383    A    C    0.9825    0.0314                 
    rs4475691    T    C    0.9436    0.0319
    rs13302982   A    G    1.1337    0.0543
    ...
```
where SNP is the rs ID, A1 is the effect allele, A2 is the alternative allele, BETA/OR is the effect/odds ratio of the A1 allele, SE is the standard error of the effect. Note that when OR is used, SE corresponds to the standard error of logOR.

When using BETA/OR + P as the input, the file must have the following format (including the header line):

```
    SNP          A1   A2   BETA      P
    rs4970383    C    A    -0.0064   0.4778
    rs4475691    C    T    -0.0145   0.1245
    rs13302982   A    G    -0.0232   0.2429
    ...
```
Or:
```
    SNP          A1   A2   OR        P
    rs4970383    A    C    0.9825    0.5737                 
    rs4475691    T    C    0.9436    0.0691
    rs13302982   A    G    1.1337    0.0209
    ...
```
where SNP is the rs ID, A1 is the effect allele, A2 is the alternative allele, BETA/OR is the effect/odds ratio of the A1 allele, P is the p-value of the effect. Here, a standardized effect size is calculated using the p-value while BETA/OR is only used to determine the direction of an association. Therefore if z-scores or even +1/-1 indicating effect directions are presented in the BETA column, the algorithm should still work properly.

 - GWAS_SAMPLE_SIZE (required): Sample size of the GWAS.

 - OUTPUT_DIR (required): Output directory and output filename prefix of the posterior effect size estimates.

 - PARAM_A (optional): Parameter a in the gamma-gamma prior. Default is 1.

 - PARAM_B (optional): Parameter b in the gamma-gamma prior. Default is 0.5.

 - PARAM_PHI (optional): Global shrinkage parameter phi. If phi is not specified, it will be learnt from the data using a fully Bayesian approach. This usually works well for polygenic traits with large GWAS sample sizes (hundreds of thousands of subjects). For GWAS with limited sample sizes (including most of the current disease GWAS), fixing phi to 1e-2 (for highly polygenic traits) or 1e-4 (for less polygenic traits), or doing a small-scale grid search (e.g., phi=1e-6, 1e-4, 1e-2, 1) to find the optimal phi value in the validation dataset often improves perdictive performance.

 - MCMC_ITERATIONS (optional): Total number of MCMC iterations. Default is 1,000.

 - MCMC_BURNIN (optional): Number of burnin iterations. Default is 500.

 - MCMC_THINNING_FACTOR (optional): Thinning factor of the Markov chain. Default is 5.

 - CHROM (optional): The chromosome(s) on which the model is fitted, separated by comma, e.g., `--chrom=1,3,5`. Parallel computation for the 22 autosomes is recommended. Default is iterating through 22 autosomes (can be time-consuming).

- BETA_STD (optional): If True, return standardized posterior SNP effect sizes (i.e., effect sizes corresponding to standardized genotypes with zero mean and unit variance across subjects). If False, return per-allele posterior SNP effect sizes, calculated by properly weighting the posterior standardized effect sizes using allele frequencies estimated from the reference panel. Default is False.

- WRITE_PSI (optional): If True, write variant-specific shrinkage estimates. Default is False.

- WRITE_POSTERIOR_SAMPLES (optional): If True, write all posterior samples of SNP effect sizes after thinning. Default is False.

- SEED (optional): Non-negative integer which seeds the random number generator.


#### Output

PRS-CS writes posterior SNP effect size estimates for each chromosome to the user-specified directory. The output file contains chromosome, rs ID, base position, A1, A2 and posterior effect size estimate for each SNP. An individual-level polygenic score can be produced by concatenating output files from all chromosomes and then using `PLINK`'s `--score` command (https://www.cog-genomics.org/plink/1.9/score). If polygenic scores are generated by chromosome, use the 'sum' modifier so that they can be combined into a genome-wide score.


## Computational Efficiency

PRS-CS relies on numpy packages, which automatically use all available cores on a compute node. This can be problematic when running PRS-CS on a compute cluster; PRS-CS jobs may interfere with other jobs running on the same node, reducing computational efficiency. To resolve this issue, including the following code in the script to specify the number of threads in scipy:

```
export MKL_NUM_THREADS=$N_THREADS
export NUMEXPR_NUM_THREADS=$N_THREADS
export OMP_NUM_THREADS=$N_THREADS
```
For example, to use a single thread for the computation, set `N_THREADS=1`.


#### Test Data

The test data contains GWAS summary statistics and a bim file for 1,000 SNPs on chromosome 22.
An example to use the test data:

`
python PRScs.py --ref_dir=path_to_ref/ldblk_1kg_eur --bim_prefix=path_to_bim/test --sst_file=path_to_sumstats/sumstats_se.txt --n_gwas=200000 --chrom=22 --phi=1e-2 --out_dir=path_to_output/eur
`


#### Support

Please direct questions or bug reports to Tian Ge (tge1@mgh.harvard.edu).


