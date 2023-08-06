
transliterator(){

    # first argument
    local ascii_phonemic="$1"

    # using sed command to perform string replacement based on regex
    # command substitution syntax of bash
    # sed : stream editor
    # -E : extended regular expression
    # s : search and replace
    # g : global replacement (all occurrences)
    # RULE: s/pattern/replacement/flags
    
    # input string consists of patterns which are overlapping each other
    # so the string is divided as super_set and sub_set (devanagari) to parse
    # first the super_set is parsed and then the returned string is reparsed as sub_set
     
    # super set $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    local super_set=$(echo "$ascii_phonemic" | sed -E 's/\|k/क़्/g;
    s/\|K/ख़्/g; s/\|g/ग़्/g; s/\|j/ज़्/g; s/\|x/ड़्/g; s/\|X/ढ़्/g; s/`a/ऍ/g; s/RR/_ॄ/g; s/eː/_े/g; s/oː/_ो/g; s/Oː/_ौ/g; s/n~/ँ/g')

    # subset **********************************************************************************************************************
    local devanagari=$(echo "$super_set" | sed -E 's/k/क्/g; s/K/ख्/g;
    s/g/ग्/g; s/G/घ्/g; s/w/ङ्/g; s/c/च्/g; s/C/छ्/g; s/j/ज्/g; s/J/झ्/g; s/Y/ञ्/g; s/q/ट्/g;
    s/V/ठ्/g; s/x/ड्/g; s/X/ढ्/g; s/N/ण्/g; s/t/त्/g; s/T/थ्/g; s/d/द्/g; s/D/ध्/g; s/n/न्/g;
    s/p/प्/g; s/P/फ्/g; s/b/ब्/g; s/B/भ्/g; s/m/म्/g; s/y/य्/g; s/r/र्/g; s/l/ल्/g; s/`L/ळ्/g; s/\|L/\|ल्/g;
    s/v/व्/g; s/z/श्/g; s/S/ष्/g; s/s/स्/g; s/h/ह्/g; s/H/ः/g; s/M/ं/g; s/O/\|औ/g; s/a/अ/g; s/Aː/_ा/g;
    s/\|A/\|आ/g; s/i/_ि/g; s/Iː/_ी/g; s/u/_ु/g; s/Uː/_ू/g; s/R/_ृ/g; s/e/_ॆ/g;
    s/Eː/_ै/g; s/\|E/\|ऐ/g; s/o/_ॊ/g; s/्अ//g; s/्_//g')
    
    # post processing =============================================================================================================
    local postProcessed=$(echo "$devanagari" | sed -E 's/_ा/आ/g;
    s/_ि/इ/g; s/_ी/ई/g; s/_ु/उ/g; s/_ू/ऊ/g; s/_ृ/ऋ/g; s/_ॆ/ऎ/g;
    s/_ै/ऐ/g; s/_ॊ/ऒ/g; s/_ॄ/ॠ/g; s/_े/ए/g; s/_ो/ओ/g; s/_ौ/औ/g;')

    # retrun the stirng finally ********************************
    echo "$postProcessed"
}

#my_input_string="nRpaH latAːmapi akSAːmyat . kaKa|K"

# declar file name
#myFile="../exp/tri1/decode_test/scoring_kaldi/test_filt.txt"

# read file
#asciiText=$(cat "$myFile")

# call transliterator to transliterate
#transliterated=$(transliterator "$asciiText")

# export the file
#echo "$transliterated" > "myOutput.txt"

#echo "$transliterated"

#echo "my source text $my_input_string"
#echo "my output $transliterated"






