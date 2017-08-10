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
    def __init__(self,tokens,fhand):
        self.classname = ''
        self.tokens = tokens
        self.index = 0
        self.classtable = dict()
        self.subtable = dict()
        self.fhand = fhand
        
    def get(self):
        self.index += 1
        return self.tokens[self.index-1]
        
    def cur():
        return self.tokens[self.index]
    
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
        if self.get() == 'class':
            self.index += 1
        self.classname = self.get()
        self.index += 1    
        self.compilecvd()
        self.compilesub()
    
        
    def compilecvd(self):
        vidx = 0
        vkind = self.get()
        while vkind in {'field','static'}:                            #field int wall;
            vtype = self.get()
            self.classtable[self.get()] = (vtype, vkind, cvidx)
            cvidx += 1
            while self.get() == ',':
                self.classtable[self.get()] = (vtype, vkind, cvidx)
                vidx += 1
            vkind = self.get()
        self.index += 1
        
    def compilesub(self):                                               # method void dispose() {
        self.subtable = dict()
        subroutine = self.get()
        ismethod = 0
        while subroutine in {'constructor','function','method'}:               
            self.index += 1                                            #void
            function = self.classname + self.get()                      # dispose
            if subroutine == 'method':
                self.subtable['this'] = (self.classname,'argument',0)
                ismethod = 1
            self.index += 1                                            # (
            nargs = self.compilepml(ismethod)
            self.fhand.write('function {0} {1}\n'.format(function, nargs))
            if subroutine == 'constructor':
                self.fhand.write('push constant {}\n'.format(nargs))
                self.fhand.write('call Memory.alloc 1\npop pointer 0\n')
            self.index += 2                                    # ){
            self.compilesbd()
            self.index += 1                                    # }
            subroutine = self.get()
            
    def compilepml(self,ismtd):                         # compile parameterlist
        argidx = ismtd
        vtype = self.get()
        if vtype != ')':
            self.subtable[self.get()] = (vtype, 'argument', argidx)
            argidx +=1
            vtype = self.get()
            while vtype == ',':
                self.subtable[self.get()] = (vtype, 'argument', argidx)
                vtype = self.get()
                argidx +=1
        return argidx
        
                
    def compilesbd(self):
        self.compilevar()
        
        self.compilestm()
        
    def compilevar(self):
        vidx = 0
        vkind = self.get()
        while vkind == 'var':                            #field int wall;
            vtype = self.get()
            self.subtable[self.get()] = (vtype, 'var', cvidx)
            cvidx += 1
            while self.get() == ',':
                self.classtable[self.get()] = (vtype, 'var', cvidx)
                vidx += 1
            vkind = self.get()
        self.index += 1
        
    def compilestm(self):
        stm = self.get()
        while stm in {'let','do','if','while','return'}:
            if stm == 'let':
                self.compilelet()
            elif stm == 'do':
                self.compiledo()
            elif stm == 'if':
                self.compileif()
            elif stm == 'while':
                self.compilewhile()
            else:
                self.compilereturn()
        
    def compilelet(self):
        self.index += 1
        identifier = self.get()
        varinfo = self.subtable.get(identifier, self.classtable.get(identifier,classname))
        if varinfo[1] == 'field'
        words = 'push {} {}
        if self.cur() == '[':
            self.index += 1
            self.compilexp()
            self.index += 1
        self.index += 1
        self.compilexp()
        self.index += 1
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