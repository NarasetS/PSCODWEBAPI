from lib import ERCwebscraping


startrowid = 0
endrowid = 2
storingpath = ''

dat = ERCwebscraping.obtaindata(startrowid,endrowid)
dat = ERCwebscraping.combinerawdata()