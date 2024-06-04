from lib import ERCwebscraping


startrowid = 1
endrowid = 40
storingpath = ''

dat = ERCwebscraping.obtaindata(startrowid,endrowid)
dat = ERCwebscraping.combinerawdata()