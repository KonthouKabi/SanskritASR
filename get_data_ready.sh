echo "============= getting data ready ==============="
cd data
echo "==================== dataset name: train"
python pre_data.py
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
