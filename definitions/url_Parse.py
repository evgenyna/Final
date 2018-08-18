# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq



import spacy
from spacy.tokenizer import Tokenizer
nlp = spacy.load('en_core_web_sm')

class url_Parse:    
    def __init__(self, myUrl):
        self.myUrl = myUrl
        self.string = self.__parsing()[0]
        self.defORstatement = self.__parsing()[1]
        
    def __parsing(self):
        fileName = open('AllText.txt','a')
        uClient = uReq(self.myUrl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        TBData = page_soup.find("textarea",{"id": "wpTextbox1"})
        [fileName.write(text + '\n') for text in TBData.text.splitlines()]
        fileName.write(self.myUrl + '\n')
        fileName.close()
#        result = TBData.text.replace('{{particular group}}\n\n==Definition==\n\n', '')
        flag=False
        result = ''
        defORstatement = ''
        for k in TBData.text.splitlines():
            if flag:
                if k.strip():
                    if 'class="sortable" border="1"' in k:
                        return ['Table','Table']
                    if not '===' or not '==' in k:
                        return [k,defORstatement]
                        #result+=k
                        #break
#                    else:
#                        flag=False
            if '==Definition==' in k :
                flag=True
                defORstatement = 'D'
            if '== Definition ==' in k:
                flag=True
                defORstatement = 'D'
            if '==Statement==' in k:
                flag=True
                defORstatement = 'S'
                
            
#        nlp = spacy.load('en_core_web_sm')
#        doc = nlp(TBData.text)
#        sentences = [sent.string.strip() for sent in doc.sents]
        return [result,defORstatement]
    