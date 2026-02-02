'''
Let's make the code in 1-4-1 more resusable 

re-write the date parse into a function `parsedate_mdy(text: str) -> datetime:`   
re-write the date format into a function `formatdate_ymd(date: datetime) -> str:`  
re-write the main program to use both functions. input -> parsedate -> formatdate -> output


'''

from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    return datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")


# Main program
test = '12/30/2000'
date_dt = parsedate_mdy(test)
print(date_dt)
date_str = formatdate_ymd(date_dt)
print(date_str)  # Expected output: "2000-12-30"