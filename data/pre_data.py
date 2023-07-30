# -*- coding: utf-8 -*-
import os
from phonemiser import phonemise as phm

# your are at: kaldi/egs/digits/data

#change the last folder name accordingly like /train or /test whenever requires
root_path="/home/kkabikhanganba/kaldi_new/kaldi/egs/digits/digits_audio/"



all_audios=[]
all_corpus=[] #should contain both text of train and test sets
all_lexicon=[]
lexicon_lines=[]

#Switching Statements
#***********************************
print("********************provide test or train*************************")
data_set_name = input()
subset_dir_name = data_set_name+"/" #switch between "train/" and "test/"


#**************************************
#**************************************

#Checking and Flushing for rewritable files
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

if os.path.exists(subset_dir_name+"text"):
  with open (subset_dir_name+"text","w",encoding='utf-8') as output:
    pass
    print(subset_dir_name+"text was flushed..............")

if os.path.exists(subset_dir_name+"utt2spk"):
  with open (subset_dir_name+"utt2spk","w",encoding='utf-8') as output:
    pass
    print(subset_dir_name+"utt2spk was flushed..............")

if "train/" in subset_dir_name:
  with open ("local/corpus.txt","w",encoding='utf-8') as output:
    pass
    print(subset_dir_name+"local/corpus.txt was flushed..............")
  with open ("local/dict/lexicon.txt","w",encoding='utf-8') as file:
    lexicon_lines = ["!SIL SIL","<UNK> spn","SIL SIL","<Applause/> SIL","<Laugh/> SIL","<Noise/> SIL","<Overlap/> SIL","<babble/> SIL","<cough/> SIL","<music/> SIL",\
"<incomplete/> SIL","<inaudible/> SIL"]
    print("local/dict/lexicon.txt was flushed..............")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#start walking to directories and checking for audio and text files
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

for root, folds, files in os.walk(root_path + subset_dir_name):
	audio_uttr_id=[] # used in creating "text" file
	i = 0
	for aFile in files:
		if aFile.endswith(".wav"):
			audio_utterranceID = os.path.relpath(os.path.join(root,aFile),root_path+subset_dir_name)
			audio_utterranceID = audio_utterranceID.replace("/","_").replace("..wav","").replace(".wav","")
			
			audio_path = os.path.join(root,aFile)
			#audio_path = audio_path.replace("..wav",".wav")
			
			#print(audio_utterranceID)
			#print(audio_path)
			
			all_audios.append(audio_utterranceID+" "+audio_path)
			audio_uttr_id.append(audio_utterranceID)
			#i+=1
			
		
	for aFile in files:
		if aFile.endswith(".txt"):
			print("id list is",audio_utterranceID)
			
			if not os.path.exists(subset_dir_name+"text"):
				#if the file "text" does not exists, just create
				pass
				print("\"text\" file was created.........")
							
			elif not os.path.exists(subset_dir_name+"utt2spk"):
				#if the file "text" does not exists, just create
				pass
				print("\"utt2spk\" file was created.........")
							
			elif os.path.exists(subset_dir_name+"text"):
				print("reading and exporting \"c. text\" from:",aFile)
				
				currentPath=os.path.relpath(os.path.join(root),root_path+subset_dir_name)
				
				with open(os.path.join(root,aFile),"r",encoding="utf-8") as input_file:
				  #print("len of input file",len(input_file))
				  print("..............len of audio id",len(audio_uttr_id))
				
				  with open (subset_dir_name+"text","a",encoding='utf-8') as output:
				  
				    for aLine in input_file:
				      audio_id = currentPath+"_"+aLine[0:aLine.index("\t")]
				      if audio_id in audio_uttr_id:
				        output.write(audio_id+" "+phm.phonemise(aLine[aLine.index("\t")+1:-1],delimiter="")+"\n")
				        utterance = aLine[aLine.index("\t")+1:-1]
				        all_corpus.append(phm.phonemise(utterance,delimiter=""))
				        all_lexicon.append(utterance)
				      else:
				        print("text: audio id not exist",audio_id)
				  
				  with open (subset_dir_name+"utt2spk","a",encoding="utf-8") as output:
				    
				    #Reset file pointer to the beginning of the file
				    input_file.seek(0)
    				    
				    for aLine in input_file:
				      audio_id = currentPath+"_"+aLine[0:aLine.index("\t")]
				      
				      if audio_id in audio_uttr_id:
				        output.write(audio_id+" "+currentPath+"\n")
				      else:
				        print("utt2spk: audio id not exist",audio_id)
				    print(" contents were appended to utt2spk from the folder /"+currentPath)
	
			else:
				pass
		else:
			pass
	
						
			
#creating wav.scp
with open (subset_dir_name+"wav.scp","w",encoding='utf-8') as file:
	file.write("\n".join(str(element) for element in all_audios))
	print("......................",subset_dir_name+"wav.scp was created")
	
# creating local/corpus.txt
with open ("local/corpus.txt","a",encoding='utf-8') as file:
	file.write("\n".join(str(element) for element in all_corpus))
	print("......................","local/corpus.txt was created")
	
# creating unique words

words = []
words_train_set = []

# when preparing for test set, the existing lexicon of train should be read and check for duplicate
# now reading the lexicon.txt, storing all words to a list: words_train_set
words_train_set = []
if "test/" in subset_dir_name:
  with open("local/dict/lexicon.txt","r",encoding='utf-8') as file:
    lines = file.readlines()
    words_train_set = [aLine.split()[0] for aLine in lines if len(aLine.strip()) > 0]

print("words train set is------------------------------------------------------",len(words_train_set))

for aSent in all_lexicon:
  for aWord in aSent.split():
    aWord = aWord.strip()
    aWord = aWord.replace("।","").replace(",","").replace("!","")
    if (not len(aWord) == 0) and (not aWord == " ") and ("\n" not in aWord) and (aWord not in words) and (phm.phonemise(aWord,delimiter="") not in words_train_set):
      words.append(aWord)

all_lexicon = set(words)

# creating local/dict/lexicon.txt

with open ("local/dict/lexicon.txt","a",encoding='utf-8') as file:
  for element in all_lexicon:
        phonemized_delimiter_space = str(phm.phonemise(str(element), delimiter=" ")).strip()
        if not phonemized_delimiter_space:
            phonemized_delimiter_space = "SIL"
        phonemized_delimiter_empty = str(phm.phonemise(str(element), delimiter="")).strip()
        lexicon_lines.append(phonemized_delimiter_empty + " " + phonemized_delimiter_space)

  
  lexicon_lines = list(set(lexicon_lines))

    
  file.write("\n".join(lexicon_lines)+"\n")
  print("......................","local/dict/lexicon.txt was created")

	
	
	
	
	
	
	
	

