#!/usr/bin/sudo python
# ===========================================================================

#  This script make a data bin to write some data at some sector

# REFERENCES

#  $DateTime: 2017/07/10 10:33:00 $
#  $Author: jaehyek.choi

# when          who            what, where, why
# --------      ---           -------------------------------------------------------
# 2017-07-10    jaehyek        First made.

import struct


file_blockinfo = "blockinfo.bin"
file_blockdata = "blockdata.bin"

sectorno_blockinfo = 508928
sectorlen_blockinfo = 2
sectorno_blockdata = 508930
sectorlen_blockdata = 10

SECTOR_SIZE = 512

def make_sector_blockinfo():
    " make a bin file for bloclinfo"
    len_empty = SECTOR_SIZE*sectorlen_blockinfo - struct.calcsize("<ll")

    listtemp = [sectorno_blockdata, sectorlen_blockdata] +  [0x00]* len_empty

    no = struct.calcsize("<ll%dB"%(len_empty) )

    bytes = struct.pack("<ll%dB"%(len_empty), *listtemp )

    open(file_blockinfo, "wb").write(bytes)

def make_sector_blockdata():
    "make a bin file for blockdata"

    msg = b'hello world\n'
    bytes_msg = struct.unpack("<%dB"%(len(msg)), msg)

    len_empty = SECTOR_SIZE*sectorlen_blockdata - len(bytes_msg)
    listtemp = list(bytes_msg) + [0x00] * len_empty

    bytes = struct.pack("<%sB"%(SECTOR_SIZE*sectorlen_blockdata),*listtemp  )

    open(file_blockdata, "wb").write(bytes)

if __name__ == "__main__" :
    make_sector_blockinfo()
    make_sector_blockdata()