#!/bin/bash

# 깃허브에서 PRScs 코드 가져오기
git clone https://github.com/getian107/PRScs.git

cd PRScs



# scipy와 h5py 설치
pip install scipy h5py


# plink 설치
wget http://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20201019.zip
!unzip plink_linux_x86_64_20201019.zip

chmod +x plink


# GWAS 파일 전처리
python /study/gwasprepross.py



# 23andMe public genetic data 다운로드
wget --mirror --no-parent --no-host --cut-dirs=1 'https://f117bf2e5dd0945429c1b77666420704-200.collections.ac2it.arvadosapi.com/_/'


# 23andMe data는 txt 파일이기 때문에 bim 파일로 변환
python /study/personalprepross.py
