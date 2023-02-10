# 0 /home/ubuntu/sr/library/SRgetopt.sr 127+

global SRgetopt

 var optind := 1
 var opterr := true




 const optMAXLEN := 256

 var optarg : string [ optMAXLEN ]




 var optEOF := char ( EOF )

 op getopt ( optstring : string [ * ] ) returns char

 body SRgetopt ; end ;
