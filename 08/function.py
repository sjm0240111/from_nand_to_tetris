 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

funcmd = dict()
funcmd['call'] = '@{}\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R1\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R2\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R3\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R4\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@{0}\nD=A\n@5\nD=D+A\n@R0\nD=M-D\n@R2\nM=D\n'\
+'@R0\nD=M\n@R1\nM=D\n@{1}\n0;JMP\n({})'

#push return-address // (Using the label declared below)
#push LCL // Save LCL of the calling function
#push ARG // Save ARG of the calling function
#push THIS // Save THIS of the calling function
#push THAT // Save THAT of the calling function
#ARG = SP-n-5 // Reposition ARG (n ¼ number of args.)
#LCL = SP // Reposition LCL
#goto f // Transfer control
#(return-address) // Declare a label for the return-address

funcmd['function'] = '({0})\n@{1}\nD=A\n(createlcl.{0})@R0\nA=M\nM=0\n'\
+'@R0\nM=M+1\nD=D-1\nD;JGT\n'

#(f) // Declare a label for the function entry
#repeat k times: // k = number of local variables
#PUSH 0 // Initialize all of them to 0

funcmd['return'] = '@R1\nD=M\n@R13\nM=D\n'\
+'@R0\nA=M-1\nD=M\n@R2\nA=M\nM=D\n'\
+'@R2\nD=M+1\n@R0\nM=D\n'\
+'@R13\nM=M-1\nA=M\nD=M\n@R4\nM=D\n'\
+'@R13\nM=M-1\nA=M\nD=M\n@R3\nM=D\n'\
+'@R13\nM=M-1\nA=M\nD=M\n@R2\nM=D\n'\
+'@R13\nM=M-1\nA=M\nD=M\n@R1\nM=D\n'\
+'@R13\nM=M-1\nA=M\n0;JMP\n'

#FRAME = LCL // FRAME is a temporary variable
#*ARG = pop() // Reposition the return value for the caller
#SP = ARG+1 // Restore SP of the caller
#THAT = *(FRAME-1) // Restore THAT of the caller
#THIS = *(FRAME-2) // Restore THIS of the caller
#ARG = *(FRAME-3) // Restore ARG of the caller
#LCL = *(FRAME-4) // Restore LCL of the caller
#RET = *(FRAME-5) // Put the return-address in a temp. var.
#goto RET // Goto return-address (in the caller’s code)

