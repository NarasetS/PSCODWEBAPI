from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import ssl
import certifi


def obtaindata(startrowid, endrowid):
    
    list_id = [
    'ctl00_ContentPlaceHolder1_lblPowerPlantType',
    'ctl00_ContentPlaceHolder1_lblCompany_Personel',
    'ctl00_ContentPlaceHolder1_lblAddress',
    'ctl00_ContentPlaceHolder1_lblFuelTypeName',
    'ctl00_ContentPlaceHolder1_lblEXP_MW',
    'ctl00_ContentPlaceHolder1_lblSale_MW',
    'ctl00_ContentPlaceHolder1_lblApplicationDate',
    'ctl00_ContentPlaceHolder1_lblAcceptDate',
    #'ctl00_ContentPlaceHolder1_Label31',
    'ctl00_ContentPlaceHolder1_lblSignDate',
    'ctl00_ContentPlaceHolder1_lblSignNumber',
    'ctl00_ContentPlaceHolder1_lblSCOD',
    'ctl00_ContentPlaceHolder1_lblCOD',
    'ctl00_ContentPlaceHolder1_lblCancelRequestDate',
    'ctl00_ContentPlaceHolder1_lblCancelAcceptedDate',
    'ctl00_ContentPlaceHolder1_lblCancelContractDate',
    'ctl00_ContentPlaceHolder1_lblStatusText2'
    ]
    list_column = []
    for i in list_id :
        list_column.append(i[29:])
    list_column.append('rowid')
    df = pd.DataFrame(columns=list_column)

    for rowid in range(startrowid,(endrowid+1)):
        print("rowid = "+str(rowid))
        url = 'https://app03.erc.or.th/ERCSPP/ListViewDetail.aspx?RowID=' + str(rowid)
        res = requests.get(url,verify=False)
        res.encoding = "utf-8"
        if res.status_code == 404:
            print("Error 404 page not found with rowid = ",rowid)
        if res.status_code != 200 and res.status_code != 404:
            print("Not both 200 and 404 with rowid = ",rowid)
        
        bufferdf = []
        soup = BeautifulSoup(res.text, 'html.parser')
        for i in range(len(list_id)):
            buffer = soup.find_all(id=list_id[i])
            buffer[0] = buffer[0].get_text()
            bufferdf.append(buffer[0])
        bufferdf.append(rowid)
        if bufferdf[0] != '' :
            df.loc[len(df)] = bufferdf
            
    df.to_csv("ERCwebscrapingoutput\\"+str("From_" + str(startrowid) + "_to_" + str(endrowid) + "_Row_ExistingPlant.csv"),encoding="utf-8-sig",index=False)

    return None

def combinerawdata() :
    scrappingfilespath = "ERCwebscrapingoutput\\"
    scrappingdata = pd.DataFrame()

    for i in os.listdir(scrappingfilespath):
        scrappingfile = pd.read_csv(scrappingfilespath+i)
        scrappingdata = pd.concat([scrappingdata,scrappingfile])

    # scrappingdata = scrappingdata.drop(columns=['Unnamed: 0'])
    scrappingdata = scrappingdata.loc[scrappingdata['StatusText2'] == 'COD แล้ว']
    scrappingdata = scrappingdata.loc[scrappingdata['PowerPlantType'] != 'IPP']
    scrappingdata.reset_index(inplace=True,drop='index')
    print(scrappingdata)
    scrappingdata.to_csv(scrappingfilespath+"ExistingPlants.csv",encoding="utf-8-sig",index=False)
    
    return None

