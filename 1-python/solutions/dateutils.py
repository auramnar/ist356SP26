from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    """
    Parses a date in the format "Month/Day/Year" and returns a datetime object.

    """
    return datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str:
    """
    Takes a datetime object and returns a string formatted as "YYYY-MM-DD".


    """
    return date.strftime("%Y-%m-%d")

if __name__ == "__main__":
# Main program 
    test = "12/30/2000"
    date = parsedate_mdy(test)
    print(date)
    date_str = formatdate_ymd(date)
    print(date_str)
 