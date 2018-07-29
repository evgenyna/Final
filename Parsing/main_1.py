# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import spacy

# myUrl = 'https://groupprops.subwiki.org/w/index.php?title=Abelian_group&action=edit'

# uClient = uReq(myUrl)

# page_html = uClient.read()

# uClient.close()

# page_soup = soup(page_html, "html.parser")
# test = page_soup.find_all('textarea')
# test=str(test).splitlines()

#print(re.findall(r'==Definition==(.+?)\.',repr(test)))
#t = repr(test)

# tr=False
# for line in test:
#     if tr == False:
#         #print(line)
#        test.remove(line)
#     if line == '==Definition==':
#         tr = True
#     break
# RegEx = r'==Definition==(.+?)\.'

#print(test)
# for line in test:
#     print(re.search(r'(.+?)\.',line))
# print(re.findall(r'(.+?)\.',test[1]))
# ttt = re.findall(r'(.+?)\.',test[0])
# print(ttt[0])
# test=str(test).splitlines()
# for des in page_soup.p.descendants:
# 	print(des)

#************Site scrapping from received URL
def Scraping(myUrl):
	uClient = uReq(myUrl)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	#********Searching and extracting TextBox data from site
	TBData = page_soup.find_all('textarea')
#	result=str(TBData).splitlines()
	return str(TBData)

#************Parsing Json file
def OpenJson(Jfile):
    result = []
    with open(Jfile) as f:
        d = json.load(f)
    for key in d.keys():
        key = key.replace(" ","_")
        result.append(key)
    return result

#************Get list of sites names and return list of URL's
def Create_URL_List(ToAppend):
    result = []
    for line in ToAppend:
        line = 'https://groupprops.subwiki.org/w/index.php?title=' + line + '&action=edit'
        result.append(line)
    return result

#************Get list of URL's and scrapping
#************After scrapping will find Definition sentences
#************Write definition sentence into "Definition.txt" file
def DefinitionExtract(DefList):
   #     temp = DefList
   #     type(temp)
        def Remove(TbText):
            tr=False
            tmp=TbText
            
            for line in tmp:
                if line == '==Definition==':
                    tr = True
                    tmp.remove(line)
                #break                    
                if tr == False:
                    tmp.remove(line)                   
            return tmp
        temp = Remove(DefList)
        temp=str(temp).splitlines()
        temp = re.findall(r'(.+?)\.',temp[0])               
        return temp[0]

result = OpenJson('SubWiki.json')

#print(result)


res = Create_URL_List(result)
#print(res)
filename = "definition.txt"
def_open = open(filename,"w")

for line in res: #List of URL's
    test = Scraping(line)
#    def_open.write(line) #Adding URL
#    def_open.write("\n")
#    test2 = DefinitionExtract(test)   
    def_open.write(test)    
    def_open.write("\n")
#    def_open.write("\n")
def_open.close()



