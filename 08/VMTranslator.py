# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:28:48 2017

@author: John Lee
"""
import os
import re
import sys
from Parser import *

def main(fname):
    if os.path.isfile(fname):
        nameasm = re.sub(r'.vm','.asm',fname)
        output = open(nameasm, 'w')
        throughfile(fname,output)
        output.close()
    elif os.path.isdir(fname):
        nameasm = fname.split(sep='/')[-1]+'.asm'
        nameasm = os.path.join(fname,nameasm)
        output = open(nameasm, 'w')
        for file in os.listdir():
            if file.split(sep='.')[-1] == 'vm':
                throughfile(file,output)
        output.close()

def throughfile(filename,resultfile):
    try:
        fhand = open(filename)
    except:
        print('File cannot be opened:', filename)
        exit()
    linecount = 1
    for line in fhand:
        if '//' in line:
            line = re.sub(r'//(.*)','',line)
        line = line.strip()
        if len(line) ==0:
            continue
        lineasm = translate(line,linecount)
        resultfile.writelines(lineasm)
        linecount = linecount + 1
        
def translate(line,linecount):
    if line in alcmd:
        lasm = alcmd.get(line)
        return lasm.format(linecount)
    words = line.split(sep=' ')
    if words[0] == 'push':
        lasm = pushcmd.get(words[1])
        return lasm.format(words[2])
    if words[0] == 'pop':
        lasm = popcmd.get(words[1])
        return lasm.format(words[2]) 
    if words[0] in branchcmd:
        lasm = branchcmd.get(words[0])
        return lasm.format(words[1])

    


print(funcmd['function'])
#main(sys.argv[1])
