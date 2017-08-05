# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:23:47 2017

@author: John Lee
"""
class comileEngine:
    symbols = set(['{','}','(',')','[',']','.',',',';','+','-',\
               '*','/','&','|','<','>','=','~'])
    keywords = set(['class','constructor','function','method','field','static',\
                'var','int','char','boolean','void','true','false','null',\
                'this','let','do','if','else','while','return'])
    def __init__(self,words,fhand):
        self.words = words
        self.length = len(words)
        self.index = 0
        self.fhand = fhand
        
    def cur(self):
        return self.words[self.index]
    def compileClass(self):
        self.fhand.write('<class>\n')
        self.tokenize(3)    
        self.compilefield()
        self.compilesub()
        self.tokenize(1)
        self.fhand.write('</class>\n')
    def tokenize(self,count):
        i = 0     
        while i < count:
            word = self.cur()
            if word in self.keywords:
                self.fhand.write('<keyword>{}</keyword>\n'.format(word))
            elif word in self.symbols:
                self.fhand.write('<symbol>{}</symbol>\n'.format(word))
            elif word.startswith('"'):
                word = word.strip('"')
                self.fhand.write('<stringConstant>{}</stringConstant>\n'.format(word))
            elif word.isnumeric():
                self.fhand.write('<integerConstant>{}</integerConstant>\n'.format(word))
            else:
                self.fhand.write('<identifier>{}</identifiler>\n'.format(word))
            self.index += 1
            i += 1
        
    def compilefield(self):
        while self.cur() in {'field','static'}:
            self.fhand.write('<classVarDec>\n')
            self.tokenize(4)
            self.fhand.write('</classVarDec>\n')
            
    def compilesub(self):
        while self.cur() in {'constructor','function','method'}:
            self.fhand.write('<subroutineDec>\n')
            self.tokenize(4)
            self.compileparm()
            self.tokenize(2)
            self.compilesbd()
            self.tokenize(1)
            self.fhand.write('</subroutineDec>\n')
            
    def compileparm(self):
        if self.cur() != ')':
            self.tokenize(1)
            while self.cur() == ',':
                self.tokenize(2)
                
    def compilesbd(self):
        self.fhand.write('<subroutineBody>\n')
        self.compilevar()
        self.fhand.write('<statements>\n')
        self.compilestm()
        self.fhand.write('</statements>\n')
        self.fhand.write('</subroutineBody>\n')
        
    def compilevar(self):
        while self.cur() == 'var':
            self.fhand.write('<varDec>\n')
            self.tokenize(4)
            self.fhand.write('</varDec>\n')
            
    def compilestm(self):
        if self.cur() == 'let':
            self.compilelet()
        if self.cur() == 'do':
            self.compiledo()
        if self.cur() == 'if':
            self.compileif()
        if self.cur() == 'else':
            self.compileelse()
        if self.cur() == 'while':
            self.compilewhile()
        if self.cur() == 'return':
            self.compilereturn()
    def compilelet(self):
        self.fhand.write('<letStatement>\n')
        self.tokenize(2)
        if self.cur() == '(':
            self.tokenize(1)
            self.compilexp()
            self.tokenize(1)
        self.tokenize(1)
        self.compilexp()
        self.tokenize(1)
        self.fhand.write('</letStatement>\n')
        