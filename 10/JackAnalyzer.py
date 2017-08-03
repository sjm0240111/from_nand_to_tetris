# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:13:19 2017

@author: John Lee
"""

import os
import re
import sys

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
        
def openfile(file):
    try:
        fhand = open(file)
    except:
        print('File cannot be opened:', file)
        exit()
    return fhand

def analyzefile(jackfile):
    with open(jackfile, 'r') as myfile:
        text = myfile.read()
    
    namevm = re.sub(r'.jack','.vm',jackfile)
    fout = open(namevm, 'w')
    
    
def analyzeline(line):
    