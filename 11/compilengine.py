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
        self.nfield = 0
        
    def get(self):
        self.index += 1
        return self.tokens[self.index-1]
        
    def cur(self):
        return self.tokens[self.index]
            
    def compileClass(self):
        if not self.get() == 'class':
            return
        self.classname = self.get()
        #print(self.classname)
        self.index += 1    
        self.compilecvd()
        self.compilesub()
        self.index += 1
        #print(len(self.tokens))
        #print(self.index)
        if self.index == len(self.tokens):
            print('compile successfully!')
    
    def compilecvd(self):
        _fidx = 0
        _sidx = 0
        _vkind = self.cur()
        while _vkind in {'field','static'}:               #field int wall,wall2;
            if _vkind == 'field': 
                self.index += 1
                _vtype = self.get()                                     # int
                self.classtable[self.get()] = (_vtype, 'this', _fidx)   # wall
                _fidx += 1
                while self.get() == ',':                                   # ,
                    self.classtable[self.get()] = (_vtype, 'this', _fidx)  # wall2
                    _fidx += 1
            else:    
                self.index += 1
                _vtype = self.get()
                self.classtable[self.get()] = (_vtype, _vkind, _sidx)
                _sidx += 1
                while self.get() == ',':
                    self.classtable[self.get()] = (_vtype, _vkind, _sidx)
                    _sidx += 1
            _vkind = self.cur()
        self.nfield = _fidx
        #print(self.classtable)
        #print(_vkind)
        
    def compilesub(self):                                              # method void dispose() { }       
        _subroutine = self.cur()
        print(_subroutine)
        while _subroutine in {'constructor','function','method'}:
            self.subtable = dict()
            _ismethod = 0
            self.index += 2                                            # jump method void
            function = self.classname + '.' +self.get()                # dispose
            #print(function)
            if _subroutine == 'method':
                self.subtable['this'] = (self.classname,'argument',0)
                _ismethod = 1
            self.index += 1                                            # (
            self.compilepml(_ismethod)               # compile arguments
            
            self.index += 2                                  # ){
            #print(self.cur())
            _nlcls = self.compilevar()                       # compile local variables
            self.fhand.write('function {0} {1}\n'.format(function, _nlcls))
            if _subroutine == 'constructor':
                self.fhand.write('push constant {}\n'.format(self.nfield))
                self.fhand.write('call Memory.alloc 1\npop pointer 0\n')
            if _subroutine == 'method':
                self.fhand.write('push argument 0\npop pointer 0\n')
            
            self.compilestm()                                # compile statements
            self.index += 1                                  # }
            _subroutine = self.cur()
            #print(self.subtable)
            
    def compilepml(self,ismtd):                         # compile parameterlist
        _argidx = ismtd
        _vtype = self.cur()
        if _vtype != ')':
            self.index += 1
            self.subtable[self.get()] = (_vtype, 'argument', _argidx)
            _argidx +=1  
            while self.cur() == ',':
                self.index += 1
                _vtype = self.get()
                self.subtable[self.get()] = (_vtype, 'argument', _argidx)
                _argidx +=1                        
        
    def compilevar(self):
        _vidx = 0
        _vkind = self.cur()                           #var int wall;
        while _vkind == 'var':                            
            self.index += 1
            _vtype = self.get()                                     # int
            self.subtable[self.get()] = (_vtype, 'local', _vidx)   # wall
            _vidx += 1
            while self.get() == ',':                                   # ,
                self.subtable[self.get()] = (_vtype, 'local', _vidx)  # wall2
                _vidx += 1
            _vkind = self.cur()
        print(self.subtable)
        return(_vidx)
        
        
    def compilestm(self):
        _stm = self.cur()
        while _stm in {'let','do','if','while','return'}:
            if _stm == 'let':
                self.compilelet()
            elif _stm == 'do':
                self.compiledo()
            elif _stm == 'if':
                self.compileif()
            elif _stm == 'while':
                self.compilewhile()
            else:
                self.compilereturn()
            _stm = self.cur()
            #print(_stm)
                
    def compilepp(self, name, action):                                     # compile push and pop
        varinfo = self.subtable.get(name, self.classtable.get(name,self.classname))
        self.fhand.write('{0} {1} {2}\n'.format(action, varinfo[1], varinfo[2]))
        
    def compilelet(self):
        self.index += 1
        _identifier = self.get()
        #print(_identifier)            
        if self.cur() == '[':
            self.compilepp(_identifier,'push')
            self.index += 1
            self.compilexp()
            self.fhand.write('add\n')
            self.index += 2
            self.compilexp()
            self.fhand.write('pop temp 0\npop pointer 1\npush temp 0\npop that 0\n')
        elif self.cur() == '=':
            self.index += 1
            self.compilexp()
            self.compilepp(_identifier,'pop')
        self.index += 1

        
    def compiledo(self):
        self.index += 1
        self.subroutinecall()
        self.fhand.write('pop temp 0\n')
        self.index += 1   
        
    def compileif(self):
        _labelif = 'ifexp.{}'.format(self.index)
        _labelelse = 'elsexp.{}'.format(self.index)
        self.index += 2
        self.compilexp()
        self.fhand.write('not\nif-goto {}\n'.format(_labelif))
        self.index += 2
        self.compilestm()
        self.index += 1
        if self.cur() == 'else':
            self.fhand.write('goto {0}\nlabel {1}\n'.format(_labelelse, _labelif))
            self.index += 2
            self.compilestm()
            self.index += 1
            self.fhand.write('label {}\n'.format(_labelelse))
        else:
            self.fhand.write('label {}\n'.format(_labelif))
        
    def compilewhile(self):
        _labelyes = 'while.{}'.format(self.index)
        _labelno = 'cycle.{}'.format(self.index)
        self.fhand.write('label {}\n'.format(_labelno))
        self.index += 2
        self.compilexp()
        self.index += 2
        self.fhand.write('not\nif-goto {}\n'.format(_labelyes))
        self.compilestm()
        self.index += 1
        self.fhand.write('goto {0}\nlabel {1}\n'.format(_labelno, _labelyes))
        
    def compilereturn(self):
        self.index += 1
        if self.cur() != ';':
            self.compilexp()
        else:
            self.fhand.write('push constant 0\n')
        self.fhand.write('return\n')
        self.index += 1
        #print('returned{}'.format(self.cur()))
        
    def compilexp(self):
        self.compileterm()
        _op = self.cur()
        while _op in self.operations:
            self.index += 1
            self.compileterm()
            self.fhand.write(self.operations.get(_op)+'\n')
            _op = self.cur()

    def writeconstant(self):
        _word = self.cur()
        if _word.isnumeric():
            self.fhand.write('push constant {}\n'.format(_word))
        elif _word.startswith('"'):
            _word = _word.strip('"')
            self.fhand.write('push constant {}\ncall String.new 1\n'.format(len(_word)))
            i = 0  
            while i< len(_word):
                self.fhand.write('push constant {}\n'.format(ord(_word[i])))
                self.fhand.write('call String.appendChar 2\n') 
                i += 1
        elif _word in {'false','null'}:
            self.fhand.write('push constant 0\n')
        elif _word == 'true':
            self.fhand.write('push constant 0\nnot\n')
        elif _word == 'this':
            self.fhand.write('push pointer 0\n')         
        else: 
            return False
        self.index += 1
        return True
    
    def compileterm(self):
        if self.writeconstant():
            return
        elif self.cur() in {'~','-'}:
            if self.get() == '~':
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
            _identifier = self.get() 
            if self.cur() == '[':
                self.compilepp(_identifier,'push')
                self.index += 1
                self.compilexp()
                self.fhand.write('add\n')
                self.index += 1
                self.fhand.write('pop pointer 1\npush that 0\n')
            elif self.cur() in {'(','.'}:
                self.index -= 1
                self.subroutinecall()  
            else:
                self.compilepp(_identifier,'push')

    def subroutinecall(self):
        _identifier = self.get()                           # SquareGame.new(expl)
        _ismethod = 1
        if self.cur() == '.':
            if _identifier in self.subtable:                     # local var method
                _class = self.subtable.get(_identifier)[0]
                self.compilepp(_identifier,'push')
            elif _identifier in self.classtable:                 # class var method
                _class = self.classtable.get(_identifier)[0]
                self.compilepp(_identifier,'push')
            else:                                                # a function
                _class = _identifier
                _ismethod = 0
            self.index += 1                                # .
            _sub = self.get()                              # new
        elif self.cur() == '(':                                  #  this object method
            _class = self.classname
            _sub = _identifier
            self.fhand.write('push pointer 0\n')
        self.index += 1
        _nargs = self.compilexpl() + _ismethod             # expl
        self.fhand.write('call {0}.{1} {2}\n'.format(_class, _sub, _nargs))
        self.index += 1        # )
        #print(self.cur())
        
    def compilexpl(self):
        _nargs = 0
        if self.cur() != ')':
            self.compilexp()
            _nargs += 1
            while self.cur() == ',':
                self.index += 1
                self.compilexp()
                _nargs += 1
        return _nargs