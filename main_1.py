# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import spacy
from data import *
from definitions.url_Parse import *
import pypandoc


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


res = Create_URL_List(OpenJson('data\\SubWiki.json'))
##res = Create_URL_List(OpenJson('data\\SubWikiRead.json'))
#
#deftext=[]
#deftext.append(strng.string+'\n')
working=open('working','w')
working.close()

file1=open('Definitions.txt','w', encoding="utf-8")
file2=open('Definitions with URL.txt','w', encoding="utf-8")
file3=open('Statements.txt','w', encoding="utf-8")
file4=open('Statements with URL.txt','w', encoding="utf-8")
file1.close()
file2.close()
file3.close()
file4.close()


fileName = open('AllText.txt' ,'w',  encoding = 'utf-8')
fileName.close()

file1=open('Definitions.txt','a', encoding="utf-8")
file2=open('Definitions with URL.txt','a', encoding="utf-8")
file3=open('Statements.txt','a', encoding="utf-8")
file4=open('Statements with URL.txt','a', encoding="utf-8")

Tables = open('Tables.txt','w')
Tables.close()
Tables = open('Tables.txt','a')
for line in res:
    strng = url_Parse(line)
    if strng.string : 
        str_ = strng.string
        typeOf = strng.defORstatement
        hypher = re.sub(r'\[{2}\w+?(\ \w+)+\:{2}', '[[', str_)
        #    braces = re.sub(r'\{(\w)\}', r'\1', hypher)
#        tables = re.sub(r'\{\|\ class="sortable" border="1"', '', hypher)
        #    apostr = re.sub("'''", '', tables)    
        output = pypandoc.convert_text(hypher, 'plain', format = 'mediawiki', outputfile = 'working')
        #    output = output.replace("\r","")
        #    output = output.replace("\n"," ")
        working = open('working','r', encoding="utf-8")    
        test = working.read()
        working.close()
#        for line in test:        
        test = test.replace("\r","")
        test = test.replace("\n"," ")#    newString = output.encode('ascii', 'ignore').decode("utf-8")
        if typeOf == 'D':
            file1.write(test)
            file1.write('\n')
            file2.write(test)
            file2.write(strng.myUrl)
            file2.write('\n')
            file2.write('\n')
        if typeOf == 'S':
            file3.write(test)
            file1.write('\n')
            file3.write(test)
            file4.write(strng.myUrl)
            file4.write('\n')
            file4.write('\n')
        if typeOf == 'Table':
            Tables.write(strng.myUrl)
file1.close()
file2.close()
file3.close()
file4.close()
Tables.close()
#    for k in deftext:
#        file2.write(k)
#        file2.write('\n')
#        file2.write(strng.myUrl)
#        file2.write('\n')
#        file1.write(k)
#        file1.write('\n')

#    

#url = 'https://groupprops.subwiki.org/w/index.php?title=1-automorphism-invariant_subgroup&action=edit'
#strng = url_Parse(url)
#deftext.append(strng.string)
#doc = nlp(strng.string)
#sen = [sent.string.strip() for sent in doc.sents]
#
#file1=open('output.txt','w')
#file2=open('output_URLs.txt','w')    
#for sentence in sen:
#    file2.write(sentence)
#    file2.write('\n')
#    file2.write(strng.myUrl)
#    file2.write('\n')
#    file1.write(sentence)
#    file1.write('\n')
#file2.close()
#file1.close()

#output = open("output.txt","r")
#input = open("input.txt","w")
#for line in output:
#    input.write(re.sub(r'\[{2}.*\::', '[[', line))
#input.close()
#output.close()
#
#output = open("output.txt","r")
#input = open("input.txt","w")
#for line in output:
#    input.write(re.sub('{| class="sortable" border="1"', '', line))
#input.close()
#output.close()
#
#output = open("output.txt","r")
#input = open("input.txt","w")
#for line in output:
#    input.write(re.sub(r'\{(\w+)\}', r'\1', line))

#for line in output:
#    c = re.sub(r'\{(\w)\}', r'\1', line)
#    t = re.sub(r'\[{2}.*\::', '[[', c)
#    a = re.sub(r'\{\|\ class="sortable" border="1"', '', t)
#    
#    input.write(a)
#    
#input.close()
#output.close()

#input = open("input.txt","r")
#output = open("output4.txt","w")
#output = pypandoc.convert_file('input.txt', 'plain', format = 'mediawiki', outputfile = 'output4.txt')

#
#output = open("output.txt","r")
#input = open("input.txt","w")
#for line in output:
#    
#    f = re.sub(t=r'\\mathbb\w\}',t , line)
#    
#    input.write(re.sub(r'\[{2}.*\::', '[[', line))
#input.close()
#output.close()
