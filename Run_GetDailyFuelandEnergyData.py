import json
import pandas as pd
from pandas import json_normalize
import importlib
from lib import PSDCODAPIFUNCS as psd
# psd = importlib.import_module('PSDCODAPIFUNCS')

### Usernamepassword input format as "username:password" ##
usernamepassword = open('usernamepassword.txt','r')
usernamepassword = usernamepassword.read()
usernamepasswordbase64 = psd.converttobase64(usernamepassword)
token = psd.gettoken(usernamepasswordbase64)

### Date input format as "Date/Month/Year"
startdate = '01/01/2024'
enddate = '31/01/2024'

dt_dailyfueldata = psd.importdailyfuel(startdate,enddate,token)
dt_dailyfueldata.to_csv('Output\\'+'DailyFuelData_'+startdate.replace('/','-')+'_to_'+enddate.replace('/','-')+'.csv',encoding="utf-8-sig",index=False)

dt_dailyenergycompare = psd.importdailyenergy(startdate,enddate,token)
dt_dailyenergycompare.to_csv('Output\\''DailyEnergyData_'+startdate.replace('/','-')+'_to_'+enddate.replace('/','-')+'.csv',encoding="utf-8-sig",index=False)