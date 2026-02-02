    # Main program 
    test = "12/30/2000"
    date = parsedate_mdy(test)
    print(date)
    date_str = formatdate_ymd(date)
    print(date_str)