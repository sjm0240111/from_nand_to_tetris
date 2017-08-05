# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:13:19 2017

@author: John Lee
"""

import os
import re
import sys
from JackTokenizer import *

def main(fname):
    if os.path.isfile(fname):                         # user gives one file
        analyzefile(fname)
        
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
            analyzefile(pf)
    else:
        print('no such file or directory')

def parseword(text):
    comment = r'//.*\n|/\*.*?\*/'
    symbolptn = r'(\{)|(\})|(\()|(\))|(\[)|(\])|(\.)|(\,)|(;)|(\+)|'\
    +'(\-)|(\*)|(/)|(&)|(\|)|(<)|(>)|(=)|(~)'
    symbolrpl = r' \1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19 '
    text = re.sub(comment, ' ',text)               # remove comment
    text = re.sub(symbolptn, symbolrpl, text)       # separate elements
    text = text.strip()
    wordlist = re.split(r'\s+', text)   
    return wordlist     

def analyzefile(jackfile):
    with open(jackfile, 'r') as myfile:
        text = myfile.read()
    wordlist = parseword(text)
    namevm = re.sub(r'.jack','.vm',jackfile)
    fout = open(namevm, 'w')
    i = 0
    vardeci = 0
    nTlist = list()
    paramstate = False
    for i in wordlist:
        word = wordlist[i]
        if word in keywords:
            if word in structure:             # structure keyword with {}
                nTlist.append(word)
                fout.write(nTStart.get(word))
            if word in variable:                # variable declaration
                nTlist.append(word)    
                fout.write(nTStart.get(word))
                vardeci = i
            fout.write('<keyword>{}</keyword>'.format(word))
        elif word in symbols:
            if word == '}' and nTlist[-1] in statements:
                fout.write('</statements>\n')
            elif word == '(':
                if nTlist[-1] in subroutine:
                    fout.write('<parameterList>\n')
                    paramstate = True
            fout.write('<symbol>{}</symbol>\n'.format(word))
            if word == '{' and nTlist[-1] in statements:
                fout.write('<statements>\n')
            elif word == '}':
                fout.write(nTEnd.get(nTlist.pop()))              
            elif word == ')':
                if paramstate == True:
                    fout.write('</parameterList>\n')
                    paramstate = False
                elif 
                
        elif word.startswith('"'):
            word = word.strip('"')
            fout.write('<stringConstant>{}</stringConstant>'.format(word))
        elif word.isnumeric():
            fout.write('<integerConstant>{}</integerConstant>'.format(word))
        else:
        if i-vardeci == 2:
            fout.write(nTEnd.get(nTlist.pop()))
        i += 1
            
            
    
    

    