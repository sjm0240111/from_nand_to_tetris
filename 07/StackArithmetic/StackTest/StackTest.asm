@17
D=A
@R0
A=M
M=D
@R0
M=M+1
@17
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@EQ.3
D;JEQ
@R0
A=M
A=A-1
M=0
(EQ.3)
@17
D=A
@R0
A=M
M=D
@R0
M=M+1
@16
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@EQ.6
D;JEQ
@R0
A=M
A=A-1
M=0
(EQ.6)
@16
D=A
@R0
A=M
M=D
@R0
M=M+1
@17
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@EQ.9
D;JEQ
@R0
A=M
A=A-1
M=0
(EQ.9)
@892
D=A
@R0
A=M
M=D
@R0
M=M+1
@891
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@LT.12
D;JLT
@R0
A=M
A=A-1
M=0
(LT.12)
@891
D=A
@R0
A=M
M=D
@R0
M=M+1
@892
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@LT.15
D;JLT
@R0
A=M
A=A-1
M=0
(LT.15)
@891
D=A
@R0
A=M
M=D
@R0
M=M+1
@891
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@LT.18
D;JLT
@R0
A=M
A=A-1
M=0
(LT.18)
@32767
D=A
@R0
A=M
M=D
@R0
M=M+1
@32766
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@GT.21
D;JGT
@R0
A=M
A=A-1
M=0
(GT.21)
@32766
D=A
@R0
A=M
M=D
@R0
M=M+1
@32767
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@GT.24
D;JGT
@R0
A=M
A=A-1
M=0
(GT.24)
@32766
D=A
@R0
A=M
M=D
@R0
M=M+1
@32766
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@GT.27
D;JGT
@R0
A=M
A=A-1
M=0
(GT.27)
@57
D=A
@R0
A=M
M=D
@R0
M=M+1
@31
D=A
@R0
A=M
M=D
@R0
M=M+1
@53
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M
@112
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
M=M-D
@R0
A=M
A=A-1
M=-M
@R0
M=M-1
A=M
D=M
A=A-1
M=D&M
@82
D=A
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
A=A-1
M=D|M
@R0
A=M
A=A-1
M=!M
