#!/usr/bin/env python3

bgp_peer_list = ['192.168.1.1']

output = """
Wed Apr  1 23:23:41.605 MDT
BGP VRF INET, state: Active
BGP Route Distinguisher: 65535:1
VRF ID: 0x60000002
BGP router identifier 192.168.1.2, local AS number 65535
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000011   RD version: 8233
BGP main routing table version 8253
BGP NSR Initial initsync version 188 (Reached)
BGP NSR/ISSU Sync-Group versions 8253/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker            8253       8253       8253       8253        8253        8253

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
192.168.1.1    0  65534  302905  302928     8253    0    0     2w0d          1
"""
#print(output)
dict1 = output.splitlines()
dict2 = {}
dict2 = dict1[19].splitlines()
bgp_peer_Table = {}
#for line in output.splitlines():
#    if any(x in line for x in bgp_peer_list):
#        print(line)


for key in bgp_peer_list:
    #print(key)
    for search in dict2:
        bgp_peer_Table.update(key, search[8])
        if key in search:
            print(f"{key} is in this list")
print(bgp_peer_Table)
