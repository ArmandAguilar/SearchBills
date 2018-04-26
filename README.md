# SearchBills

> This script search all bills that be duplicate in the table [FacturacionConsulting] (that be in MSSQL)  other function the can to do is detected if exit a bad register in the la table  [CobrosConsulting], if exist any problems the script send a notify by Teamwork to administrative team.

### Tools used in this project

- Python 2.7.11
- pypyodbc as pyodbc
- pymssql
- collections

### Descriptions of scripts

**Main** : This file run the main function..

**searchbills** : This script serach bills that be duplicate.

**searchoperbnk** : This script search operation bad register or bill that don't existe in FacturacionConsulting but have a field in CobrosConsulting.

**teamworkmessage** : This script is used for send notify the platform teamwork.

**Tokes (tokensTeamWork,tokensSQL)** : this files have access (users,passwords and tokens).



![How is works](https://github.com/ArmandAguilar/searchbills/blob/master/Diagrama/Diagrama.png)
