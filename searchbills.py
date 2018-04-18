#!user/bin/python
# -*- coding: utf-8 -*-
#Libs Here
from tokensSQL import *
from tokensNotification import *
from notifications import *
import pypyodbc as pyodbc
import pymssql

#here gets a list of all bills of MSSQL

def getlist_bills(dateCompare):
    listbills = []
    k = 0
    sql = 'SELECT [FacturaForta] FROM [SAP].[dbo].[FacturacionConsulting] Where FacturaForta not like '%*%' and [Fecha Factura] >= \'' + str(dateCompare) + '\''
    conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=dbMSSQL)
    cur = conn.cursor()
    cur.execute(sql)
    for value in cur:
        Id_Opers = value[0]
        listBnk.insert(k,str(Id_Opers))
    conn.commit()
    conn.close()
    return listbills


################################################################################
##                                                                            ##
##                                  Test                                      ##
##                                                                            ##
################################################################################

print(getlist_bills('2013-01-01'))
