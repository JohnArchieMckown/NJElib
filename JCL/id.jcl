//H4CKRNJE JOB (JOBNAME),'exec id in uss',CLASS=A,
//             MSGLEVEL=(0,0),MSGCLASS=K,NOTIFY=&SYSUID
/*XEQ    NEWYORK
//*
//UNIXCMD  EXEC PGM=BPXBATCH
//*
//STDIN     DD SYSOUT=*
//STDOUT    DD SYSOUT=*
//STDPARM   DD *
sh id;who;uname -a