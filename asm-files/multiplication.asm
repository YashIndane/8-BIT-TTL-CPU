0x0 lda 0xe
0x1 sub 0xc
0x2 jc  0x6
0x3 lda 0xd
0x4 out
0x5 hlt
0x6 sta 0xe
0x7 lda 0xd
0x8 add 0xf
0x9 sta 0xd
0xa jmp 0x0
0xb 0x00
0xc 0x01
0xd 0x00
0xe X
0xf Y
