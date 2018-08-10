# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:41:17 2018

@author: evgen
"""

import json
from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
from html5lib import HTMLParser


#import spacy
#from spacy.tokenizer import Tokenizer
#nlp = spacy.load('en_core_web_sm')


myUrl = 'https://groupprops.subwiki.org/w/index.php?title=(2,3,7)-triangle_group&action=edit'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

# =============================================================================
# for p in page_soup:
#     print(page_soup.p)
# =============================================================================
TBData = page_soup.find("textarea",{"id": "wpTextbox1"})
T = TBData.text.replace('{{particular group}}\n\n==Definition==\n\n', '')
start = '<math>'
end = '</math>'

#Finding positions of "start"
tag1 = []

test_string = 'The <math>(7,3,2)</math>-triangle group or <math>(2,3,7)</math>-triangle group is defined as the [[member of family::triangle group]] with parameters <math>(7,3,2)</math>. Equivalently, it is defined as:\n\n<math>\\langle s_1, s_2, s_3 \\mid s_1^2 = s_2^2 = s_3^2 = (s_1s_2)^7 = (s_2s_3)^3 = (s_3s_1)^2 = e \\rangle</math>.\n\nHere, <math>e</math> is the identity element.\n\nThe term <math>(7,3,2)</math>-triangle group or <math>(2,3,7)</math>-triangle group is also used for the [[subgroup of index two]] in this group, which we refer to [[(7,3,2)-von Dyck group]].\n'
def Find_Tags_Positions(string):
    tag = []
    for m in re.finditer(start, string):   #Finding position of "end" in
        temp = T[m.end():] #String after tag
        temp1 = re.search(end,temp)
        start_pos = temp1.span()[0] + m.end() #Closing position
        end_pos = temp1.span()[1] + m.end()  #Tag ending position
        temp = {m: [m.start(), m.end(), start_pos, end_pos]}
        tag.append(temp)
    return tag

def Formulas(tag_list, string):
    List = set()
    for x in tag_list:
        for tag,value in x.items():
            List.add(string[value[1]:value[2]])
    return List

#def Tags_And_Formulas_Remove(Tags,formulas,string):

tags = Find_Tags_Positions(T)


#tags[0].items(start)
#for v in tags[0].items():
#...     print(v)





#s = Substr(T, beginning, LENGTH)
#T+=TBData.text.replace(']]', '')
#T+=TBData.text.replace('[[', '')


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
            
#jsonD = json.dumps(TBData.text)

