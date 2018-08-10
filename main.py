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
##url = 'https://groupprops.subwiki.org/w/index.php?title=Subgroup_with_abelianization_of_maximum_order&action=edit'
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

#result = OpenJson('data\\SubWiki.json')

filename = "definition.txt"
def_open = open(filename,"w")
res = Create_URL_List(OpenJson('data\\SubWiki.json'))
for line in res:
    strng = url_Parse(line)
    test = Define(strng.string)
    sentences = test.tokenized
    doc = nlp(sentences)
    sen = [sent.string.strip() for sent in doc.sents]
    def_open.write("".join(sen)+'\n'+ line)    
    def_open.write("\n")
def_open.close()
    
    
    
    