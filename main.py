#!user/bin/python
# -*- coding: utf-8 -*-
#Libs Here
from tokensSQL import *
from tokensTeamWork  import *
from searchbills import *
from searchoperbnk import *
from teamworkmessage import *
import pypyodbc as pyodbc
import pymssql
import collections


################################################################################
##                                                                            ##
##                                                                            ##
##                              Code here                                     ##
##                                                                            ##
################################################################################

#get message Here
msj = ''
listas = getlist_bills('2010-01-01')
msj = compareList(listas)

if  msj.strip():
    print (msj)
    #send notification to usres
    Title = 'Hola, he encontrado facturas duplicadas'
    IdTeamWorkUsersList = '216004,270823,259573'
    #IdTeamWorkUsersList = '216004'
    send_private_messaje(title=Title,IdTeamWorkUsers=IdTeamWorkUsersList,IdTeamWorkProject='418014',message=msj,notify=IdTeamWorkUsersList)
else:
    print ('Esta vacio')

searchNullProjects('RV-VentasCobradasXProyecto')
