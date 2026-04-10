from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from time import sleep # add pause to allow page to load
import sys # handy for command line

# Create function that takes playwright object and year as input

def run(playwright: Playwright, year) -> str:
    browser = playwright.chromium.launch(headless=False) # launch browser
    context = browser.new_context() # open a new broser profile
    page = context.new_page() # open a tab
    
    # Complete the code to navigate to the page and extract the data
    