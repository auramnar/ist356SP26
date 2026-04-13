from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from time import sleep
import sys


# function does browsing, scraping, and data extraction
def run(playwright: Playwright, year):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(f"https://cuse.com/sports/football/schedule/{year}")
    page.wait_for_load_state("load")

    # switch to table view
    page.get_by_role("tab", name="Table View").click()

    # wait for table
    page.wait_for_selector("table")

    # read table
    dfs = pd.read_html(page.content())
    df = dfs[0]

    context.close()
    browser.close()

    return df


with sync_playwright() as playwright:
    year = input("Enter year: ")
    df = run(playwright, year=str(year))

    print(df)

    # Save to CSV file
    output_filename = f"syracuse_football_schedule_{year}.csv"
    df.to_csv(output_filename, index=False, encoding="utf-8-sig")

    print(f"✅ Schedule saved to '{output_filename}'")