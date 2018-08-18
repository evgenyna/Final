# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import pypandoc
from nltk import sent_tokenize


import spacy
from spacy.tokenizer import Tokenizer
nlp = spacy.load('en_core_web_sm')

class url_test:    
    def __init__(self, myUrl):
        self.myUrl = myUrl
        self.string = self.__parsing()
#        self.defORstatement = self.__parsing()[2]
        
    def __parsing(self):
        def parsed_string():
            uClient = uReq(self.myUrl)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            TBData = page_soup.find("textarea",{"id": "wpTextbox1"})
            fileName = open('AllText.txt' ,'a',  encoding = 'utf-8')
            fileName.writelines(TBData.text + '\n')
            fileName.write(self.myUrl + "\n\n")
            fileName.close()
            return TBData.text.splitlines()
        def findDefinition(str_):
            DorS = ''
            whitespacesDict =	{
                "4": "\u2004",
                "5": "\u2005",
                "6": "\u2006",
                "\r": "\r",
                "#": "#"
                }
            #Cleanning empty lines
            for line in str_:
                if not line.strip():
                    str_.remove(line)
            #findin definition text        
            flag=False
            triple_flag=False
            idx=0
            result =''
            for line in str_:
                if flag==True:
                    if re.search(r'^={2}[^=].*[^=]={2}$',line):
                        break
                    if re.search(r'^={3}\s*.*\s*={3}$',line):
                        triple_flag=True
                        idx+=1
                        continue
                    line = re.sub(r'\[{2}\w*?(\ \w+)+\:{2}', '[[', line)
#                k = pypandoc.convert_text(k, 'plain', format = 'mediawiki')
                    for value in whitespacesDict.values():
                        line = line.replace(value,"")
                    line = line.replace("\n"," ")
                    result+=line + "\n"
                if re.search(r'^={2}\s*Definition\s*={2}$',line):
                    flag=True
                    DorS = 'D'
                if re.search(r'^={2}\s*Statement\s*={2}$',line):
                    flag=True
                    DorS = 'S'
                    
            return [result, DorS]
        result = findDefinition(parsed_string())
        table = re.search('class="sortable" border="1"',result[0])
        DorS = result[1]
        return [result[0],table is None, DorS]
               
                
                
#        fileName = open('AllText.txt','a')
##        uClient = uReq(self.myUrl)
##        page_html = uClient.read()
##        uClient.close()
##        page_soup = soup(page_html, "html.parser")
##        TBData = page_soup.find("textarea",{"id": "wpTextbox1"})
##        [fileName.write(text + '\n') for text in TBData.text.splitlines()]
##        fileName.write(self.myUrl + '\n')
##        fileName.close()
##        result = TBData.text.replace('{{particular group}}\n\n==Definition==\n\n', '')
#        flag=False
#        tripl_flag=False
#        idx=0
#        result =''
#        defORstatement = ''
#        whitespacesDict =	{
#                "4": "\u2004",
#                "5": "\u2005",
#                "6": "\u2006",
#                "\r": "\r"
#                }
#        text = TBData.text.splitlines()
#        for line in text :
#            if not line.strip():
#                text.remove(line)
#        for k in text:
##            if flag:
##                if k.strip():
##                    if '{| class="sortable" border="1"' in k:
##                        return ['Table','Table']
##                    if not '===' or not '==' in k:
##                        result += k
##                        temp = re.search(r'^={2}[^=].*[^=]={2}$',k)        
##                        if temp is not None:
##                            return [result,defORstatement]
##            if '==Definition==' in k :
##                flag=True
##                defORstatement = 'D'
##            if '== Definition ==' in k:
##                flag=True
##                defORstatement = 'D'
##            if '==Statement==' in k:
##                flag=True
##                defORstatement = 'S'
#            if flag==True:
#                if re.search(r'^={2}[^=].*[^=]={2}$',k):
#                    break
#                if re.search(r'^={3}\s*.*\s*={3}$',k):
#                    tripl_flag=True
#                    idx+=1
#                    continue
#                
#                k = re.sub(r'\[{2}\w*?(\ \w+)+\:{2}', '[[', k)
##                k = pypandoc.convert_text(k, 'plain', format = 'mediawiki')
#                for value in whitespacesDict.values():
#                    k = k.replace(value,"")
#                k = k.replace("\n"," ")
#                result+=k
#            if re.search(r'^={2}\s*Definition\s*={2}$',k):
#                flag=True
##        nlp = spacy.load('en_core_web_sm')
##        result.strip()
##        doc = nlp(result)
#        result = [sent.string.strip() for sent in doc.sents]
#        TEST = pypandoc.convert_text(result, 'plain', format = 'mediawiki')
#        t = sent_tokenize(TEST)
#        return TEST

