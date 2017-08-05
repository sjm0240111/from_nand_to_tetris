# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:57:46 2017

@author: John Lee
"""

keywords = set(['class','constructor','function','method','field','static',\
                'var','int','char','boolean','void','true','false','null',\
                'this','let','do','if','else','while','return'])
structure = set(['class','constructor','function','method',\
                 'let','do','if','else','while','return'])
subroutine = set(['constructor','function','method'])
statements = set(['let','do','if','else','while','return'])
variable = set(['field','static','var'])
symbols = set(['{','}','(',')','[',']','.',',',';','+','-',\
               '*','/','&','|','<','>','=','~'])

nTStart = dict()
nTEnd = dict()
nTStart['class'] ='<class>'
nTEnd['class'] ='</class>\n'
nTStart['constructor'] ='<subroutineDec>'
nTEnd['constructor'] ='</subroutineDec>\n'
nTStart['method'] ='<subroutineDec>'
nTEnd['method'] ='</subroutineDec>\n'
nTStart['function'] ='<subroutineDec>'
nTEnd['function'] ='</subroutineDec>\n'

nTStart['field'] ='<classVarDec>'
nTEnd['field'] ='</classVarDec>\n'
nTStart['static'] ='<classVarDec>'
nTEnd['static'] ='</classVarDec>\n'
nTStart['var'] ='<varDec>'
nTEnd['var'] ='</varDec>\n'

nTStart['if'] ='<ifStatement>'
nTEnd['if'] ='</ifStatement>\n'
nTStart['else'] =''
nTEnd['else'] =''
nTStart['while'] ='<whileStatement>'
nTEnd['while'] ='</whileStatement>\n'
nTStart['let'] ='<letStatement>'
nTEnd['let'] ='</letStatement>\n'
nTStart['do'] ='<doStatement>'
nTEnd['do'] ='</doStatement>\n'
nTStart['return'] ='<returnStatement>'
nTEnd['return'] ='</returnStatement>\n'

nTStart['field'] ='<classVarDec>\n'
nTEnd['field'] ='</classVarDec>\n'
nTStart['static'] ='<classVarDec>\n'
nTEnd['static'] ='</classVarDec>\n'
nTStart['var'] ='<varDec>\n'
nTEnd['var'] ='</varDec>\n'