# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:23:47 2017

@author: John Lee
"""
class CompileEngine:
    symbols = set(['{','}','(',')','[',']','.',',',';','+','-',\
               '*','/','&','|','<','>','=','~'])
    keywords = set(['class','constructor','function','method','field','static',\
                'var','int','char','boolean','void','true','false','null',\
                'this','let','do','if','else','while','return'])
    operations = set(['+','-','*','/','&','|','<','>','='])
    def __init__(self,words,fhand):
        self.words = words
        self.index = 0
        self.classtable = dict()
        self.subtable = dict()
        self.fhand = fhand
        
    def get(self, i):
        return self.words[self.index + i]
    
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
                self.fhand.write('<identifier>{}</identifier>\n'.format(word))
            self.index += 1
            i += 1
            
    def compileClass(self):
        self.fhand.write('<class>\n')
        self.tokenize(3)    
        self.compilecvd()
        self.compilesub()
        self.tokenize(1)
        self.fhand.write('</class>\n')
    
        
    def compilecvd(self):
        cvidx = 0
        while self.get(0) in {'field','static'}:
            vkind = self.get(0)
            vtype = self.get(1)
            self.classtable[self.get(2)] = (vtype, vkind, cvidx)
            cvidx += 1
            self.index += 3
            while self.get(0) == ',':
                self.classtable[self.get(1)] = (vtype, vkind, cvidx)
                cvidx += 1
                self.idx += 2
            self.index += 1
            
    def compilesub(self):
        while self.get(0) in {'constructor','function','method'}:
            subroutine = self.get(0)

            self.tokenize(4)
            nargs = self.compilepml()
            if subroutine == 'constructor':
                self.fhand.write('push {}'.format(nargs))
                self.fhand.write('call Memory.alloc 1')
            self.tokenize(1)
            self.compilesbd()
            self.fhand.write('</subroutineDec>\n')
            
    def compilepml(self):                         # compile parameterlist
        argidx = 0
        nargs = 0
        if self.get(0) != ')':
            self.subtable[self.get(1)] = (self.get(0), 'argument', argidx)
            self.index += 2
            nargs +=1
            while self.get(0) == ',':
                self.subtable[self.get(1)] = (self.get(1), 'argument', argidx)
                self.index += 3
                nargs +=1
        return nargs
        
                
    def compilesbd(self):
        self.fhand.write('<subroutineBody>\n')
        self.tokenize(1)
        self.compilevar()        
        self.compilestm()
        self.tokenize(1)        
        self.fhand.write('</subroutineBody>\n')
        
    def compilevar(self):
        while self.cur() == 'var':
            self.fhand.write('<varDec>\n')
            self.tokenize(3)
            while self.cur() == ',':
                self.tokenize(2)
            self.tokenize(1)
            self.fhand.write('</varDec>\n')
            
    def compilestm(self):
        self.fhand.write('<statements>\n')
        while self.cur() in {'let','do','if','while','return'}:
            if self.cur() == 'let':
                self.compilelet()
            elif self.cur() == 'do':
                self.compiledo()
            elif self.cur() == 'if':
                self.compileif()
            elif self.cur() == 'while':
                self.compilewhile()
            elif self.cur() == 'return':
                self.compilereturn()
        self.fhand.write('</statements>\n')
        
    def compilelet(self):
        self.fhand.write('<letStatement>\n')
        self.tokenize(2)
        if self.cur() == '[':
            self.tokenize(1)
            self.compilexp()
            self.tokenize(1)
        self.tokenize(1)
        self.compilexp()
        self.tokenize(1)
        self.fhand.write('</letStatement>\n')
        
    def compiledo(self):
        self.fhand.write('<doStatement>\n')
        self.tokenize(2)
        if self.cur() == '.':
            self.tokenize(3)
            self.compilexpl()
            self.tokenize(1)
        elif self.cur() == '(':
            self.tokenize(1)
            self.compilexpl()
            self.tokenize(1)     
        self.tokenize(1)
        self.fhand.write('</doStatement>\n')
        
    def compileif(self):
        self.fhand.write('<ifStatement>\n')
        self.tokenize(2)
        self.compilexp()
        self.tokenize(2)
        self.compilestm()
        self.tokenize(1)
        if self.cur() == 'else':
            self.tokenize(2)
            self.compilestm()
            self.tokenize(1)
        self.fhand.write('</ifStatement>\n')
        
    def compilewhile(self):
        self.fhand.write('<whileStatement>\n')
        self.tokenize(2)
        self.compilexp()
        self.tokenize(2)
        self.compilestm()
        self.tokenize(1)
        self.fhand.write('</whileStatement>\n')
        
    def compilereturn(self):
        self.fhand.write('<returnStatement>\n')
        self.tokenize(1)
        if self.cur() != ';':
            self.compilexp()
        self.tokenize(1)
        self.fhand.write('</returnStatement>\n')
        
    def compilexp(self):
        self.fhand.write('<expression>\n')
        self.compileterm()
        while self.cur() in self.operations:
            self.tokenize(1)
            self.compileterm()
        self.fhand.write('</expression>\n')

    def isconstant(self):
        word = self.cur()
        if word.isnumeric() or word.startswith('"') or\
        word in {'true','false','null','this'}:
            return True
        return False
    def compileterm(self):
        self.fhand.write('<term>\n')
        if self.isconstant():
            self.tokenize(1)
        elif self.cur() in {'~','-'}:
            self.tokenize(1)
            self.compileterm()
        elif self.cur() == '(':
            self.tokenize(1)
            self.compilexp()
            self.tokenize(1)
        elif self.cur()[0].isalpha() or self.cur()[0] == '_':
            self.tokenize(1)
            if self.cur() == '[':
                self.tokenize(1)
                self.compilexp()
                self.tokenize(1)
            elif self.cur() == '.':
                self.tokenize(3)
                self.compilexpl()
                self.tokenize(1)
            elif self.cur() == '(':
                self.tokenize(1)
                self.compilexpl()
                self.tokenize(1)            
        self.fhand.write('</term>\n')
        
    def compilexpl(self):
        self.fhand.write('<expressionList>\n')
        if self.cur() != ')':
            self.compilexp()
            while self.cur() == ',':
                self.tokenize(1)
                self.compilexp()
        self.fhand.write('</expressionList>\n')