import datetime

defaultDate = "20170101"

def GetNowYMD():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")

def GetDefaultDate():
    return defaultDate

def SetDefaultDate(year, month, day):
    defaultDate = year + month + day