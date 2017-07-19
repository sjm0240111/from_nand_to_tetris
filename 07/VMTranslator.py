# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:28:48 2017

@author: 71804
"""
import re
import sys

def main(fname):
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    nameasm = str(fname).split(sep='.vm')[0]+'.asm'
    fout = open(nameasm, 'w')
    linecount = 1
    for line in fhand:
        if '//' in line:
            line = re.sub(r'//(.*)','',line)
        line = line.strip()
        if len(line) ==0:
            continue
        lineasm = translate(line,linecount)
        fout.writelines(lineasm)
        linecount = linecount + 1
    fout.close()
    
def translate(line,linecount):
    if line.startswith('push'):
        words = line.split(sep=' ')
        lasm = pushcmd.get(words[1])
        return lasm.format(words[2])
    elif line.startswith('pop'):
        words = line.split(sep=' ')
        lasm = popcmd.get(words[1])
        return lasm.format(words[2])    
    else:
        lasm = alcmd.get(line,-1)
        if lasm != -1:
            return lasm.format(linecount)
    
pushcmd = dict()
pushcmd['local']='@{}\nD=A\n@R1\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['argument']='@{}\nD=A\n@R2\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['this']='@{}\nD=A\n@R3\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['that']='@{}\nD=A\n@R4\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['temp']='@{}\nD=A\n@5\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['static']='@{}\nD=A\n@16\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['pointer']='@{}\nD=A\n@R3\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['constant']='@{}\nD=A\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'

popcmd = dict()
popcmd['local'] = '@{}\nD=A\n@R1\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['argument'] = '@{}\nD=A\n@R2\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['this'] = '@{}\nD=A\n@R3\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['that'] = '@{}\nD=A\n@R4\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['temp'] = '@{}\nD=A\n@5\nD=D+A\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['static'] = '@{}\nD=A\n@16\nD=D+A\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['pointer'] = '@{}\nD=A\n@R3\nD=D+A\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
    
alcmd = dict()
alcmd['add'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=D+M\n'
alcmd['sub'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D\n'
alcmd['neg'] = '@R0\nA=M\nA=A-1\nM=-M\n'
alcmd['and'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=D&M\n'
alcmd['or'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=D|M\n'
alcmd['not'] = '@R0\nA=M\nA=A-1\nM=!M\n'
alcmd['eq'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\nM=-1\n@EQ.{0}\n'\
+'D;JEQ\n@R0\nA=M\nA=A-1\nM=0\n(EQ.{0})\n'
alcmd['gt'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\nM=-1\n@GT.{0}\n'\
+'D;JGT\n@R0\nA=M\nA=A-1\nM=0\n(GT.{0})\n'
alcmd['lt'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\nM=-1\n@LT.{0}\n'\
+'D;JLT\n@R0\nA=M\nA=A-1\nM=0\n(LT.{0})\n'

main(sys.argv[1])
