def detect_tipper(tip_pct:float, 
                  tip_pct_75th_pctile:float, 
                  tip_pct_25th_pctile:float) -> str:
    if tip_pct > tip_pct_75th_pctile:
        return 'heavy tipper'
    if tip_pct < tip_pct_25th_pctile:
        return 'light tipper'
    
    return ''