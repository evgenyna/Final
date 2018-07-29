# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:29:34 2018

@author: evgen
"""

from tools.general import *
from definitions.Definition import *
from definitions.url_Parse import *

#import spacy



OUTPUT_DIR = 'data'

create_dir(OUTPUT_DIR)

url = 'https://groupprops.subwiki.org/w/index.php?title=(2,3,7)-triangle_group&action=edit'
string = url_Parse(url)

test = Define(string.string)


tags = test.all_tags_pos

formulas = test.all_formulas
#print(formulas[0])
text = test.tags_removed
#print(text)
sentences = test.tokenized