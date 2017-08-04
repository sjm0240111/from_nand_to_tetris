# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:57:46 2017

@author: John Lee
"""

keywords = set(['class','constructor','function','method','field','static',\
                'var','int','char','boolean','void','true','false','null',\
                'this','let','do','if','else','while','return'])

symbols = set(['{','}','(',')','[',']','.',',',';','+','-',\
               '*','/','&','|','<','>','=','~'])

nTStart = dict()
nTEnd = dict()
nTStart['class'] ='<class>'
nTEnd['class'] ='</class>'
nTStart['constructor'] ='<subroutineDec>'
nTEnd['constructor'] ='</subroutineDec>'
nTStart['method'] ='<subroutineDec>'
nTEnd['method'] ='</subroutineDec>'
nTStart['function'] ='<subroutineDec>'
nTEnd['function'] ='</subroutineDec>'

nTStart['field'] ='<classVarDec>'
nTEnd['field'] ='</classVarDec>'
nTStart['static'] ='<classVarDec>'
nTEnd['static'] ='</classVarDec>'
nTStart['var'] ='<varDec>'
nTEnd['var'] ='</varDec>'

nTStart['if'] ='<ifStatement>'
nTEnd['if'] ='</ifStatement>'
nTStart['while'] ='<whileStatement>'
nTEnd['while'] ='</whileStatement>'
nTStart['let'] ='<letStatement>'
nTEnd['let'] ='</letStatement>'
nTStart['do'] ='<doStatement>'
nTEnd['do'] ='</doStatement>'
nTStart['return'] ='<returnStatement>'
nTEnd['return'] ='</returnStatement>'