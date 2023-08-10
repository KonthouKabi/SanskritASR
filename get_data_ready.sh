#!/bin/bash
echo "============= getting data ready ==============="
cd data
echo "==================== dataset name: train"
source /home/kkabikhanganba/miniforge3/etc/profile.d/conda.sh
conda activate kabi || exit 1
python pre_data.py || exit 1
echo
echo "==================== dataset name: test"
python pre_data.py
cd ..
echo
sort -o data/train/utt2spk data/train/utt2spk 
sort -o data/train/spk2utt data/train/spk2utt
sort -o data/train/text data/train/text 
sort -o data/train/wav.scp data/train/wav.scp 
utils/validate_data_dir.sh data/train
echo
echo "====================== FIXING DATASET ========================"
echo
echo "fixing train dataset --------------------------------------------"
utils/fix_data_dir.sh data/train
echo "fixing test dataset --------------------------------------------"
utils/fix_data_dir.sh data/test
