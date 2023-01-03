import sys
from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget,\
                         ContextData, ObjectType, ObjectIdentity, getCmd

host=sys.argv[1]
snmp_community=sys.argv[2]+'21'

iterator = getCmd(
    SnmpEngine(),
    CommunityData(snmp_community, mpModel=1),           # mpModel for snmp v2c - value=1
    UdpTransportTarget((host, 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.4.1.20044.45.3.1.17.0'))
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('{} at {}'.format(errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

def return_value():
    for oid, val in varBinds:
        return(str((f'{oid.prettyPrint()} = {val.prettyPrint()}')))

value=return_value()
value=value.replace('SNMPv2-SMI::enterprises.20044.45.3.1.17.0 = ','')

if (value.isdecimal):
    dec_value=int(value)/500
    print(dec_value)
else:
    print(-111111)					# return -111111 as sign of incorrect value 


