# Ekinops--TRFAN-module-voltage

For correct use is required library "pysnmp" -> https://pypi.org/project/pysnmp/

Scripts are use as external check in zabbix for get TRFAN voltage DWDM Ekinops C600HC. If you want use in zabbix move this scripts to:/usr/lib/zabbix/externalscripts and configure item.

get_trfanMesrvoltMeas12v1.py - for TRFAN power line A (main line)
get_trfanMesrvoltMeas12v2.py - for TRFAN power line B (backup line)

For request about voltage is OIDs used:
1.3.6.1.4.1.20044.45.3.1.16.0 -TRFAN power line A
1.3.6.1.4.1.20044.45.3.1.17.0 -TRFAN power line B

Both OID from official Ekinops Docs for C600HC


Script default using v2c version SNMP

Script take 2 arguments in command line: get_chassis_temp.py <HOST_IP> <SNMP_COMMUNITY> 

Where:

<HOST_IP> - IP address your Ekinops device
<SNMP_COMMUNITY> - SNMP Community for Ekinops device (default in v2c verion in use)