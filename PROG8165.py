>>> s=8093
>>> d=7798
>>> SHEX=hex(s)
>>> SHEX
'0x1f9d'
>>> DHEX=hex(d)
>>> DHEX
'0x1e76'
>>> SHEX+DHEX
'0x1f9d0x1e76'
>>> SHEX+DHEX+'00000000 00000000'+'50020010'
'0x1f9d0x1e7600000000 0000000050020010'
