// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    @R2
    M=0
    @i
    M=1  // initialize variables R2 = 0, i=1
    
    @R0
    D=M
    @NEGATIVE  // if (R1<0) negative loop
    D;JLT
    @END  // if (R1==0) end
    D;JEQ 
(LOOP)
    @R1
    D=M
    @R2
    M=D+M  //R2=R2+R1
    
    @i
    M=M+1  //i=i+1
    D=M
    @R0
    D=M-D  //R0-i
    
    @LOOP
    D;JGE
    @END
    0;JMP
    
(NEGATIVE)    
    @R1
    D=M
    @R2
    M=M-D  //R2=R2+R1
    
    @i
    M=M+1  //i=i+1
    D=M
    @R0
    D=D+M  //i+R0
    
    @NEGATIVE
    D;JLE
    
(END)    
    @END
    0;JMP