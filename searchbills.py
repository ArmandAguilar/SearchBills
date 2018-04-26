#!user/bin/python
# -*- coding: utf-8 -*-
#Libs Here
from tokensSQL import *
from teamworkmessage import *
from teamworkmessage import *
import pypyodbc as pyodbc
import pymssql
import collections

#here gets a list of all bills of MSSQL

def getlist_bills(dateCompareStart):
    listbills = []
    k = 0
    sql = 'SELECT [FacturaForta] FROM [SAP].[dbo].[FacturacionConsulting] Where FacturaForta not like \'%*%\' and [Fecha TENTATIVA de pago] >= \'' + str(dateCompareStart) + '\''
    conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=dbMSSQL)
    cur = conn.cursor()
    cur.execute(sql)
    for value in cur:
        Factura = value[0]
        listbills.insert(k,str(Factura))
    conn.commit()
    conn.close()
    return listbills

def compareList(listbils):

    list1 = listbils
    doubleBills = []
    exist = 0
    i = 0
    message = 'Hola he examinado la base de datos y pude ver que existen Facturas que estan duplicadas te muestro un listado.\n'
    message += '\n'
    message += '################################################################\n'
    message += '\t Facturas Duplicadas Encontradas \n'
    message += '################################################################\n'
    doubleBills =  [x for x, y in collections.Counter(list1).items() if y > 1]
    for value in doubleBills:
        message += ' Factura :'+ value +'\n'
    message += "################################################################\n"
    message += "\n"
    message += "Saludos."
    return message

################################################################################
##                                                                            ##
##                                  Test                                      ##
##                                                                            ##
################################################################################

#listas = getlist_bills('2013-01-01')
#print (compareList(listas))
