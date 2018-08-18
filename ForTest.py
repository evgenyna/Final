# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 19:43:00 2018

@author: evgen
"""
import json
from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import spacy
from data import *
from definitions.url_Parse_double import *
import pypandoc
from nltk import sent_tokenize
from tools.general import *
import os.path

from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'D:\stanford-corenlp-full-2018-02-27\stanford-corenlp-full-2018-02-27')


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

def parse2file(sentences, DorS, url, index):
    if os.path.isfile('vimwiki.txt'):
        f1='a'
    else:
        f1='w'
    if os.path.isfile('vimwikiDefsURLs.txt'):
        f2='a'
    else:
        f2='w'
    if os.path.isfile('Statements.txt'):
        f3='a'
    else:
        f3='w'
    if os.path.isfile('StatementsURLs.txt'):
        f4='a'
    else:
        f4='w'
    filename =  open('vimwiki.txt', f1, encoding = 'utf-8')
    filename1 =  open('vimwikiDefsURLs.txt', f2, encoding = 'utf-8')
    filename2 =  open('Statements.txt', f3, encoding = 'utf-8')
    filename3 =  open('StatementsURLs.txt', f4, encoding = 'utf-8')
#    if os.path.isfile('test1.txt'):
#        f1='a'
#    else:
#        f1='w'
#    if os.path.isfile('test2.txt'):
#        f2='a'
#    else:
#        f2='w'
#    if os.path.isfile('test3.txt'):
#        f3='a'
#    else:
#        f3='w'
#    if os.path.isfile('test4.txt'):
#        f4='a'
#    else:
#        f4='w'        
#    filename =  open('test1.txt', f1, encoding = 'utf-8')
#    filename1 =  open('test2.txt', f2, encoding = 'utf-8')
#    filename2 =  open('test3.txt', f3, encoding = 'utf-8')
#    filename3 =  open('test4.txt', f4, encoding = 'utf-8')
    props={'annotators': 'ssplit','pipelineLanguage':'en','outputFormat':'JSON'}
    text2convert = pypandoc.convert_text(sentences, 'plain', format = 'mediawiki')
    if re.search('$', text2convert) is not None:
        text2convert = pypandoc.convert_text(text2convert, 'plain', format = 'vimwiki')
    js = json.loads(nlp.annotate(text2convert, properties=props))
    for sentence, sentences in enumerate(js['sentences']):
        result = ''
        for i, originalText in enumerate(js['sentences'][sentence]['tokens']):
            if i < len(js['sentences'][sentence]['tokens'])-1 :        
                result += originalText['originalText'] + ' '
            elif i >= len(js['sentences'][sentence]['tokens']) - 1 :
                result += originalText['originalText']
        if DorS == 'D':
            filename.write(result + '\n')
            filename1.write(result + '\n')
        if DorS == 'S':
            filename2.write(result + '\n')
            filename3.write(result + '\n')
    if DorS == 'D':
        filename.close()
        filename1.write(str(index) + '\n')
        filename1.write(url + '\n')
        filename1.close()
    if DorS == 'S':
        filename2.close()
        filename3.write(str(index) + '\n')
        filename3.write(url + '\n')
        filename3.close()
#=========================For Testing+++++++++++++++
#f = open('test1.txt', 'w')
#f.close()
#f = open('test2.txt','w')
#f.close()
#f = open('test3.txt', 'w')
#f.close()
#f = open('test4.txt','w')
#f.close()
#
#url='https://groupprops.subwiki.org/w/index.php?title=Characterization_of_free_Lie_ring_in_terms_of_eigenspaces_of_Dynkin_operator&action=edit'
#string_ = url_test(url)
#
#if string_.string[1] == True:
#    parse2file(string_.string[0], string_.string[2], url, 0)
#
        #=========================Real run+++++++++++++++
f = open('vimwiki.txt', 'w')
f.close()
f = open('vimwikiDefsURLs.txt','w')
f.close()
f = open('Statements.txt', 'w')
f.close()
f = open('StatementsURLs.txt','w')
f.close()
fileName = open('AllText.txt' ,'w',  encoding = 'utf-8')
fileName.close()
res = Create_URL_List(OpenJson('data\\SubWiki.json'))
for indx, line in enumerate(res):
    string_ = url_test(line)
    if string_.string[1] == True:
        parse2file(string_.string[0], string_.string[2], line, indx)
