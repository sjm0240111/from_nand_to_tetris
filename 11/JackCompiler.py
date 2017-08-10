# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:13:19 2017

@author: John Lee
"""

import os
import re
import sys
from compilengine import *

def main(fname):
    if os.path.isfile(fname):                         # user gives one file
        #print(fname)
        compilefile(fname)
        
    elif os.path.isdir(fname):                       # user gives one directory        
        filelist = list()
        for file in os.listdir(fname):                         # get all jack files
            if file.split(sep='.')[-1] == 'jack':
                pathedfile = os.path.join(fname, file)
                filelist.append(pathedfile)
        #print(filelist)
        if len(filelist) == 0:
            print('no jack file exist')
            exit()                                            
        for pf in filelist:                              # translating all
            compilefile(pf)
    else:
        print('no such file or directory')

def tokenizer(text):
    comment = r'//.*\n|/\*[\s\S]*?\*/'
    symbolptn = r'(\{)|(\})|(\()|(\))|(\[)|(\])|(\.)|(\,)|(;)|(\+)|'\
    +'(\-)|(\*)|(/)|(&)|(\|)|(<)|(>)|(=)|(~)'
    symbolrpl = r' \1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19 '
    text = re.sub(comment, ' ',text)               # remove comment
    _roughlist = text.split('"')
    i = 1
    tokens = list()
    while i < len(_roughlist):
        _subtext = re.sub(symbolptn, symbolrpl, _roughlist[i-1])       # separate elements
        _subtext = _subtext.strip() 
        tokens = tokens + re.split(r'\s+', _subtext) 
        tokens.append('"'+_roughlist[i])
        i = i+2
    _subtext = re.sub(symbolptn, symbolrpl, _roughlist[i-1])      
    _subtext = _subtext.strip() 
    tokens = tokens + re.split(r'\s+', _subtext) 
    return tokens     

def compilefile(jackfile):
    with open(jackfile, 'r') as myfile:
        text = myfile.read()
    tokens = tokenizer(text)
    namevm = re.sub(r'.jack','.vm',jackfile)
    fout = open(namevm, 'w')
    jackobj = CompileEngine(tokens,fout)
    #jackobj.tokenize(len(tokens))
    jackobj.compileClass()
    fout.close()
            
#main(sys.argv[1])  