Assembler <- function(fname) {
    library(stringr)
    fhand <- file(fname)
    lines <- readLines(fhand)
    lwc <- sub("//(.*)", "", lines)  #lwc means line without comment
    lwc <- str_trim(lwc)
    lt <- lwc[nchar(lwc)>0]          #lt means line trimmed
    
    lbidx <- grep("^\\(", lt)
    if (length(lbidx)==0){
        lwol <- lt
    } else{
        lwol <- lt[-lbidx]               #line without labels
    }
    symboltable <- addlabel(lbidx, lt)
    
    ramad = 16
    i=1
    stname <- names(symboltable)
    binarycode <- rep(NA, times=length(lwol))
    for (ln in lwol) {
        if(substr(ln,1,1)=="@"){
            lb <- sub("@","",ln)
            if (grepl("^[0-9]",lb)) {
                address <- lb
            } else {
                idx <- which(symboltable$Label==lb)
                if(length(idx)==0){
                    symboltable <- addvariable(lb,ramad,symboltable)
                    address <- ramad
                    ramad = ramad + 1 
                } else {
                    address <- symboltable[idx,2]
                }
            }
            instruction <-substr(paste(rev(as.integer(intToBits(as.integer(address)))), collapse=""),17,32)
        } else {
            if(grepl("=",ln)){
                ln2 <- unlist(strsplit(ln,"="))
                dst <- ln2[1]
                cj <- ln2[2]
            } else{
                dst <- "null"
                cj <- ln
            }
            
            if(grepl(";",cj)){
                cj2<- unlist(strsplit(cj,";"))
                cmp <- cj2[1]
                jmp <- cj2[2]
            } else{
                cmp <- cj
                jmp <- "null"
            }
            instruction <- paste0("111", comptbl[comptbl[,1]==cmp,2],
                       desttbl[desttbl[,1]==dst,2], jumptbl[jumptbl[,1]==jmp,2])
        }
        binarycode[i] <- instruction
        i = i+1
    }
    codename <-sub("asm","hack",fname)
    write.table(binarycode,codename,quote = FALSE,row.names = FALSE,col.names = FALSE)
    close(fhand)
}

addlabel <- function(index, lines) {
    lbls <-lines[index]
    lb <- substr(lbls, 2, nchar(lbls)-1)
    extraidx <- 1:length(index)
    tableidx <- index - extraidx
    labeltable <- data.frame(lb, tableidx)
    names(labeltable) <- names(symboltbl)
    rbind(symboltbl, labeltable)
}

addvariable <- function(lb,idx,symboltable){
    newvariable <- data.frame(lb,idx)
    names(newvariable) <- stname
    rbind(symboltable,newvariable)
}