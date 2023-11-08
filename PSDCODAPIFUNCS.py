import requests
import json
import pandas as pd
from pandas import json_normalize
import base64

def converttobase64(usernamepassword) :
    sample_string = usernamepassword
    sample_string_bytes = sample_string.encode("ascii") 
    base64_bytes = base64.b64encode(sample_string_bytes) 
    base64_string = base64_bytes.decode("ascii")
    print("Convert U:P to base64 str")
    return base64_string

def gettoken(usernamepasswordBase64string) :
    print( "Getting Token" )
    url = "https://www.sothailand.com/PSCODWebAPI/api/LoginApi/GetToken"
    token = requests.get(url, headers={'Authorization': 'Basic ' + usernamepasswordBase64string})
    bufftoken = json.loads(token.content)
    outtoken = bufftoken['access_token']
    return outtoken


def importdailyfuel(startdate,enddate,token) :
    print( "Import daily fuel data from " + str(startdate) + " to " +  str(enddate) )
    url = "https://www.sothailand.com/PSCODWebAPI/api/FuelDataApi/GetDailyFuelWH"
    header = {
        'token' : token,
        'st' : startdate,
        'en' : enddate
    }
    data = requests.get(url, headers=header)
    df = json.loads(data.content)
    df = df['data']
    df = df['DailyFuelWH']
    df2 = json_normalize(df)  
    return df2

def importdailyenergy(startdate,enddate,token) :
    print( "Import daily energy data from " + str(startdate) + " to " +  str(enddate) )
    url = "https://www.sothailand.com/PSCODWebAPI/api/EnergyDataApi/GetDailyEnergyCompareWH"
    header = {
        'token' : token,
        'st' : startdate,
        'en' : enddate
    }
    data = requests.get(url, headers=header)
    df = json.loads(data.content)
    print(df)
    df = df['data']
    df = df['DailyEnergyCompareWH']
    df2 = json_normalize(df)  
    return df2

