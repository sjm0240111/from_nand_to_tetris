# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:23:47 2017

@author: John Lee
"""
class CompileEngine:
    operations = {'+':'add', '-':'sub', '*':'call Math.multiply 2',\
    '/':'call Math.divide 2', '&':'and', '|':'or', '<':'lt','>':'gt','=':'eq'}
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
                
    def compilepp(self, name, action):                                     # compile push and pop
        varinfo = self.subtable.get(name, self.classtable.get(name,self.classname))
        if varinfo[2] == 'field':
            self.fhand.write('{0} {1} {2}'.format(action, this, varinfo[3]))
        else:
            self.fhand.write('{0} {1} {2}'.format(action, varinfo[2], varinfo[3]))
        
    def compilelet(self):
        self.index += 1
        identifier = self.get()            
        if self.cur() == '[':
            self.compilepp(identifier,'push')
            self.index += 1
            self.compilexp()
            self.fhand.write('add\n')
            self.index += 2
            self.compilexp()
            self.fhand.write('pop temp 0\npop pointer 1\npush temp 0\npop that 0\n')
        else:
            self.index += 1
            self.compilexp()
            self.compilepp(identifier,'pop')
        self.index += 1

        
    def compiledo(self):
        self.index += 1
        identifier = self.get()  
        self.subroutinecall()
        self.fhand.write('pop temp 0\n')
        self.index += 1   
        
    def compileif(self):
        _labelif = 'ifexp.{}'.format(self.index)
        _labelelse = 'elsexp.{}'.format(self.index)
        self.index += 2
        self.compilexp()
        self.fhand.write('neg\nif-goto {}'.format(_labelif))
        self.index += 2
        self.compilestm()
        self.index += 1
        self.fhand.write('goto {0}\nlabel {1}\n'.format(_labelelse, _labelif))
        if self.cur() == 'else':
            self.index += 2
            self.compilestm()
            self.index += 1
        self.fhand.write('label {}\n'.format(_labelelse)
        
    def compilewhile(self):
        _labelyes = 'while.{}'.format(self.index)
        _labelno = 'cycle.{}'.format(self.index)
        self.index += 2
        self.compilexp()
        self.index += 2
        self.fhand.write('label {0}\nneg\nif-goto {1}'.format(_labelno, _labelyes))
        self.compilestm()
        self.index += 1
        self.fhand.write('goto {}\nlabel {}\n'.format(_labelno, _labelyes))
        
    def compilereturn(self):
        self.index += 1
        if self.cur() != ';':
            self.compilexp()
        else:
            self.fhand.write('push constant 0')
        self.index += 1
        
    def compilexp(self):
        self.compileterm()
        op = self.get()
        while op in self.operations: 
            self.compileterm()
            self.fhand.write(self.operations.get(op)+'\n')

    def writeconstant(self):
        word = self.cur()
        if word.isnumeric():
            self.fhand.write('push constant {}\n'.format(word))
        elif word.startswith('"'):
            word = word.strip('"')
            self.fhand.write('push constant {}\ncall String.new 1\n'.format(len(word)))
            i=0  
            while i< len(word)
                self.fhand.write('push constant {}\n'.format(ord(word[i])))
                self.fhand.write('call String.appendChar 2\n')        
        elif word in {'false','null'}:
            self.fhand.write('push constant 0\n')
        elif word == 'true':
            self.fhand.write('push constant 1\nneg\n')
        elif word == 'this':
            self.fhand.write('push pointer 0\n')
        else:
            return False
        return True
    
    def compileterm(self):
        if self.writeconstant():
            return
        elif self.cur() in {'~','-'}:
            if self.cur() == '~':
                _op = 'not\n'
            else:
                _op = 'neg\n'
            self.compileterm()
            self.fhand.write(_op)
        elif self.cur() == '(':
            self.index += 1
            self.compilexp()
            self.index += 1
        elif self.cur()[0].isalpha() or self.cur()[0] == '_':
            identifier = self.get() 
            if self.cur() == '[':
                self.compilepp(identifier,'push')
                self.index += 1
                self.compilexp()
                self.fhand.write('add\n')
                self.index += 1
                self.fhand.write('pop pointer 1\n\npush that 0\n')
            else:
                self.index -= 1
                self.subroutinecall()


    def subroutinecall(self):
        identifier = self.get()
        _ismethod = 1
        if self.cur() == '.':
            if identifier in self.subtable:
                _class = self.subtable.get(identifier)[1]
            elif identifier in self.classtable:
                _class = self.classtable.get(identifier)[1]
            else:
                _class = identifier
                _ismethod = 0
            self.index += 1
            _sub = self.get()
        elif self.cur() == '(':
            _class = self.classname
            _sub = identifier
        self.index += 1
        _nargs = self.compilexpl() + _ismethod
        self.fhand.write('call {0}.{1} {2}\n'.format(_class, _sub, _nargs))
        self.index += 1 
        
    def compilexpl(self):
        _nargs = 0
        if self.cur() != ')':
            self.compilexp()
            _nargs += 1
            while self.cur() == ',':
                self.index += 1
                self.compilexp()
                nargs += 1
        return _nargs