@256
D=A
@R0
M=D
@Sys.init
0;JMP
(Class1.set)
@0
D=A
(createlcl.Class1.set)
@R0
A=M
M=0
@R0
M=M+1
D=D-1
@createlcl.Class1.set
D;JGT
@0
D=A
@R2
A=M
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
@.vm.0
M=D
@1
D=A
@R2
A=M
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
@.vm.1
M=D
@0
D=A
@R0
A=M
M=D
@R0
M=M+1
@R1
D=M
@R13
M=D
@R0
A=M-1
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@R13
M=M-1
A=M
D=M
@R4
M=D
@R13
M=M-1
A=M
D=M
@R3
M=D
@R13
M=M-1
A=M
D=M
@R2
M=D
@R13
M=M-1
A=M
D=M
@R1
M=D
@R13
M=M-1
A=M
0;JMP
(Class1.get)
@0
D=A
(createlcl.Class1.get)
@R0
A=M
M=0
@R0
M=M+1
D=D-1
@createlcl.Class1.get
D;JGT
@.vm.0
D=M
@R0
A=M
M=D
@R0
M=M+1
@.vm.1
D=M
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
@R1
D=M
@R13
M=D
@R0
A=M-1
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@R13
M=M-1
A=M
D=M
@R4
M=D
@R13
M=M-1
A=M
D=M
@R3
M=D
@R13
M=M-1
A=M
D=M
@R2
M=D
@R13
M=M-1
A=M
D=M
@R1
M=D
@R13
M=M-1
A=M
0;JMP
(Class2.set)
@0
D=A
(createlcl.Class2.set)
@R0
A=M
M=0
@R0
M=M+1
D=D-1
@createlcl.Class2.set
D;JGT
@0
D=A
@R2
A=M
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
@.vm.0
M=D
@1
D=A
@R2
A=M
A=D+A
D=M
@R0
A=M
M=D
@R0
M=M+1
@R0
M=M-1
A=M
D=M
@.vm.1
M=D
@0
D=A
@R0
A=M
M=D
@R0
M=M+1
@R1
D=M
@R13
M=D
@R0
A=M-1
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@R13
M=M-1
A=M
D=M
@R4
M=D
@R13
M=M-1
A=M
D=M
@R3
M=D
@R13
M=M-1
A=M
D=M
@R2
M=D
@R13
M=M-1
A=M
D=M
@R1
M=D
@R13
M=M-1
A=M
0;JMP
(Class2.get)
@0
D=A
(createlcl.Class2.get)
@R0
A=M
M=0
@R0
M=M+1
D=D-1
@createlcl.Class2.get
D;JGT
@.vm.0
D=M
@R0
A=M
M=D
@R0
M=M+1
@.vm.1
D=M
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
@R1
D=M
@R13
M=D
@R0
A=M-1
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@R13
M=M-1
A=M
D=M
@R4
M=D
@R13
M=M-1
A=M
D=M
@R3
M=D
@R13
M=M-1
A=M
D=M
@R2
M=D
@R13
M=M-1
A=M
D=M
@R1
M=D
@R13
M=M-1
A=M
0;JMP
(Sys.init)
@0
D=A
(createlcl.Sys.init)
@R0
A=M
M=0
@R0
M=M+1
D=D-1
@createlcl.Sys.init
D;JGT
@6
D=A
@R0
A=M
M=D
@R0
M=M+1
@8
D=A
@R0
A=M
M=D
@R0
M=M+1
@ret.Class1.set.11
D=A
@R0
A=M
M=D
@R0
M=M+1
@R1
D=M
@R0
A=M
M=D
@R0
M=M+1
@R2
D=M
@R0
A=M
M=D
@R0
M=M+1
@R3
D=M
@R0
A=M
M=D
@R0
M=M+1
@R4
D=M
@R0
A=M
M=D
@R0
M=M+1
@2
D=A
@5
D=D+A
@R0
D=M-D
@R2
M=D
@R0
D=M
@R1
M=D
@Class1.set
0;JMP
(ret.Class1.set.11)
@0
D=A
@5
D=D+A
@R13
M=D
@R0
M=M-1
A=M
D=M
@R13
A=M
M=D
@23
D=A
@R0
A=M
M=D
@R0
M=M+1
@15
D=A
@R0
A=M
M=D
@R0
M=M+1
@ret.Class2.set.15
D=A
@R0
A=M
M=D
@R0
M=M+1
@R1
D=M
@R0
A=M
M=D
@R0
M=M+1
@R2
D=M
@R0
A=M
M=D
@R0
M=M+1
@R3
D=M
@R0
A=M
M=D
@R0
M=M+1
@R4
D=M
@R0
A=M
M=D
@R0
M=M+1
@2
D=A
@5
D=D+A
@R0
D=M-D
@R2
M=D
@R0
D=M
@R1
M=D
@Class2.set
0;JMP
(ret.Class2.set.15)
@0
D=A
@5
D=D+A
@R13
M=D
@R0
M=M-1
A=M
D=M
@R13
A=M
M=D
@ret.Class1.get.17
D=A
@R0
A=M
M=D
@R0
M=M+1
@R1
D=M
@R0
A=M
M=D
@R0
M=M+1
@R2
D=M
@R0
A=M
M=D
@R0
M=M+1
@R3
D=M
@R0
A=M
M=D
@R0
M=M+1
@R4
D=M
@R0
A=M
M=D
@R0
M=M+1
@0
D=A
@5
D=D+A
@R0
D=M-D
@R2
M=D
@R0
D=M
@R1
M=D
@Class1.get
0;JMP
(ret.Class1.get.17)
@ret.Class2.get.18
D=A
@R0
A=M
M=D
@R0
M=M+1
@R1
D=M
@R0
A=M
M=D
@R0
M=M+1
@R2
D=M
@R0
A=M
M=D
@R0
M=M+1
@R3
D=M
@R0
A=M
M=D
@R0
M=M+1
@R4
D=M
@R0
A=M
M=D
@R0
M=M+1
@0
D=A
@5
D=D+A
@R0
D=M-D
@R2
M=D
@R0
D=M
@R1
M=D
@Class2.get
0;JMP
(ret.Class2.get.18)
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
