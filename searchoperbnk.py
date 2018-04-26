#!user/bin/python
# -*- coding: utf-8 -*-
#Libs Here
from tokensSQL import *
from teamworkmessage import *
from teamworkmessage import *
import pypyodbc as pyodbc
import pymssql
import collections

#Here get the list of that haven't NumProyecto
def search_factura(oper):
    listBills = ''
    sql = 'SELECT [FacturaForta],[ImporteOperacion] FROM [SAP].[dbo].[CobrosConsulting] where OperacionAbono = \'' + str(oper) + '\''
    conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=dbMSSQL)
    cur = conn.cursor()
    cur.execute(sql)
    for values in cur:
        listBills += 'Factura : ' + str(values[0]) + ' Importe : $' + str(values[1]) + '\n'
    conn.commit()
    conn.close()
    return listBills

def searchNullProjects(Table):
    contfield = 0;
    message = 'Hola he examinado la base de datos y pude ver que existen Operaciones de Abono que no estan debidamente registradas.\n'
    message += '\n'
    message += '################################################################\n'
    message += '\t Operaciones en ' + str(Table) + '\n'
    message += '################################################################\n'
    sql = 'SELECT [OperacionAbono],[ImporteOperacion],[Fecha],[Cuenta],[NumProyecto],[Estatus],[NomProyecto],[NumMaestro],[NomMaestro] FROM [SAP].[dbo].[' + str(Table) + '] Where (NumProyecto Is Null) Order by Cuenta'
    conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=dbMSSQL)
    cur = conn.cursor()
    cur.execute(sql)
    for value in cur:
        OperacionAbono = value[0]
        ImporteOperacion = value[1]
        message += 'Operacion : ' + str(OperacionAbono) + ' Importe Operacion : $' + str(ImporteOperacion) + ' Fecha :' + str(value[2]) + '\n'
        message += 'Facturas para esta operacion\n'
        message += search_factura(OperacionAbono)
        contfield += 1
    conn.commit()
    conn.close()
    message += "################################################################\n"
    message += "\n"
    message += "Estas operaciones tiene factura que podrina no corresponder a la operacion.\n"
    message += "Saludos.\n"
    if contfield >= 1:
        #Send Message
        Title = 'Hola, he encontrado operaciones de abono'
        #IdTeamWorkUsersList = '216004,270823,259573'
        IdTeamWorkUsersList = '216004'
        send_private_messaje(title=Title,IdTeamWorkUsers=IdTeamWorkUsersList,IdTeamWorkProject='418014',message=message,notify=IdTeamWorkUsersList)
        print(message)
    else:
        print ('Vacio')

    #return message

################################################################################
##                                                                            ##
##                                                                            ##
##                              Test                                          ##
##                                                                            ##
##                                                                            ##
################################################################################

print(searchNullProjects('RV-VentasCobradasXProyecto'))
