from lib import ERCwebscraping


startrowid = 0
endrowid = 200000
storingpath = ''

dat = ERCwebscraping.obtaindata(startrowid,endrowid)
dat = ERCwebscraping.combinerawdata()