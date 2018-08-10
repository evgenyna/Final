# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 19:43:00 2018

@author: evgen
"""


from tools.general import *
#from definitions.Definition import *
from definitions.url_Parse import *
from data import *
import spacy

url='https://groupprops.subwiki.org/w/index.php?title=1-automorphism-invariant_subgroup&action=edit'
strng = url_Parse(url)