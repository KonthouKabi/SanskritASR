# -*- coding: utf-8 -*-
import re

class phonemise:

  def phonemise(text,delimiter):
    #----------------------------------------- pre processing --------------------------------------------------
  
    text = text.replace("फ़","फ़").replace("०","शून्यम्").replace("१","एकम्").replace("२","द्वे").replace("३","त्रिणि").replace("४","चत्वारि").\
    replace("५","पञ्च").replace("६","षट्").replace("७","सप्त").replace("८","अष्ट").replace("९","नव").replace("0","शून्यम्").replace("1","एकम्").replace("2","द्वे").replace("3","त्रिणि").replace("4","चत्वारि").\
    replace("5","पञ्च").replace("6","षट्").replace("7","सप्त").replace("8","अष्ट").replace("9","नव").replace("ड़","ड़").replace("ॐ","ओम्").replace("य़्","ॺ्").replace("`","").replace("_स","स").replace("_न","न")\
    .replace("अङु्गलीयके","अङ्गुलीयके").replace("ध्रुवस~ग्कल्पेन","ध्रुवसंकल्पेन").replace("\u200c","").replace("\u200d","")
    
    #-------------- phoeme dictionary ---------------------
    
    dictionary = {
    "क़": "|ka",
    "ख़": "|Ka",
    "ग़": "|ga",
    "ज़": "|ja",
    "ड़": "|xa",
    "फ़": "fa",
    "ढ़": "|Xa",
    "क": "ka",
    "ख": "Ka",
    "ग": "ga",
    "घ": "Ga",
    "ङ": "wa",
    "ह": "ha",
    "च": "ca",
    "|च": "|ca",
    "छ": "Ca",
    "ज": "ja",
    "झ": "Ja",
    "य": "ya",
    "ञ": "Ya",
    "ट": "qa",
    "ठ": "Va",
    "ड": "xa",
    "ढ": "Xa",
    "ण": "Na",
    "ष": "Sa",
    "र": "ra",
    "त": "ta",
    "थ": "Ta",
    "द": "da",
    "ध": "Da",
    "न": "na",
    "ल": "la",
    "ळ": "`La",
    "|ल": "|La",
    "प": "pa",
    "फ": "Pa",
    "ब": "ba",
    "भ": "Ba",
    "म": "ma",
    "श": "za",
    "स": "sa",
    "व": "va",
    "|व": "|va",
    "ॺ": "|ya",
    "अ": "a",
    "आ": "Aː",
    "|आ": "|A",
    "इ": "i",
    "ई": "I:",
    "उ": "u",
    "ऊ": "Uː",
    "ऋ":"R",
    "ॠ":"RR",
    "ए": "eː",
    "ऎ": "e",
    "ऐ": "Eː",
    "|ऐ": "|E",
    "ँ": "n~",
    "ं": "M",
    "ः":"H",
    "ओ": "oː",
    "ऒ": "o",
    "औ": "Oː",
    "|औ": "|o",
    "ऑ": "|e",
    "ॲ": "`a",
    "ऍ": "`a",
    "[ओ": "$",
    "र्र्": "rr",
    "ऽ": "$",
    "ा": "<_>Aː",
    "ि": "<_>i",
    "ी": "<_>I:",
    "ु": "<_>u",
    "ू": "<_>Uː",
    "ृ":"<_>R",
    "ॄ":"<_>RR",
    "े": "<_>eː",
    "ै":"<_>Eː",
    "ॆ": "<_>e",
    "ो": "<_>oː",
    "ॊ": "<_>o",
    "ौ": "<_>Oː",
    "ॉ": "<_>|o",
    "ॅ": "<_>`a"
    }
    
    pattern1 = "\|च|\|ल|\|व|\|आ|\|औ|\[ओ|र्र|\|ऐ"

    pattern2 = "क़|ख़|ग़|ज़|ड़|फ़|ढ़|क|ख|ग|घ|ङ|ह|च|छ|ज|झ|य|ञ|ट|ठ|ड|ढ|ण|ष|र|त|थ|द|ध|न|ल|ळ|प|फ|ब|भ|म|श|स|व|ॺ|ऐ|ँ|ं|ः|अ|आ|इ|ई|उ|ऊ|ए|ऎ|ओ|ऒ|औ|ऑ|ॲ|ऍ|ऋ|ॠ|ऽ|ा|ि|ी|ु|ू|े|ै|ॆ|ो|ॊ|ौ|ॉ|ॅ|ृ|ॄ"

    # matching for exceptions
    mappedString = ""
    start = 0
    for aMatched in re.finditer(r""+pattern1,text):
      end, newStart = aMatched.span()
      mappedString += text[start:end]
      aPhone = aMatched.group()
      mappedString += dictionary[aPhone]+delimiter
      start = newStart
    
    mappedString += text[start:]
    
    second_level = ""
    # matchi for regular patterns
    start = 0
    for aMatched in re.finditer(r""+pattern2,mappedString):
      end, newStart = aMatched.span()
      second_level += mappedString[start:end]
      aPhone = aMatched.group()
      second_level += dictionary[aPhone]+delimiter
      start = newStart
    
    second_level += mappedString[start:]
    
    # -------------------------------------post processing --------------------------------------------
    if " " in delimiter:
      second_level = second_level.replace("a <_>"," a<_>").replace("a ्"," a् ").replace("  "," ").replace("a "," a ").replace("-","- ")\
      .replace(":",": ").replace("_ ","_ ").replace("  "," ")
    second_level = second_level.replace("a<_>","").replace("a्","").replace("।",".").replace("  "," ")
    return second_level
    
    
    
    
    
    
    
    
       
