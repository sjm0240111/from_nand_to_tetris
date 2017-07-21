 # -*- coding: utf-8 -*-
"""
Spyder Editor

@author: John Lee
"""

pushcmd = dict()
pushcmd['local']='@{0}\nD=A\n@R1\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['argument']='@{0}\nD=A\n@R2\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['this']='@{0}\nD=A\n@R3\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['that']='@{0}\nD=A\n@R4\nA=M\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['temp']='@{0}\nD=A\n@5\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['static']='@{1}.{0}\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['pointer']='@{0}\nD=A\n@R3\nA=D+A\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'
pushcmd['constant']='@{0}\nD=A\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'

popcmd = dict()
popcmd['local'] = '@{0}\nD=A\n@R1\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['argument'] = '@{0}\nD=A\n@R2\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['this'] = '@{0}\nD=A\n@R3\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['that'] = '@{0}\nD=A\n@R4\nD=D+M\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['temp'] = '@{0}\nD=A\n@5\nD=D+A\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
popcmd['static'] = '@R0\nM=M-1\nA=M\nD=M\n@{1}.{0}\nM=D\n'
popcmd['pointer'] = '@{0}\nD=A\n@R3\nD=D+A\n@R13\nM=D\n@R0\nM=M-1\nA=M\nD=M\n'\
+'@R13\nA=M\nM=D\n'
    
alcmd = dict()
alcmd['add'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=D+M\n'
alcmd['sub'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D\n'
alcmd['neg'] = '@R0\nA=M\nA=A-1\nM=-M\n'
alcmd['and'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=D&M\n'
alcmd['or'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nM=D|M\n'
alcmd['not'] = '@R0\nA=M\nA=A-1\nM=!M\n'
alcmd['eq'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\nM=-1\n@EQ.{0}.{1}\n'\
+'D;JEQ\n@R0\nA=M\nA=A-1\nM=0\n(EQ.{0}.{1})\n'
alcmd['gt'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\nM=-1\n@GT.{0}.{1}\n'\
+'D;JGT\n@R0\nA=M\nA=A-1\nM=0\n(GT.{0}.{1})\n'
alcmd['lt'] = '@R0\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\nM=-1\n@LT.{0}.{1}\n'\
+'D;JLT\n@R0\nA=M\nA=A-1\nM=0\n(LT.{0}.{1})\n'

branchcmd = dict()
branchcmd['label'] = '({0}${1})\n'
branchcmd['goto'] = '@{0}${1}\n0;JMP\n'
branchcmd['if-goto'] ='@R0\nM=M-1\nA=M\nD=M\n@{0}${1}\nD;JNE\n'

funcmd = dict()
funcmd['call'] = '@ret.{0}.{2}\nD=A\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R1\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R2\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R3\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@R4\nD=M\n@R0\nA=M\nM=D\n@R0\nM=M+1\n'\
+'@{1}\nD=A\n@5\nD=D+A\n@R0\nD=M-D\n@R2\nM=D\n'\
+'@R0\nD=M\n@R1\nM=D\n@{0}\n0;JMP\n(ret.{0}.{2})\n'

#push return-address // (Using the label declared below)
#push LCL // Save LCL of the calling function
#push ARG // Save ARG of the calling function
#push THIS // Save THIS of the calling function
#push THAT // Save THAT of the calling function
#ARG = SP-n-5 // Reposition ARG (n = number of args.)
#LCL = SP // Reposition LCL
#goto f // Transfer control
#(return-address) // Declare a label for the return-address

funcmd['function'] = '({0})\n@{1}\nD=A\n@nolcl.{0}\nD;JEQ\n(createlcl.{0})\n'\
+'@R0\nA=M\nM=0\n@R0\nM=M+1\nD=D-1\n@createlcl.{0}\nD;JGT\n(nolcl.{0})\n'

#(f) // Declare a label for the function entry
#repeat k times: // k = number of local variables
#PUSH 0 // Initialize all of them to 0

#funcmd['return'] = '@R1\nD=M\n@R14\nM=D\n'\
#+'@5\nA=D-A\nD=M\n@R15\nM=D\n'\

funcmd['return'] = '@5\nD=A\n@R1\nA=M-D\nD=M\n@R15\nM=D\n'\
+'@R0\nA=M-1\nD=M\n@R2\nA=M\nM=D\n'\
+'@R2\nD=M+1\n@R0\nM=D\n'\
+'@R1\nM=M-1\nA=M\nD=M\n@R4\nM=D\n'\
+'@R1\nM=M-1\nA=M\nD=M\n@R3\nM=D\n'\
+'@R1\nM=M-1\nA=M\nD=M\n@R2\nM=D\n'\
+'@R1\nM=M-1\nA=M\nD=M\n@R1\nM=D\n'\
+'@R15\nA=M\n0;JMP\n'

#funcmd['return'] = '@R1\nD=M\n@R13\nM=D\n'\
#+'@R0\nA=M-1\nD=M\n@R2\nA=M\nM=D\n'\
#+'@R2\nD=M+1\n@R0\nM=D\n'\
#+'@R13\nM=M-1\nA=M\nD=M\n@R4\nM=D\n'\
#+'@R13\nM=M-1\nA=M\nD=M\n@R3\nM=D\n'\
#+'@R13\nM=M-1\nA=M\nD=M\n@R2\nM=D\n'\
#+'@R13\nM=M-1\nA=M\nD=M\n@R1\nM=D\n'\
#+'@R13\nM=M-1\nA=M\nA=M\n0;JMP\n'

#funcmd['return'] = '@5\nD=A\n@R1\nA=M-D\nD=M\n@R15\nM=D\n'\
#FRAME = LCL // FRAME is a temporary variable
#RET = *(FRAME-5) // Put the return-address in a temp. var.
#*ARG = pop() // Reposition the return value for the caller
#SP = ARG+1 // Restore SP of the caller
#THAT = *(FRAME-1) // Restore THAT of the caller
#THIS = *(FRAME-2) // Restore THIS of the caller
#ARG = *(FRAME-3) // Restore ARG of the caller
#LCL = *(FRAME-4) // Restore LCL of the caller
#goto RET // Goto return-address (in the caller’s code)

