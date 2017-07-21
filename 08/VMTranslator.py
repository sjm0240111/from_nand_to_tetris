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
    if os.path.isfile(fname):                         # one file
        nameasm = re.sub(r'.vm','.asm',fname)
        fout = open(nameasm, 'w')
        fhand = openfile(fname)
        throughfile(fhand,fout)       
        fout.close()
        print(fout.name)
    elif os.path.isdir(fname):                       # one directory        
        filelist = list()
        for file in os.listdir(fname):                         # get all vm files
            if file.split(sep='.')[-1] == 'vm':
                pathedfile = os.path.join(fname, file)
                filelist.append(pathedfile)
        print(filelist)
        if len(filelist) == 0:
            print('no vm file exist')
            exit()
        if len(filelist) == 1:                        # one file in dir
            fhand = openfile(pathedfile)
            fout = open(re.sub(r'.vm','.asm',pathedfile),'w')
            throughfile(fhand,fout)
            fout.close()
        else:                                           # multiple files
            nameasm = fname.split(sep='/')[-1]+'.asm'
            nameasm = os.path.join(fname,nameasm)
            fout = open(nameasm,'w')
            fout.writelines('@256\nD=A\n@R0\nM=D\n')
            fout.writelines('@Sys.init\n0;JMP\n')
            #fout.writelines(funcmd['call'].format('Sys.init','0','0'))
            for pf in filelist:
                fhand = openfile(pf)
                throughfile(fhand,fout)
        fout.close()
        fhand.close()
    else:
        print('no such file or directory')
            
def openfile(file):
    try:
        fhand = open(file)
    except:
        print('File cannot be opened:', file)
        exit()
    return fhand

def throughfile(resource,resultfile):
    linecount = 1
    fun = ''
    classname = os.path.splitext(resource.name)[1]
    for line in resource:
        if '//' in line:
            line = re.sub(r'//(.*)','',line)
        line = line.strip()
        if len(line) ==0:
            linecount += 1
            continue
        if line in alcmd:
            lasm = alcmd.get(line)
            lineasm = lasm.format(fun,linecount)
        else:
            words = line.split(sep=' ')
            if words[0] == 'call': 
                lasm = funcmd.get(words[0])
                lineasm = lasm.format(words[1], words[2], linecount)
            elif words[0] == 'return':
                lineasm = funcmd.get(words[0])
            elif words[0] == 'function':
                fun = words[1]
                lasm = funcmd.get(words[0])
                lineasm = lasm.format(words[1], words[2])
            elif words[0] == 'push':
                lasm = pushcmd.get(words[1])
                lineasm = lasm.format(words[2], classname)
            elif words[0] == 'pop':
                lasm = popcmd.get(words[1])
                lineasm = lasm.format(words[2], classname) 
            elif words[0] in branchcmd:
                lasm = branchcmd.get(words[0])
                lineasm = lasm.format(fun, words[1])
            else:
                print('invalid vm command in file {}, line {0}'.format(resource.name, linecount))
        resultfile.writelines(lineasm)
        linecount += 1
    
    print(resource.name+': '+str(linecount))
#print(funcmd['function'])
#main(sys.argv[1])