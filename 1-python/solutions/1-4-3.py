'''

Let's make the code in 1-4-2 more resusable!!! 

move your functions into a module names `dateutils.py`

import your functions from `dateutils.py` into `1-4-3.py`

'''

from dateutils import parsedate_mdy, formatdate_ymd
from datetime import datetime

# Testing Code 
date = "12/30/2000"
date_dt_expect = datetime(2000, 12, 30)
date_dt_actual = parsedate_mdy(date)
assert date_dt_expect == date_dt_actual


# Testing with pytest
def test_formatdate_ymd():
    date_dt = datetime(2000, 12, 30)
    date_str_expect = "2000-12-30"
    date_str_actual = formatdate_ymd(date_dt)
    assert date_str_expect == date_str_actual


