# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq



import spacy
from spacy.tokenizer import Tokenizer
nlp = spacy.load('en_core_web_sm')

class url_Parse:    
    def __init__(self, myUrl):
        self.myUrl = myUrl
        self.string = self.__parsing()
        
    def __parsing(self):
        uClient = uReq(self.myUrl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        TBData = page_soup.find("textarea",{"id": "wpTextbox1"})
#        result = TBData.text.replace('{{particular group}}\n\n==Definition==\n\n', '')
        flag=False
        result = ''
        for k in TBData.text.splitlines():
            if flag:
                if k.strip():
                    if not '===' or not '==' in k:
                        result+=k
            if '==Definition==' in k :
                flag=True
            elif '== Definition ==' in k:
                flag=True
#        nlp = spacy.load('en_core_web_sm')
#        doc = nlp(TBData.text)
#        sentences = [sent.string.strip() for sent in doc.sents]
        return result
    