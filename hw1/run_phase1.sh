#/bin/bash

mkdir $2
mkdir tmp_dir

#word2vec
python word2vec.py --train_data=$1 --save_path=tmp

python filterVocab/filterVocab.py filterVocab/fullVocab.txt < tmp_dir/tmp_word2vec.txt > $2/filter_word2vec.txt

#glove

python glove.py $1 

python filterVocab/filterVocab.py filterVocab/fullVocab.txt < tmp_dir/tmp_glove.txt > $2/filter_glove.txt

rm -r tmp_dir -f 
