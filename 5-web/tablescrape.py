from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from io import StringIO

# Function perform the browser automation tasks
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) #  # Launch the Chromium browser (headless=False shows the browser window)
    context = browser.new_context() # create a new browser context
    page = context.new_page() # open a new page or tab
    page.goto("https://en.wikipedia.org/wiki/National_Football_League") # go to the page
    
    html = StringIO(page.content()) # get the page content and wrap it in a StringIO object for pandas
    dfs = pd.read_html(html) # use pandas to read all tables from the page content

    df_teams = dfs[2]
    #print(df_teams) # get the first table which contains the teams
    df_teams.to_csv("nfl_teams.csv", index=False) # save the teams table to a CSV file
    
    
        
    # cleanup
    # close browser context
    # close browser to free up resources
    context.close()
    browser.close()

# launch playwright
# ensure it shuts down
with sync_playwright() as playwright:
    run(playwright)
    
