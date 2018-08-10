# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:29:34 2018

@author: evgen
"""

from tools.general import *
from definitions.Definition import *
from definitions.url_Parse import *
from data import *
import spacy


def OpenJson(Jfile):
    result = []
    with open(Jfile) as f:
        d = json.load(f)
    for key in d.keys():
        key = key.replace(" ","_")
        result.append(key)
    return result

def Create_URL_List(ToAppend):
    result = []
    for line in ToAppend:
        line = 'https://groupprops.subwiki.org/w/index.php?title=' + line + '&action=edit'
        result.append(line)
    return result

OUTPUT_DIR = 'data'

create_dir(OUTPUT_DIR)

#url = 'https://groupprops.subwiki.org/w/index.php?title=(2,3,7)-triangle_group&action=edit'
#url = 'https://groupprops.subwiki.org/w/index.php?title=1-automorphism-invariant_subgroup&action=edit'
#string = url_Parse(url)
#
#test = Define(string.string)
#
#
#tags = test.all_tags_pos
#
#formulas = test.all_formulas
##print(formulas[0])
#text = test.tags_removed
##print(text)
#sentences = test.tokenized 
#sentence = test.tokenized

#result = OpenJson('data\\SubWiki.json')

filename1 = "All Sentences.txt"
filename2 = "Defenitions with URL.txt"
filename3 = "Defenitions.txt"

all_Sentences = open(filename1,"w")
definition_url = open(filename2, "w")
definition = open(filename3, "w")

res = Create_URL_List(OpenJson('data\\SubWiki.json'))
#res = Create_URL_List(OpenJson('data\\SubWikiRead.json'))

#strng = url_Parse(res[0])
#test = Define(strng.string)
#sentences = test.tokenized
#doc = nlp(sentences)
#sen = [sent.string.strip() for sent in doc.sents]
#for line in sen:
#    all_Sentences.write(line)
#    all_Sentences.write("\n")
#all_Sentences.write(res[0])
#all_Sentences.close()

for line in res:
    strng = url_Parse(line)
    test = Define(strng.string)
    sentences = test.tokenized
    doc = nlp(sentences)
    sen = [sent.string.strip() for sent in doc.sents]
    all_Sentences.write(str(res.index(line)+1) + '\n')
    definition_url.write(str(res.index(line)+1) + '\n')
    for sentence in sen:
        
        all_Sentences.write(sentence)
        all_Sentences.write("\n")
#    all_Sentences.write("".join(sen)+'\n'+ line)    
#    all_Sentences.write("\n")
    all_Sentences.write(line + '\n')
    definition_url.write(sen[0] + '\n' + line + '\n')
    definition.write(sen[0] + '\n')

all_Sentences.close()
definition_url.close()
definition.close()

    
    
    
    