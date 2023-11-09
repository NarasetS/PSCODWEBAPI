import PSDCODAPIFUNCS as psd
import json
import pandas as pd
from pandas import json_normalize

### Usernamepassword input format as "username:password" ##
usernamepassword = open('usernamepassword.txt','r')
usernamepassword = usernamepassword.read()
usernamepasswordbase64 = psd.converttobase64(usernamepassword)
token = psd.gettoken(usernamepasswordbase64)

### Date input format as "Date/Month/Year"
startdate = '01/01/2023'
enddate = '2/01/2023'

dt_dailyfueldata = psd.importdailyfuel(startdate,enddate,token)
dt_dailyfueldata.to_csv('DailyFuelData_'+startdate.replace('/','-')+'_to_'+enddate.replace('/','-')+'.csv',encoding="utf-8-sig",index=False)

dt_dailyenergycompare = psd.importdailyenergy(startdate,enddate,token)
dt_dailyenergycompare.to_csv('DailyEnergyData_'+startdate.replace('/','-')+'_to_'+enddate.replace('/','-')+'.csv',encoding="utf-8-sig",index=False)